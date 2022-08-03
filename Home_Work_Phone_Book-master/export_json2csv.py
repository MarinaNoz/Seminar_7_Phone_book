import json
import csv
import controller
from time import sleep
path_to_db = 'db.json'

def export_json2csv():
    with open(path_to_db) as json_file:
        json_obj = json.load(json_file)
    output_dir = input(r'Укажите путь экспорта (Пример: c:\user_dir\csv\):''\n')
    output_file = input('Введите имя экспортируемого файла, с расширением (Пример: db.csv):\n')
    data_file = open(output_dir + output_file, 'w', newline='')
    csv_writer = csv.writer(data_file)
    count = 0
    for data in json_obj:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
    data_file.close()
    print(f'Файл {output_file}, успешно экспортирован в {output_dir}\n')
    sleep (5)
    controller.user_choice()