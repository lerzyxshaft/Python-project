class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, 'age:', self.age, 'Happy:', self.isHappy)

cat1 = Cat()
cat1.set_data('barsik', 11, True)
print(cat1)

print('15 Nov')

