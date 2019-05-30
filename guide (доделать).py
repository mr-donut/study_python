import json

print('Создать:(1) Найти:(2) Редактировать:(3) Удалить:(4) Выйти:(5)')
key_list = ('1', '2', '3', '4', '5')

sprav = []
with open("guide.txt", "r") as f:
    sprav = json.loads(f.read())

for i in key_list:

    count = 0
    with open('guide.txt', 'r') as file:
        for line in file:
            count += 1
    print("Записей в телефонном справочнике: ", count)

    action = int(input())

    sprav_record = {}
    if action == 1:
        sprav_record["number"] = input(str('Ввести номер абонента: '))
        sprav_record["name"] = input(str('Ввести имя абонента: '))
        sprav_record["surname"] = input(str('Ввести фамилию абонента: '))

        sprav.append(sprav_record)
        with open("guide.txt", "w") as file:
            file.write(json.dumps(sprav, indent=4))
            # print(sprav, file=file)
        continue

    if action == 2:
        a = 0

    if action == 5:
        break