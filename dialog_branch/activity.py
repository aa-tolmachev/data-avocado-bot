from methods import psql_methods

from dicts import meta_info

from dialog_branch import primary


#кнопки активностей -> тип активности в public.activities (по нему считается колесо баланса)
dict_activity_types = {'Работа' : 'работа'
                      ,'Семья' : 'семья'
                      ,'Здоровье' : 'здоровье'
                      ,'Хобби' : 'хобби'
                      ,'Отдых' : 'отдых'
                      ,'Развитие' : 'развитие'
                      }


#получаем тип активности по нажатой кнопке (кнопка с эмодзи, поэтому ищем название внутри)
def activity_from_command(command = None):
    activity_type = None
    for button_name in dict_activity_types:
        if button_name in command:
            activity_type = dict_activity_types[button_name]
    return activity_type


def main(command = None , chat_id = None, dict_user_data = None,json_update = None):

    text = 'непонимайт...'
    reply_markup = meta_info.reply_markup_main


    last_state = dict_user_data['last_state']
    state_info_1 = dict_user_data['state_info_1']
    user_id = dict_user_data['user_id']

    reply_markup_main = meta_info.reply_markup_main
    markup_activities = meta_info.markup_activities

    #6 - Активности
    if 'Активности' in command:
        r = psql_methods.last_state(chat_id,command)
        text = 'Что за прекрасную активность ты хочешь записать?'
        reply_markup = markup_activities

    #6-> начало работы с активностями
    elif last_state == 'Активности':
        activity_type = activity_from_command(command = command)

        #6->1 Меню - возвращаемся на исходную
        if command == 'Меню':
            text = primary.menu(chat_id = chat_id , command = command)
            reply_markup = reply_markup_main

        #6->2 записываем активность и остаемся в активностях - можно записать еще
        elif activity_type is not None:
            r = psql_methods.add_activity(chat_id = chat_id , activity_type = activity_type , dict_user_data = dict_user_data)
            text = r['text']
            reply_markup = markup_activities if r['reply_markup'] is None else r['reply_markup']

        #6->3 непонятная команда - предлагаем выбрать на кнопках
        else:
            text = 'Не знаю такой активности... Выбери на кнопках или нажми "Меню"'
            reply_markup = markup_activities


    return text , reply_markup
