#-------------------
#Домашнее задание №1
#-------------------

#Условный оператор: Возраст

#* Попросить пользователя ввести возраст при помощи input и положить 
#  результат в переменную
#* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
#  учиться в детском саду, школе, ВУЗе или работать
#* Вызвать функцию, передав ей возраст пользователя и положить результат 
#  работы функции в переменную
#* Вывести содержимое переменной на экран

def destiny(age):
  if age <= 0:
    return "Пользователь не родился."
  elif 2 <= age <=6:
    return "Пользователь ходит в детский сад."
  elif 7 <= age <= 17:
    return "Пользователь учится в школе."
  elif 18 <= age <= 21:
    return "Пользователь учится в университете."
  elif 22 <= age <= 65:
    return "Пользователь ходит на работу."
  else:
    return "Возраст введен некорректно либо Вы слишком стар :)"
  
age = int(input("Введите свой возраст: "))
result = destiny(age)
print(result)
