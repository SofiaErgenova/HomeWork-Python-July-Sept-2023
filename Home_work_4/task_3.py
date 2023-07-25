"""
Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте 
все операции поступления и снятия средств в список.
"""

"""
Задание №6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

summ = 0
count_add = 0
count_out = 0
operations = [] 

def iswealth(money):
    """Проверка на богатство"""

    if int(money) > 5_000_000:
        print("С вас сняли налог на богатство", money * 0.1)
        money -= money * 0.1
        return money
    else:
        return money
    
def added_sum(money_add):
    """Пополнение счета"""

    global summ
    global count_add
    global operations
    if money_add % 50 == 0:
            summ += money_add
            count_add += 1
            if count_add % 3 == 0:
                summ *= 1.03
    else:
        print("Введена некорректная сумма (не кратна 50)")
        
    operation = {"Тип": "Пополнение счета", "Сумма": money_add} 
    operations.append(operation) 
    return summ

def cash_withdrawal(money_out):
    """Снятие наличных"""

    global count_out
    global summ
    global operations
    comission = money_out * 0.015
    if comission < 30:
            comission = 30
    elif comission > 600:
            comission = 600

    if money_out + comission > summ:
        print("Недостаточно средств")

    else:
        if money_out % 50 == 0:
            summ -= money_out + comission
            count_out += 1
            if count_out % 3 == 0:
                    summ *= 1.03
            operation = {"Тип": "Снятие наличных", "Сумма": money_out}
            operations.append(operation) 
            return summ
        else:
            print("Введена некорректная сумма")
            return summ

while True:
    action = input(" q - выход из банокмата \n а - пополнить счет \n о - снять наличные \n ваше действие: ")

    if action == "q":
        print("Выходим из банкомата")
        print(f"Сумма: {summ} и список действий: {operations}")
        break     

    elif action == "a":
        summ_add = int(input("Сумма пополнения: "))
        summ = iswealth(summ)
        summ = added_sum(summ_add)

    elif action == "o":
        summ_out = int(input("Сумма снятия: "))
        summ = iswealth(summ)
        summ = cash_withdrawal(summ_out)
    
    print(f"Сумма: {summ} и список действий: {operations}")


