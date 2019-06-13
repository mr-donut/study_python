import json
import os

full_name = "guide.txt"

print('Создать:(1) Найти:(2) Редактировать:(3) Удалить:(4) Выйти:(5)')
key_list = ('1', '2', '3', '4', '5')

sprav = []

if os.path.isfile(full_name):
    with open(full_name, "r") as f:
        sprav = json.loads(f.read())

for i in key_list:

    count = 0
    if os.path.isfile(full_name):
        with open(full_name, 'r') as file:
            for line in file:
                count += 1
    # print("Записей в телефонном справочнике: ", count)

    action = int(input("Ввести номер действия "))

    sprav_record = {}

    if action == 1:
        sprav_record["number"] = input(str('Ввести номер абонента: '))
        sprav_record["name"] = input(str('Ввести имя абонента: '))
        sprav_record["surname"] = input(str('Ввести фамилию абонента: '))

        print("Добавлен новый абонент"'\n',
              "Имя абонента: ", sprav_record["name"],'\n',
              "Фамилия абонента: ", sprav_record["surname"],'\n',
              "Номер абонента: ", sprav_record["number"]
        )
        sprav.append(sprav_record)

        with open(full_name, "w") as file:
            file.write(json.dumps(sprav, indent=4))
        continue

    if action == 2:
        who_to_find = input("Ввести номер или имя, или фамилию абонента: ")
        with open(full_name, 'r') as file:
            data = json.loads(file.read())

            def search(something):
                for item in data:
                    if item['name'] == something:
                        return item
                    elif item['surname'] == something:
                        return item
                    elif item['number'] == something:
                        return item
                return None

            locations = [i for i, t in enumerate(data) if t["name"] == who_to_find or t["surname"] == who_to_find or t["number"] == who_to_find][0]
            print(search(who_to_find))
            print("Имя абонента: ", data[locations]['name'], '\n',
                  "Фамилия абонента: ", data[locations]['surname'], '\n',
                  "Номер абонента: ", data[locations]['number'])
            print("Запись в справочнике №", locations)

    if action == 3:
        data = json.load(open(full_name))
        guide_id = int(input("Ввести номер записи для редактирования: "))
        print("Имя абонента: ", data[guide_id]['name'],'\n',
              "Фамилия абонента: ", data[guide_id]['surname'],'\n',
              "Номер абонента: ", data[guide_id]['number'])

        data[guide_id]["number"] = input(str('Ввести новый номер абонента: '))
        data[guide_id]["name"] = input(str('Ввести новое имя абонента: '))
        data[guide_id]["surname"] = input(str('Ввести новую фамилию абонента: '))
        print("Имя абонента: ", data[guide_id]['name'],'\n',
              "Фамилия абонента: ", data[guide_id]['surname'],'\n',
              "Номер абонента: ", data[guide_id]['number'])
        open(full_name, "w").write(json.dumps(data, sort_keys=True, indent=4))

    if action == 4:
        data = json.load(open(full_name))
        guide_id = int(input("Ввести номер записи для удаления: "))
        data.pop(guide_id)
        print("Запись в справочнике №", guide_id, "удалена")
        open(full_name, "w").write(json.dumps(data, sort_keys=True, indent=4))

    if action == 5:
        break