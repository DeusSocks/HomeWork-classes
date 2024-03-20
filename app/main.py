"""Реализуйте класс «Автомобиль». Необходимо хранить
в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
"""

class Auto():
    def __init__(self, model=None, year=None, fabric=None, volume=None, color=None, price=None) -> None:
        self.model = model
        self.year = year
        self.fabric = fabric
        self.volume = volume
        self.color = color
        self.price = price
    
    def create(self, model, year, fabric, volume, color, price):
        self.model = model
        self.year = int(year)
        self.fabric = fabric
        self.volume = int(volume)
        self.color = color
        self.price = int(price)
        
    def get_all(self):
        return self.model, self.year, self.fabric, self.volume, self.color, self.price
    
    def get(self, property:str):
        return eval(f"self.{property}")

"""Реализуйте класс «Книга». Необходимо хранить в
полях класса: название книги, год выпуска, издателя,
жанр, автора, цену. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса."""

class Book():
    def __init__(self, title=None, year=None, fabric=None, genre=None, author=None, price=None) -> None:
        self.title = title
        self.year = year
        self.fabric = fabric
        self.genre = genre
        self.author = author
        self.price = price
    
    def create(self, title, year, fabric, genre, author, price):
        self.title = title
        self.year = int(year)
        self.fabric = fabric
        self.genre = genre
        self.author = author
        self.price = int(price)

    def get_all(self):
        return self.title, self.year, self.fabric, self.genre, self.author, self.price
    
    def get(self, property:str):
        return eval(f"self.{property}")

"""Реализуйте класс «Стадион». Необходимо хранить в
полях класса: название стадиона, дату открытия, страну,
город, вместимость. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса."""

class Stadium():
    def __init__(self, title=None, year=None, country=None, town=None, capacity=None) -> None:
        self.title = title
        self.year = year
        self.country = country
        self.town = town
        self.capacity = capacity
    
    def create(self, title, year, country, town, capacity):
        self.title = title
        self.year = int(year)
        self.country = country
        self.town = town
        self.capacity = int(capacity)
    
    def get_all(self):
        return self.title, self.year, self.country, self.town, self.capacity
    
    def get(self, property:str):
        return eval(f"self.{property}")


def check():
    sample_auto = Auto()
    sample_auto.create(input("Model: "), input("Year of issue: "), input("Fabricator: "), input("Volume of engine: "), input("Color: "), input("Price: "))
    print(sample_auto.get_all())
    print(sample_auto.get('model'))
    
    sample_book = Book()
    sample_book.create(input("Book title: "), input("Year of writing: "), input("Fabricator: "), input("Genre: "), input("Author: "), input("Price: "))
    print(sample_book.get_all())
    print(sample_book.get('title'))
    
    sample_stadium = Stadium()
    sample_stadium.create(input("Stadium title: "), input("Year of opening: "), input("Country: "), input("Town: "), input("Capacity: "))
    print(sample_stadium.get_all())
    print(sample_stadium.get('title'))

#check() #Проверка работоспособности
