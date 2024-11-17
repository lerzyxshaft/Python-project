class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name = None, age = None, isHappy = None):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

cat1 = Cat('Barsik', 3, True)
cat2 = Cat('Babos', 4, True)
print("17Nov")

class Building:
    __year = None
    __city = None
    def __init__(self, year, city):
        self.year = year
        self. city = city

    def get_info(self):
        print('Year', self.year, 'City', self.city)

class School(Building):
    pupils = 0

    def __init__(self, pupils, years, city):
        super(School, self).__init__(year, city )
        self.pupils = pupils

    def get_info(self):
        super().get_info()
        print("Pupils: ", self.pupils)
class House(Building):
    pass

class Shop(Building):
    pass

school = School(100, 2000, 'Kyiv')
school.get_info()
house = House(2010, 'Kyiv')
shop =Shop(2000, "Kiyv")
shop.get_info()