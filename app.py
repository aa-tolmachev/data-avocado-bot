from flask import Flask
from dotenv import load_dotenv
load_dotenv()
from methods import access
import requests

# load environment-dependent tokens/configs
token = access.token()
api = access.api()

application = Flask(__name__)


# импортируем вынесенные обработчики
from tests.init_tests import hello, check_params


#тест ответа
application.add_url_rule('/flask_test', 'hello', hello)
#тест вывода параметров
application.add_url_rule('/check_params', 'check_params', check_params, methods=['GET', 'POST'])


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


# запуск основной функции
@application.route('/main', methods=['GET', 'POST'])
def main():
    try:
        json_update = json.loads(request.get_data())

        print(json_update)

        #Изначально для отправки кнопки пустые
        reply_markup = None
        #главное меню
        global g_reply_markup_main
        reply_markup_main = g_reply_markup_main

        #получаем id чата и текст сообщения
        chat_id = json_update['message']['chat']['id']
        command = json_update['message']['text']

        #получаем список трат
        keyboard_expense , list_expense_types = reply.list_expense_types()

        #получаем текущее состояние
        dict_user_data = psql_methods.user_data(chat_id)
        last_state = dict_user_data['last_state']
        state_info_1 = dict_user_data['state_info_1']
        state_info_2 = dict_user_data['state_info_2']
        state_info_3 = dict_user_data['state_info_3']
        state_info_4 = dict_user_data['state_info_4']
        state_info_5 = dict_user_data['state_info_5']
        user_id = dict_user_data['user_id']
        personal_wallet_id = dict_user_data['personal_wallet_id']


        #определяем направление ветки разговора
        meta_path = router.route.meta(chat_id = chat_id , command = command ,dict_user_data= dict_user_data)

        #направляем на запуск ветки разговора
        text , reply_markup = router.route.make_dialog_branch(meta_path= meta_path, chat_id= chat_id, command= command , dict_user_data= dict_user_data , json_update = json_update)

        #отправляем сообщение
        send_result = telegram_bot_methods.send_message(chat_id = chat_id, text = text, reply_markup = reply_markup)
  
        return "!", 200
    except:

        #тест - для тестирования
        traceback.print_exc()

        return "!", 200