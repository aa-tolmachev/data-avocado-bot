import psycopg2
from methods import access

def restore_connection():
    import methods.psql_methods as psql_methods
    import methods.psql_cron_methods as psql_cron_methods
    import methods.psql_watch_methods as psql_watch_methods

    PSQL_heroku_keys = access.PSQL_heroku_keys()
    conn_string = "dbname='%(dbname)s' port='%(port)s' user='%(user)s' host='%(host)s' password='%(password)s'" % PSQL_heroku_keys

    for module in [psql_methods, psql_cron_methods, psql_watch_methods]:
        if module.conn.closed != 0:
            module.conn = psycopg2.connect(conn_string)
