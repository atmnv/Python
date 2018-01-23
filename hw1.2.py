
"""ДЗ номер 1-2
Работал Атманов Дидар"""

firstString = input("Введите первую строку: ")
secondString = input("Введите вторую строку: ")
if firstString > secondString and firstString.isalpha() and secondString.isalpha():
    print ("Первая строка больше -", firstString )
elif firstString < secondString:
    print ("Вторая строка больше -", secondString )
else :
    print("Строки равны!!!")

