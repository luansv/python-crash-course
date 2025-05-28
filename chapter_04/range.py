for value in range(0, 5):
    print(value)

print("-------------------")

numbers = list(range(11))
print(numbers)

print("-------------------")

even_numbers = list(range(2, 11, 2))
print(f'Even numbers:{even_numbers}')

print("-------------------")

squares = []
for value in range(1,11): #exponent
    squares.append(value **2)

print(f'Squares: {squares}')

print("-------------------")

squares = [value**2 for value in range(1, 11)]
print(squares)

