# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arifmetic_progression(first_element, difference, counter):
    arifmetic_progression = list(range(counter))

    index = 0
    for j in range(first_element, counter * 2, difference):
        arifmetic_progression[index] = j
        index += 1

    print(arifmetic_progression)

first_element = int(input("Введите первый элемент арифметической прогрессии: "))
difference = int(input("Введите разность арифметической прогрессии: "))
counter = int(input("Введите последнее значение арифметической прогрессии: "))
arifmetic_progression(first_element, difference, counter)
