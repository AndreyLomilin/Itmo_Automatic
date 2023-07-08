# class Page():
#     def __init__(self, text, url):
#         self.text = text
#         self.url = url
#         # self.get()
#
#     def get(self):
#         print('Сайт называтся: ', self.text, 'по адресу:', self.url)
#
#
# home_page = Page('Яндекс', 'http://ya.ru')
# home_page.get()


class NewPage():
    def __init__(self, url):
        self.url = url
    def visitor(self):
        return driver.get(self.url)

HomePage = NewPage('http://demoga.com')











