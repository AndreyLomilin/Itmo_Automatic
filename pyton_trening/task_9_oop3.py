class Soda:
    def __init__(self, m=''):
        self.m = m
    def show_my_drink(self):
        if self.m != '':
            print('Газировка и {self.m}')
        else:
            print('Обычная газировка')

drink1 = Soda()
drink2 = Soda('Малина')
drink1.show_my_drink()
drink2.show_my_drink()




