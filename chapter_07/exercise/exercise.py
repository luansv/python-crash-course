
#7.1
message = input("What do you want to listen to? ")
print(f'Okay, let´s play some {message}')

print("--------------------")

#7.2
people_count = int(input("How many people are in your dinner group? "))

if people_count > 8:
    print("You´ll have to wait")
else:
    print('Your table is ready')

print("--------------------")

#7.3
number = int(input("Enter a  number: "))

if number % 10 == 0:
    print(f'{number} is multiple of 10')
else:
    print(f'{number} is NOT multiple of 10')

print("--------------------")
