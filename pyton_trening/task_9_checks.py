class Checks():

    def __init__(self, loc):
        self.loc = loc
        self.get()
    def get(self):
        print(self.loc)


class Input(Checks):
    def __init__(self, loc, text):
        super(Input, self).__init__(loc)
        self.text = text


search = Input('http://ya.ru', 'текст')


class Button(Checks):
    def __init__(self, loc, text):
        super(Button, self).__init__(loc)
    #     self.loc = loc
        self.text = text
    #     self.get_info()
    #
    # def get_info(self):
    #     print(self.loc, self.text)

enter = Button('http://yandex.ru', 'яндекс')


class Title(Checks):
    def __init__(self, loc, text):
        super(Title, self).__init__(loc)
        # self.loc = loc
        self.text = text
        # self.get_info()

    # def get_info(self):
    #     print(self.loc, self.text)


page = Title('http://mail.ru', 'маил')


class Link(Checks):
    def __init__(self, loc, text):
        super(Link, self).__init__(loc)
        # self.loc = loc
        self.text = text
        # self.get_info()

    # def get_info(self):
    #     print(self.loc, self.text)

link = Link('http://google.com', 'гугл')
