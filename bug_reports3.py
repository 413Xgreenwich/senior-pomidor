import random


critical_list = ["Trivial", "Low", "High", "Critical", "Blocker"]
counter = 1
bugs = {}
bugsall = {}
hello = "Добро пожаловать в баг-трекер! Введите 'help' для вывода списка команд"
bye = "Знание - сила. Береги его как следует."

doc = """
help         - вывести список команд
init <num>   - сгенерировать начальный список багов, num от 1 до 20, по умолчанию 10
new <status> - создать баг (Trivial, Low, High, Critical, Blocker)
change <id>  - изменить статус бага
del <id>     - удалить баг
list         - показать список багов по порядку создания
all          - показать список багов, включая удалённые
sort         - список багов по возростанию приоритета
tros         - список багов по убыванию приоритета
exit         - завершить программу
"""


def bterror(param=None):
    global critical_list
    if param == 1:
        print("Неизвестная команда. Список команд - 'help'")
    elif param == 2:
        print("У этой команды не может быть аргументов")
    elif param == 3:
        print("У этой команды может быть только один аргумент")
    elif param == 4:
        print(
            "Некорректный статус бага. Доступные статусы: Trivial, Low, High, Critical, Blocker"
        )
    elif param == 5:
        print(
            "Некорректный id бага. id бага может быть только числом. Посмотрите доступные баги по команде 'list'"
        )
    elif param == 6:
        print("В баг-трекере нет багов")
    elif param == 7:
        print("Общий список багов пуст")
    elif param == 8:
        print("Ошибка. Укажите id бага, статус которого хотите изменить")
    elif param == 9:
        print("Параметр должен быть числом")
    elif param == 10:
        print("Число начальных багов может быть от 1 до 20")
    elif param == 11:
        print(
            "Команда init может не может быть применена, если ранее были созданы баги"
        )
    else:
        print("Ошибка. Список команд - 'help'")


def btexit(param=None):
    if param == None:
        print(bye)
        exit()
    else:
        bterror(2)


def bthelp(param=None):
    if param == None:
        print(doc)
    else:
        bterror(2)


def btnew(param):
    global bugs
    global counter
    global critical_list
    if param in critical_list:
        bugsall[counter] = [param]
        bugs[counter] = [param]
        counter += 1
    elif len(param.split()) >= 2:
        bterror(3)
    else:
        bterror(4)


def btdel(param):
    global bugs
    if not bugs:
        bterror(6)
        return None
    if not param.isdigit():
        bterror(5)
        return None
    param = int(param)
    if param in bugs.keys():
        del bugs[param]
        bugsall[param] = ["Deleted"]
        print(f"Баг №{param} успешно удалён")
    else:
        print(f"Бага №{param} не существует")


def btlist(param=None):
    if param == None:
        if not bugs:
            bterror(6)
        else:
            for k, v in bugs.items():
                print(str(k) + ":", v[0])
    else:
        bterror(2)


def btall(param=None):
    if param == None:
        if not bugsall:
            bterror(7)
        else:
            for k, v in bugsall.items():
                print(str(k) + ":", v[0])
    else:
        bterror(2)


def btchange(param=None):
    global bugs
    if not bugs:
        bterror(6)
        return None
    elif param == None:
        bterror(8)
        return None
    elif int(param) not in bugs.keys():
        bterror(5)
    else:
        print(
            "Введите желаемый статус бага. Доступные статусы: Trivial, Low, High, Critical, Blocker"
        )
        while True:
            status = input()
            if status not in critical_list:
                bterror(4)
            else:
                break
        if [status] == bugs[int(param)]:
            print(f"Статус бага №{param} уже был {status}")
        else:
            bugs[int(param)] = [status]
            bugsall[int(param)] = [status]
            print(f"Статус бага №{param} успешно изменён на {status}")


def btsort(param=None):
    global bugs
    global critical_list
    if param != None:
        bterror(2)
    elif not bugs:
        bterror(6)
    else:
        sorted_bugs = sorted(
            bugs.items(), key=lambda item: critical_list.index(item[1][0])
        )
        for k, v in sorted_bugs:
            print(str(k) + ":", v[0])


def bttros(param=None):
    global bugs
    global critical_list
    if param != None:
        bterror(2)
    elif not bugs:
        bterror(6)
    else:
        sorted_bugs = sorted(
            bugs.items(), key=lambda item: critical_list.index(item[1][0]), reverse=True
        )
        for k, v in sorted_bugs:
            print(str(k) + ":", v[0])


def btinit(param=None):
    global bugs
    global critical_list
    if bugsall:
        bterror(11)
        return None
    elif param == None:
        print("Создан начальный список из 5 багов:")
        for _ in range(5):
            param_for_new_bug = random.choice(critical_list)
            btnew(param_for_new_bug)
            print(param_for_new_bug)
        return None
    elif len(param.split()) >= 2:
        bterror(3)
        return None
    elif not param.isdigit():
        bterror(9)
        return None
    elif not 1 <= int(param) <= 20:
        bterror(10)
        return None
    else:
        print(f"Создан начальный список из {param} багов:")
        for _ in range(int(param)):
            param_for_new_bug = random.choice(critical_list)
            btnew(param_for_new_bug)
            print(param_for_new_bug)


cmd_dict = {
    "help": bthelp,
    "exit": btexit,
    "error": bterror,
    "new": btnew,
    "del": btdel,
    "list": btlist,
    "all": btall,
    "sort": btsort,
    "tros": bttros,
    "error": bterror,
    "init": btinit,
    "new": btnew,
    "change": btchange,
    "del": btdel,
}

print(hello)

while True:

    print("BT $ ", end="")
    user_input = input().split(" ", 1)

    cmd = user_input[0]
    param = None
    if len(user_input) == 2:
        param = user_input[1]
    if cmd in cmd_dict:
        cmd_dict[cmd](param)
    else:
        bterror(1)
