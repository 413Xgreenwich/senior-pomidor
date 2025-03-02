doc = """
help - вывести список команд
init - сгенерировать начальный список багов
new - создать баг
change <id> - изменить статус бага
del <id> - удалить баг с выбранным номером
list - показать список багов по порядку создания
sort - список багов по приоритету
end - завершить программу
"""

bug_reports_add = {
    ("Ошибка", 1): "High",
    ("Ошибка", 2): "Low",
    ("Ошибка", 3): "Trivial",
    ("Ошибка", 4): "Critical",
    ("Ошибка", 5): "Blocker",
    ("Ошибка", 6): "Low",
    ("Ошибка", 7): "Low",
    ("Ошибка", 8): "High",
    ("Ошибка", 9): "Trivial",
    ("Ошибка", 10): "Critical",
}

critical_list = ["Trivial", "Low", "High", "Critical", "Blocker"]

bug_counter = 0
init_status = False


bug_reports = []

def bthelp():
    print(doc)

def btend():
    exit()

cmd_dict = {
    "help": bthelp,
    "end": btend
}


cmd = input("Добро пожаловать в баг-трекер! Введите 'help' для вывода списка команд \nBT $ ")


while True:

    cmd_dict[cmd]()
    cmd = input("BT $ ")
