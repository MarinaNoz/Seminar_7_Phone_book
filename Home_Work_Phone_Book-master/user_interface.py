import check

def start():
    greetings = 'Привет!\n'\
                'Это телефонныйая справочник.\n' \
                'На данный момент возможности ограничены следующим функционалом:\n' \
                'Возможно:\n' \
                '* Создать новую книгу или очистить существующую\n' \
                '* Добавить новый контакт\n' \
                '* Изменить номер телефона у выбранного контакта\n' \
                '* Изменить фамилию телефона у выбранного контакта\n' \
                '* Удалить контакт\n' \
                '* Показать все контакты\n' \
                '* Экспорт телефонного справочника в форматы TXT и CSV\n'
    print(f'{greetings}\n')

def menu():
    what_to_do = 'Выберите действие соответствующее пункту меню:'
    new_book = '1. Создать новую книгу или очистить существующую'
    new_contact = '2. Добавить новый контакт'
    change_number = '3. Изменить номер телефона'
    change_surname = '4. Изменить фамилию'
    delete_contact = '5. Удалить контакт'
    view_all_contact = '6. Показать все контакты'
    export = '7. Экспорт телефонного справочника в формат TXT лил CSV'
    to_exit = '8. Выход'
    print(f'{what_to_do}\n'
          f'\n{new_book}\n'
          f'{new_contact}\n'
          f'{change_number}\n'
          f'{change_surname}\n'
          f'{delete_contact}\n'
          f'{view_all_contact}\n'
          f'{export}\n'
          f'{to_exit}')
    return check.digit_check()