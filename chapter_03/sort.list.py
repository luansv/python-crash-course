from operator import truediv

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(f'Sorted cars reversed:', cars)

print(f'Original list: \n{cars}')
print(f'Sorted list temporality: \n{sorted(cars)}')
print(f'Original list again: \n{cars}')
print(f'List´s length: {len(cars)} ')
print(f'Original unsorted list reversed: {cars.reverse()}')
