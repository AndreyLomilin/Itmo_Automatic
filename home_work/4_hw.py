# class Rec():
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#         self.square()
#         self.perimetr()
#     def s(self):
#         return self.width * self.length
#
#
#     def p(self):
#         return ((self.width + self.length) * 2)
#
#
#     def square(self):
#         print('Площадь: ', self.s() )
#
#
#     def perimetr(self):
#         print('Периметр: ', self.p())
#
#
# rec1 = Rec(2, 4)
# rec2 = Rec(3, 6)
# rec3 = Rec(5, 7)
#
#
#
#
class Math():
    def addition(self, a, b):
        print("{} + {} = {}".format(a, b, a + b))

    def subtraction(self, a, b):
        print("{} - {} = {}".format(a, b, a - b))

    def multiplication(self, a, b):
        print("{} * {} = {}".format(a, b, a * b))

    def division(self, a, b):
        print("{} / {} = {}".format(a, b, a / b))

Math().addition(3, 5)
Math().subtraction(2,3)
Math().multiplication(2,3)
Math().division(2,3)


class LeftMenu():
    def __init__(self, text, tupe='Кнопка', loc=''):
        self.text_box = text
        self.tupe = tupe
        self.loc = loc
        self.get()
        self.print()
    def click(self):
        return 'Клик по кнопке - {}'.format(self.text_box)


    def get(self):
        print('текст кнопки: ', self.text_box)

    def print(self):
        print(self.click())




text_box = LeftMenu('Text Box')
chek_box = LeftMenu('Chek Box')
radio_button = LeftMenu('Radio Button')
web_tables = LeftMenu('Web Tables')
buttons = LeftMenu('Buttons')
links = LeftMenu('Linrs')
broker_loinrs = LeftMenu('Broker Links-Images')
up_and_down = LeftMenu('Upload and Download')
dynamic_properties = LeftMenu('Dynamic Properties')
