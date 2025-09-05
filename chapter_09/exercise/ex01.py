

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        print(f"Restaurant Name: {self.name}")
        print(f"Cuisine Type: {self.cuisine}")

    def open(self):
        print(f"{self.name} is now open!")

restaurant = Restaurant('ABC', 'Korean')


print(restaurant.name)
print(restaurant.cuisine)

restaurant.describe()
restaurant.open()

print('------------------')
#9-2

restaurant1 = Restaurant("La Bella Vita", "Italian")
restaurant2 = Restaurant("Tokyo Delight", "Japanese")
restaurant3 = Restaurant("El Rancho", "Mexican")

restaurant1.describe()
restaurant2.describe()
restaurant3.describe()

print('------------------')
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
        full_name = self.first + self.last
        print(f'Hey {full_name}')

user1 = User('James', 'Adam','Iceland', '9999999' )
user2 = User('Jenni', 'Peter','Norway', '1888880' )

user1.describe_user()
user2.greet()