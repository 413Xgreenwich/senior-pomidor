doc = """
help - вывести список команд
init <num> - сгенерировать начальный список багов, num от 1 до 10, по умолчанию 5
new - создать баг
change <id> - изменить статус бага
del <id> - удалить баг с выбранным номером
list - показать список багов по порядку создания
sort - список багов по приоритету
exit - завершить программу
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

bug_reports = {}


def bthelp():
    print(doc)


def btexit():
    exit()


def btlist():
    if not bug_reports:
        print("В баг-трекере нет багов.")
    else:
        for k, v in bug_reports.items():
            print(k[0], str(k[1]) + ":", v)


def btinit(num=5):
    global bug_reports
    global bug_reports_add
    if bug_reports:
        print(
            "Начальный набор багов сгенерирован, или как минимум один баг создан вручную"
        )
    else:
        for i in range(num):
            bug_reports[("Ошибка", i + 1)] = bug_reports_add[("Ошибка", i + 1)]


cmd_dict = {"help": bthelp, "exit": btexit, "init": btinit, "list": btlist}

cmd = input(
    "Добро пожаловать в баг-трекер! Введите 'help' для вывода списка команд \nBT $ "
)
while True:
    cmd_dict[cmd]()
    cmd = input("BT $ ")
