#8-12

def sandwiches(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

sandwiches("ham", "cheese")
sandwiches("turkey", "lettuce", "tomato")
sandwiches("chicken", "bacon", "avocado", "mayo")

print('------------------------')

#8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("albert", "einstein",
                             location="princeton",
                             field="physics")
print(user_profile)

print('------------------------')
#8-14
def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

# Example call
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
