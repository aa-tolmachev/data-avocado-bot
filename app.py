from flask import Flask
from methods import access

token = access.token()
api = access.api()

application = Flask(__name__)


#тест 
@application.route('/flask_test')
def hello():
    return 'Hello, World!'



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