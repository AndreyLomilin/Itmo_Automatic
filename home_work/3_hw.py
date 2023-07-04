def month(a, b):
    if a > b:
        print(a)
    else:
        print(b)
month(8, -3)



def diff(a, b):
    res = abs(a - b)
    if res == 135:
        print('Yes')
    else:
        print('No')
diff(-200, -66)



def season(m):
    if m >=3 and m <= 5:
        print('Весна')
    elif m >= 6 and m <= 8:
        print('Лето')
    elif m >= 9 and m <= 11:
        print('Осень')
    elif m >= 1 and m<= 2:
        print('Зима')
    elif m >= 12 and m<= 12:
        print('зима')
season(6)



def nums(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')
nums(11, 101, 20)



def positive(list):
    count = 0
    for i in list:
        if i > 0:
            count +=1
    print('Количество положительных чисел: ', count)
nums = [-3, 4, 10, 0, 20]
positive(nums)


def days(a, b):
   res = ((a * 365) + (b * 29))
   print('Количество дней ', res)

days(1, 3)










