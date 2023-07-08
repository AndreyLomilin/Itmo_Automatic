# class Button:
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link
#
# home = Button('Домой', '/home')
# catalog_msk = Button('Каталог', '/msk/catalog')
# print(home.text)
# print('Кнопка', + home.text + 'имеет ссылку' + home.link)
#
# print('\n')
#
# print(catalog_msk.ink)
# print('Кнопка' catalog_msk 'имеет ссылку' catalog_msk.link)

class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def clicks(self):
        return 'Клик по локатору, - {}'.format(self.loc)

home_two = ButtonTwo('домой', '/home', 'button#home')

print(home_two.clicks())
