#9-7

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


class Admin(User):

    def __init__(self, first, name,country, cellphone):
        super().__init__(first, name, country, cellphone)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges1(self):
        print('Admin´s set of privileges: ')
        for privilege in self.privileges:
            print(f'- {privilege}')

admin1 = Admin('James', 'Lopes', 'Mexico', '999999')
admin1.show_privileges1()

#9-8

class Privileges(Admin):


    def __init__(self, first, name, country , cellphone ):
        super().__init__(first, name, country,cellphone)
        self.privileges = ["can add post", "can delete post", "can ban user"]


    def show_privileges2(self):
        print('Admin´s set of privileges: ')
        for privilege in self.privileges:
            print(f'- {privilege}')

admin1 = Admin('Sophia', 'Stone', 'UK', '999999')
admin1.show_privileges1()
