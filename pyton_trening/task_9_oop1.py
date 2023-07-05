class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


search = Input('input#search', 'ljhlkj')


class Button:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text



class Title:
    def __init__(self, text, loc):
        self.loc = loc
        self.text = text
class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

print(search.loc)

