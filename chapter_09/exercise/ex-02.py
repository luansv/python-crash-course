#9-3

class User:
    def __init__(self, first, last, country, cellphone):
        self.first = first
        self.last = last
        self.country = country
        self.cellphone = cellphone

    def describe_user(self):
        print(f'First name: {self.first}')
        print(f'Last name: {self.last}')
        print(f'Country: {self.country}')
        print(f'Cellphone: {self.cellphone}')

    def greet(self):
        full_name = (f'{self.first} {self.last}')
        print(f'Hey {full_name}')

user1 = User('James', 'Adam','Iceland', '9999999' )
user2 = User('Jenni', 'Peter','Norway', '1888880' )

user1.describe_user()
user2.greet()