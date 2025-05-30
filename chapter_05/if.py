cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'subaru':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovi!")


banned_users = ['andrew', 'carolina', 'david']
user = 'aa'

if user not in banned_users:
    print(f'{user.title()} ')