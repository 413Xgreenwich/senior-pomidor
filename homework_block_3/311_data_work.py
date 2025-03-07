import json


operator = (("name", "Александр"), ("mail", "sanches2101@gmail.com"))
# данные переменной operator конечно нельзя будет поменять, но можно переопределить саму переменную
# к сожалению Python не поддерживаются неизменяемые константы

ok_mark = "[OK]"
warning_mark = "[WARNING]"


with open("homework_block_3/response.json", "r", encoding="utf-8") as raw_response:
    response = json.load(raw_response)


# убедимся, что заказы есть в ответе от сервера
print()
orders_num = len(response['data'])
if orders_num > 0:
    print(f'{ok_mark} В ответе от сервера есть заказы. Их количество - {orders_num}')
else:
    print(f'{warning_mark} В ответе от сервера нет ни одного заказа')


# убедимся, что время выполнения первого и второго заказов не превышает 6 часов
# поскольку логика не очень внятно описана, возьмём "время выполнения первого и второго заказов" как сумму "delay" для этих заказов

if response['data'][0]['delay'] + response['data'][1]['delay'] <= 6:
    print(f"{ok_mark} Время выполнение первого и второго заказов не превышает 6 часов")
else:
    print(f"{warning_mark} Время выполнение первого и второго заказов превышает 6 часов")


# Убедимся, что для для третьего заказа все услуги обработаны и выполнено не меньше половины
# Ну или по крайней мере на текущий момент возвращено не больше, чем выполнено, а ожидают возврат не больше, чем уже возвращено

num = 3 # номер заказа

als = response['data'][num-1]['count']            # als от all services - количество услуг
cms = response['data'][num-1]['completed']        # cms от completed services - завершённые услуги
wrs = response['data'][num-1]['wait_refund']      # wrs от wait refund services - услуги ожидающие возврата
rfs = response['data'][num-1]['refunded']         # rfs от refunded services - возвращённые услуги

if als > cms+wrs+rfs:
    print(f"{warning_mark} Для заказа {num} не все услуги обработаны")
elif als == cms+wrs+rfs and cms >= als//2:
    print(f"{ok_mark} Для заказа {num} все услуги обработаны и выполнено не меньше половины")
elif rfs <= cms and wrs <= rfs:
    print(f"{ok_mark} Для заказа {num} все услуги обработаны и возвращено не больше, чем выполнено, а ожидают возврат не больше, чем уже возвращено")
else:
    print(warning_mark)
print()

# отчёт - массив (список) id заказов

id_list = []
for i in range(len(response['data'])):
    id_list.append(response['data'][i]["_id"])
print("Список id заказов: ", *id_list, sep = "\n")
print()

# объект (словарь), который содержит в себе инфу о том, сколько всего услуг выполненных, возвращенных и ожидающих возврат

service_dict = {'cms': 0, 'wrs': 0, 'rfs': 0}
for i in range(len(response['data'])):
    service_dict['cms'] += response['data'][i]['completed']
    service_dict['wrs'] += response['data'][i]['wait_refund']
    service_dict['rfs'] += response['data'][i]['refunded']

print(f"Всего выполненных услуг в заказе: {service_dict['cms']}")
print(f"Всего возвращенных услуг в заказе: {service_dict['wrs']}")
print(f"Всего ожидающих возврат услуг в заказе: {service_dict['rfs']}")
print()


print(f"Имя автора: {operator[0][1]}\nПочта автора: {operator[1][1]}")
print()


new_id = "326b23a1-e6ab-4b4a-84a1-a3ecb33afc97"
id_list.append(new_id)
print(f"В список id заказов добавлен новый идентификатор: {new_id}\n\nНовый список id заказов: ", *id_list, sep = "\n")
print()