#9-6

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type ="Ice Cream"):
        super().__init__(name,cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Cookie Dough"]

    def display_flavors(self):
        print('Available ice cream flavors: ')
        for flavor in self.flavors:
            print(f'- {flavor}')

ice_cream_shop = IceCreamStand("Cool Cones")
ice_cream_shop.describe_restaurant()
ice_cream_shop.display_flavors()

