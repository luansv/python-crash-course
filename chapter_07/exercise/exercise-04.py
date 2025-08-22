#7-10
from operator import truediv

dream = {}

active = True

while active:
    name = input("\n Whats your name?")
    place = input("If you could visit one place in the world, where would you go? ")

    dream[name] = place

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        active = False


print("Results:")
for name, places in dream.items():
    print(f'{name.title()} would like to visit {places.title()}')

print("---------------------------------")


