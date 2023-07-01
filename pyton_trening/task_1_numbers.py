a = 2
print (a, "относиться к типу", type(a))


b = 15.001
print(b, "относиться к типу", type(b))


c = 1+2j
print(c, "комплексное число?", isinstance(c, complex))


print(6+2) # 8
print(6-2) # 4
print(6*2) # 12
print(6/2) # 3.0


print(7/2) # 3.5
print(7//2)
print(7%2)
print(6**2)

s = "Это строка"
print(s + "\n")
g = """ многострочная строка"""
print(g + "\n")
print("Строки" + "можно" + "складывать")