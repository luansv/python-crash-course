#9-3/9-4

class User:
    def __init__(self, first, last, country, cellphone):
        self.first = first
        self.last = last
        self.country = country
        self.cellphone = cellphone
        self.number_served = 0
        self.login_attempts = 0

    def describe_user(self):
        print(f'First name: {self.first}')
        print(f'Last name: {self.last}')
        print(f'Country: {self.country}')
        print(f'Cellphone: {self.cellphone}')
        print(f'Number served: {self.number_served}')

    def greet(self):
        full_name = f'{self.first} {self.last}'
        print(f'Hey {full_name}')

    def set_number_served(self, numb):
        self.number_served = numb
        print(f'Number served: {self.number_served}')

    def increment_number_served(self, increment):
        self.number_served += increment
        print(f'Number served increment: {self.number_served}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def print_login_attempts(self):
        print(f'Login attempts: {self.login_attempts}')


user1 = User('James', 'Adam','Iceland', '9999999' )
user2 = User('Jenni', 'Peter','Norway', '1888880' )

user1.describe_user()
user2.greet()


user1.set_number_served(8)
user1.set_number_served(9)

print('----------------------')

user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()

for _ in range (100):
    user2.increment_login_attempts()

user2.print_login_attempts()

user2.reset_login_attempts()
user2.print_login_attempts()




