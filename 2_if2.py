#-------------------
#Домашнее задание №1
#-------------------

#Условный оператор: Сравнение строк

#* Написать функцию, которая принимает на вход две строки
#* Проверить, является ли то, что передано функции, строками. 
#  Если нет - вернуть 0
#* Если строки одинаковые, вернуть 1
#* Если строки разные и первая длиннее, вернуть 2
#* Если строки разные и вторая строка 'learn', возвращает 3
#* Вызвать функцию несколько раз, передавая ей разные праметры 
#  и выводя на экран результаты

def compare_strings(string1, string2):
  #if isinstance(string1, str) and isinstance(string2, str):           # функция insinstance() позволяет проверить принадлежность 
   # print("Введенные переменные - строки")                            # помещенных данных в переменные к оперделенному классу (типу данных)
  if not isinstance(string1, str) and isinstance(string2, str):       # проверяем переменные на то, что они не принадлежат типу "str"
    return "0"
  elif string1 == string2:                                            # Если строки равны друг другу
    return "1"                                                        # вернуть - 1                                        
  elif string1 != string2 and len(string1) > len(string2):            # Если строки не равны и длина строки 1 > длины строки 2
    return "2"                                                        # вернуть - 2
  elif string1 != string2 and string2 == "learn":                     # Если строки не равны и строка 2 = значению "learn"
    return "3"                                                        # вернуть - 3
  
#string1 = 7                                                          # в переменную string1 помещаем число
#string2 = "learn"                                                    # в переменную string2 помещаем текст
#strings = compare_strings(string1, string2)                          
#print(strings)

#string1 = "learn"                                                    # в переменные string1 и string2 помещаем одинаковый текст
#string2 = "learn"
#strings = compare_strings(string1, string2)                           
#print(strings)

#string1 = "python"                                                   # в переменные string1 и string2 помещаем просто разный текст
#string2 = "test"
#strings = compare_strings(string1, string2)                         
#print(strings)


string1 = input("Введите переменную №1: ")                           # ввод пользователем переменной 1, но она всегда будет str
string2 = input("Введите переменную №2: ")                           # ввод пользователем переменной 2, но она всегда будет str
strings = compare_strings(string1, string2)                          
print(strings)
