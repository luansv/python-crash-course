names = ['charles', 'mike', 'james']
print(names[0].title())
print(names[1].title())
print(names[2].title())

message = f'Welcome, {names[0].title()}'
print(message)

messageMike = f'Goodnight, {names[1].title()}'
print(messageMike)

messageJames = f'{names[2].title()} wont be able to come'
print(messageJames)

names[2] = 'malu'
print(f'New list: {names}')

print("More people arrived so it will be needed a new table..")
names.insert(0,'karl')
names.insert(2, 'james')
names.append('karla')

print(f'New list of people: {names}')

#3.7
print(f'New dinner table won’t arrive in time for the dinner, and you have space for only two guests.')
person1 = names.pop()
person2 = names.pop()
person3 = names.pop()
person4 = names.pop()
print(f'Sorry {person1.title()}, I can´t invite you anymore')
print(f'Sorry {person2.title()}, I can´t invite you anymore')
print(f'Sorry {person3.title()}, I can´t invite you anymore')
print(f'Sorry {person4.title()}, I can´t invite you anymore')
print(f'Hey {names[0].title()}, you are still invited!')
print(f'Hey {names[1].title()}, you are still invited!')
print(names)
del names[1]
del names[0]
print(f'Empty list: {names}')


#3.8
places = ['Italy', 'The netherlands', 'Thailand', 'Germany', 'Ireland']
print("Original list:")
print(places)

print("\nAlphabetical order (sorted):")
print(sorted(places))

print("\nStill in original order:")
print(places)

print("\nReverse alphabetical order (sorted):")
print(sorted(places, reverse=True))

print("\nStill in original order:")
print(places)

places.reverse()
print("\nReversed list:")
print(places)

places.reverse()
print("\nBack to original order:")
print(places)

places.sort()
print("\nAlphabetical order (sort):")
print(places)

places.sort(reverse=True)
print("\nReverse alphabetical order (sort):")
print(places)

print(f"\nList length: {len(places)}")






