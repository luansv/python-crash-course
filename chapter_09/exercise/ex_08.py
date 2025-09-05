#9-13
import random
from random import  randint, sample

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1 , self.sides))


die1 = Die(6)
die2 = Die(10)
die3 = Die(20)

for _ in range(10):
    die1.roll_die()

print("---------------")

for _ in range(10):
    die2.roll_die()

print("---------------")

for _ in range(10):
    die3.roll_die()

print("---------------")

#9-14
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winners = sample(my_list, 4)
print(f'Any ticket matching these four numbers or letters wins a prize: {winners}')

#9-15

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_ticket = random.sample(items, 4)

count = 0
draw= []

while draw != my_ticket:
    draw = random.sample(items, 4)
    count =+ 1

print(f"It took {count} tries to draw the winning ticket: {draw}")
