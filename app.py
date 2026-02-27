from flask import Flask
from methods import access
import requests

token = access.token()
api = access.api()

application = Flask(__name__)


# импортируем вынесенные обработчики
from tests.init_tests import hello, check_params


#тест ответа
application.add_url_rule('/flask_test', 'hello', hello)



# создаем webhook
@application.route("/set_webhook")
def webhook():
    url = api + token + '/setWebhook'
    print(url)
    
    params = {'url' : 'https://d5dpm6fnp971a1fjon84.cmxivbes.apigw.yandexcloud.net/main'
    }
    r = requests.post(url,
                      json=params)

    print(r.status_code)
    print(r.text)
    return "!", 200


application.add_url_rule('/check_params', 'check_params', check_params, methods=['GET', 'POST'])