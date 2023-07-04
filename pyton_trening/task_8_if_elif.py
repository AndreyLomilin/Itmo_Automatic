# num = 3.4
# if num > 0:
#     print("Положительное число")
# elif num == 0:
#     print("Ноль")
# else:
#     print("Чмсло отрицательное")
#
# permit_print = True
# if num > 0 and permit_print:
#     print("num - положительное число")
# elif not  permit_print:
#     print("печать завершена")

level = int(input('Введите курс: '))
if level >= 1 and level <= 4:
    print('Бакалавр')
elif level >= 5 and level <= 6:
    print('Магистр')
elif level >=7 and level <= 9:
    print('Аспирант')
else:
    print('Ведите корректный год обучения')





