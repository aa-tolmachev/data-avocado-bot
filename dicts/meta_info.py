from methods.emoji import emoji

reply_markup_main = {'keyboard': [['Активности'],['Кошелек'],['Дела']], 'resize_keyboard': True, 'one_time_keyboard': False}


markup_non_important_to_tommorow = {'keyboard': [['Перенеси неважные на завтра'], ['Все задачи выполнил'], ['меню']],'resize_keyboard': True,'one_time_keyboard': False}


#кнопки активностей - соответствуют сферам колеса баланса
markup_activities = {'keyboard': [[emoji('банкноты') + ' Работа', emoji('семья') + ' Семья']
                                 ,[emoji('красный крест') + ' Здоровье', emoji('бонсай') + ' Хобби']
                                 ,[emoji('медитация') + ' Отдых', emoji('книги') + ' Развитие']
                                 ,['Меню']]
                    ,'resize_keyboard': True, 'one_time_keyboard': False}
