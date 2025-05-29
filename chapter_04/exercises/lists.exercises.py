# 4.1
from chapter_04.range import even_numbers

singers = ['Kelena', 'Arca', 'Chali']
for singer in singers:
    print(f'You are currently listening to: {singer.title()}')

print(f'You listened to {len(singers)} artists!')

# 4.3
numbers = list(range(1, 21))
print(numbers)

# 4.5
abc = list(range(1, 1000001))
print(min(abc))
print(max(abc))

# 4.6
even_numbers = list(range(1, 21, 2))
print(f'Even numbers: {even_numbers}')

# 4.7
three = []
for value in range(3, 31, 3):
    three.append(value)

print(f'List of multiples of 3 from 3 to 30:{three}')

# 4.8
cubes = []
for i in range(1, 11):
    cubes.append(i ** 3)

print(f'Cubes: {cubes}')

cubes = [i ** 3 for i in range(1, 11)]
print(cubes)

# 4.10
foods = ['pizza', 'falafel', 'carrot cake', 'orange', 'bread', 'rice']
print(f'The first three elements in this list are: {foods[:3]}')
print(f'The last three elements in this list are: {foods[-3:]}')

# 4.11
my_foods = foods[:]
foods.append(f'meat')
my_foods.append('ice cream')
print(f'Original list: {foods}')
print(f'Copied list: {my_foods}')

for my in my_foods[:]:
    print(f'My food: {my}')

# 4.23

menu = ('pizza', 'falafel', 'carrot cake') #to be a tuple it needs to have commas
print(f'tuple:')
for more in menu:
    print(more)

new_menu = ('cake', 'carrot', 'carrot cake') #to be a tuple it needs to have commas
print(f'New tuple')
for new in new_menu:
    print(new)