class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, n, a, i):
        self.name = n
        self.age = a
        self.isHappy = i

cat1 = Cat() # создали объект кот
cat1.set_data('Барсиу', 3, True)