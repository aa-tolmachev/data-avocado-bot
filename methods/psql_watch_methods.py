import psycopg2
from datetime import datetime, timedelta
from methods import access

PSQL_heroku_keys = access.PSQL_heroku_keys()

#подключение к PSQL
conn = psycopg2.connect("dbname='%(dbname)s' port='%(port)s' user='%(user)s' host='%(host)s' password='%(password)s'" % PSQL_heroku_keys)


def now_str():
    now = datetime.now()
    now_str = str(now.year)+str(now.month if now.month >= 10 else  '0'+str(now.month))+str(now.day if now.day >= 10 else  '0'+str(now.day)) +' '+str(now.hour if now.hour >= 10 else  '0'+str(now.hour)) + str(now.minute if now.minute >= 10 else  '0'+str(now.minute)) + str(now.second if now.second >= 10 else  '0'+str(now.second))
    return now_str


def track_activity(user_id=None, activity_type=None, activity_from=None, family_id=None):
    cur = conn.cursor()
    now = now_str()

    user_id = int(user_id)

    if family_id is None:
        cur.execute("INSERT INTO public.activities (user_id, date_activity, activity_type, activity_from) VALUES (%(user_id)s, '%(now)s', '%(activity_type)s', '%(activity_from)s')" % {'user_id': user_id, 'now': now, 'activity_type': activity_type, 'activity_from': activity_from})
    else:
        cur.execute("INSERT INTO public.activities (user_id, family_id, date_activity, activity_type, activity_from) VALUES (%(user_id)s, %(family_id)s, '%(now)s', '%(activity_type)s', '%(activity_from)s')" % {'user_id': user_id, 'family_id': family_id, 'now': now, 'activity_type': activity_type, 'activity_from': activity_from})

    conn.commit()
    cur.close()

    return 200
