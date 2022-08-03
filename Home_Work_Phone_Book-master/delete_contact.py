import json
import controller

path_to_db = 'db.json'

def delete_contact():

    del_id = input('Введите id записи, которую необходимо удалить:  ')
    id = int(del_id)

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, id+1):
            if data[i]['id'] == id:
                del data[i]
        # if name not in data:
        #         print('Такого контакта нет')
    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nКонтакт успешно изменена удалён!\n')
    controller.user_choice()