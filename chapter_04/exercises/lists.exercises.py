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
for value in range(3,31,3):
    three.append(value)

print(f'List of multiples of 3 from 3 to 30:{three}')

# 4.8
cubes = []
for i in range(1,11):
    cubes.append(i**3)

print(f'Cubes: {cubes}')

cubes = [i**3 for i in range(1,11)]
print(cubes)