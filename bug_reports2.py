import random


critical_list = ["Trivial", "Low", "High", "Critical", "Blocker"]

counter = 1


bugs = {}
# формат - id: [приоритет]


def bthelp():
    print(doc)


def btexit():
    exit()


def bterror(param=1):
    if param == 3:
        print("У этой команды может быть только один аргумент")
    elif param == 2:
        print("У этой команды не может быть аргументов")
    else:
        print("Неизвестная команда. Список команд - 'help'")


def btnew(param):
    global bugs
    global counter
    bugs[counter] = [param]
    counter += 1


def btdel(param):
    global bugs
    param = int(param)
    if param in bugs.keys():
        if bugs[param] == "Deleted":
            print(f"Бага №{param} не существует")
        else:
            bugs[param] = ["Deleted"]
            print(f"Баг №{param} успешно удалён")
    else:
        print(f"Бага №{param} не существует")


def btlist():
    if not bugs:
        print("В баг-трекере нет багов.")
    else:
        for k, v in bugs.items():
            print(str(k) + ":", v[0])


cmd_dict = {
    "help": bthelp,
    "exit": btexit,
    "error": bterror,
    "new": btnew,
    "del": btdel,
    "list": btlist,
}
cmd_param_dict = {"error": bterror, "new": btnew, "del": btdel, "list": btlist}

doc = """
help         - вывести список команд
init <num>   - сгенерировать начальный список багов, num от 1 до 10, по умолчанию 5
new <status> - создать баг (Trivial, Low, High, Critical, Blocker)
change <id>  - изменить статус бага
del <id>     - удалить баг
list         - показать список багов по порядку создания
all          - показать список багов, включая удалённые
sort         - список багов по возростанию приоритета
tros         - список багов по убыванию приоритета
exit         - завершить программу
"""


print("Добро пожаловать в баг-трекер! Введите 'help' для вывода списка команд")

while True:

    print("BT $ ", end="")
    user_input = input().split()

    
    if len(user_input) == 2 and user_input[0] in cmd_param_dict.keys():
        cmd = user_input[0]
        param = user_input[1]
        cmd_dict[cmd](param)
        del param
    elif len(user_input) >= 2 and user_input[0] in cmd_param_dict.keys():
        cmd = "error"
        param = 4
        cmd_dict[cmd](param)
        del param
    elif len(user_input) > 2 and user_input[0] in cmd_param_dict.keys():
        cmd = "error"
        param = 3
        cmd_dict[cmd](param)
        del param
    elif len(user_input) == 1 and user_input[0] in cmd_dict.keys():
        cmd = user_input[0]
        cmd_dict[cmd]()
        
    elif len(user_input) >= 2 and user_input[0] in cmd_dict.keys():
        cmd = "error"
        param = 2
        cmd_dict[cmd](param)
        del param
    else:
        cmd = "error"
        param = 1
        cmd_dict[cmd](param)
        del param
