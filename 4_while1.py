#-------------------
#Домашнее задание №1
#-------------------

#Цикл while: hello_user

#* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
#  пользователя “Как дела?”, пока он не ответит “Хорошо”


def hello_user():

    user_answer = ""

    while user_answer != "Лучше всех!":
            print("Как дела?")
            user_answer = input("")

hello_user()