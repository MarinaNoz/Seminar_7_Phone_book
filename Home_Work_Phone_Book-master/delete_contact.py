import json
import controller

path_to_db = 'db.json'

def delete_contact():
    del_id = input('Введите id записи, которую необходимо удалить:  ')

    # with open(path_to_db, 'r', encoding='UTF-8') as json_data:
    #     json_data = json.load(open(path_to_db))
    #
    # # Iterate through the objects in the JSON and pop (remove)
    # # the obj once we find it.
    # for i in range(len(json_data)):
    #     if json_data[i]["id"] == del_id:
    #         json_data.pop(i)
    #         break
    #
    # # Output the updated file with pretty JSON
    # with open(path_to_db, 'w', encoding='UTF-8') as file:
    #     json.dump(json_data, file, indent=4)





    # with open(path_to_db, 'r', encoding='UTF-8') as json_data:
    #     data = json.load(json_data)
    #
    # for i in data:
    #     if i['id'] == del_id:
    #         #data.remove(i)
    #         del data[i]
    #
    # with open(path_to_db, 'w') as json_data:
    #     json.dump(data, json_data, indent=4)



    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if del_id == data[i]['id']:
                del data[i]
        # if name not in data:
        #         print('Такого контакта нет')
    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print(f'\nЗапись успешно удалёна!\n')
    controller.user_choice()




# import json
# import controller
#
#
# path_to_db = 'db.json'
#
#
# def delete_contact():
#     id = input('Введите имя или фамилию контакта, которого надо удалить:  ')
#
#     with open(path_to_db, 'r', encoding='UTF-8') as file:
#         data = json.load(file)
#         for i in range(0, len(data)):
#             if id == data[i]['id']:
#                 print(data[i][id])
#             #if name == data[i]['Name'] or name == data[i]['Surname']:
#                 del data[i]
#         # if name not in data:
#         #         print('Такого контакта нет')
#     with open(path_to_db, 'w', encoding='UTF-8') as file:
#         json.dump(data, file, indent=4)
#     print('\nКонтакт успешно изменена удалён!\n')
#     controller.user_choice()