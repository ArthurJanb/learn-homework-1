#-------------------
#Домашнее задание №1
#-------------------

# Исключения: приведение типов

#* Перепишите функцию discounted(price, discount, max_discount=20)
#  из урока про функции так, чтобы она перехватывала исключения,
#  когда переданы некорректные аргументы.
#* Первые два нужно приводить к вещественному числу при помощи float(),
#  а третий - к целому при помощи int() и перехватывать исключения
#  ValueError и TypeError, если приведение типов не сработало.

def discounted(price, discount, max_discount=20):

    try:                                                                        # конструкция try - except позволяет выловить исключение
        price = abs(float(price))                                               # в блоке try выполняется инструкция, в которой может быть исключение
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
    except (TypeError, ValueError):                                             # в блоке except указаны возможные исключения, если исключение определено
        return "Ошибка. Аргументам функции переданы неправильные значения"      # выводим ошибку

    if max_discount > 99:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount/100)
    return price_with_discount

if __name__ == '__main__':

    print(discounted(50, 3))       
    print(discounted(70, '6'))
    print(discounted('40', '3.3'))
    print(discounted('one', 13))
    print(discounted('twenty', 'one'))
    print(discounted(65.3, 12, '20'))
