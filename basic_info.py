# функционал включает все требования basic_info.py и user_profile.py

name = input("Как тебя зовут? ")
while not name:
    name = input("Пожалуйста, введи имя ")
while not name.isalpha():
    name = input("Я не верю, что у тебя такое имя. Введи правильно ")

profession = input("Какова твоя профессия? ")
while not profession:
    profession = input("Пожалуйста, введи свою профессию ")
while not profession.isalpha():
    profession = input(
        "Профессия может быть повар, врач, милиционер, но не то, что ты написал "
    )

experience = input("Сколько лет ты уже работаешь? ")
while not experience:
    experience = input("Пожалуйста, введи свой стаж работы ")
while not experience.isdigit() or int(experience) < 0:
    experience = input("Пожалуйста, введи число лет своего стажа работы ")
while not 0 <= int(experience) <= 70:
    experience = input("Я не верю, что ты столько работал! Введи свой настоящий стаж ")

testtool = input("Какой твой любимый инструмент для тестирования? ")
while not testtool:
    testtool = input(
        "Я бы всё-таки хотел узнать, какой у тебя любимый инструмент для тестирования "
    )

answer = input("Ты знаешь, что такое переменная? ")
if (
    not "ссылка" in answer.lower()
    and answer.lower() != "знаю"
    and answer.lower() != "да"
):
    answer = False
else:
    answer = True

print(f"Привет, {name}! Добро пожаловать в мир Python для тестировщиков.")
print(f"Твой любимый инструмент: {testtool}. Отличный выбор!")
if answer:
    print("Здорово, что ты уже знаешь, что такое переменная")
