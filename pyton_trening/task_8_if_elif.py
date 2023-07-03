num = 3.4
if num > 0:
    print("Положительное число")
elif num == 0:
    print("Ноль")
else:
    print("Чмсло отрицательное")

permit_print = True
if num > 0 and permit_print:
    print("num - положительное число")
elif not  permit_print:
    print("печать завершена")





