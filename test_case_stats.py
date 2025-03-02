test_case_stats = {
    "понедельник": None,
    "вторник": None,
    "среду": None,
    "четверг": None,
    "пятницу": None,
}

sum = 0

for k, v in test_case_stats.items():
    number = input(f"Сколько тест-кейсов ты выполнил в {k}? ")
    while number is None or not number.isdigit() or int(number) < 0:
        number = input(f"Введи число тест-кейсов, который ты успел выполнить в {k}? ")
    test_case_stats[k] = number
    sum += int(number)


# print(test_case_stats)

if sum / 5 > 10:
    print(f"Отличная работа! Ты проходил в среднем {round(sum/5)} тест-кейсов в день!")
# мне было впадлу кодить склонение для (1) "тест-кейс", (2, 3, 4) "тест-кейса", (5, ) "тест-кейсов", но умею
elif 0 < sum / 5 <= 10:
    print(
        f"Попробуй улучшить результат. Ты проходил всего в среднем {round(sum/5)} тест-кейсов в день."
    )
else:
    print(f"Настоящий волчара! Зачем работать если можно не работать?")
