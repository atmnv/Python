
"""ДЗ номер 1-3
Работал Атманов Дидар"""

firstNumber = int(input("Введите первое число: "))
secondNumber = int(input("Введите второе число: "))
balance = firstNumber % secondNumber
if balance != 1:
    print (balance)
else : print ("Остаток равен = ",balance)
