# 6.1
person = {
    'first_name': 'james', 'last_name': 'brooks', 'age': 19, 'city': 'toronto',
    'first_name': 'carla', 'last_name': 'brooks', 'age': 19, 'city': 'toronto'}

print("First name:", person["first_name"].title())
print("Last name:", person["last_name"].title())
print("Age:", person["age"])
print("City:", person["city"].title())

# 6.2
print("------------")
favorite_numbers = {
    "Alice": 7,
    "Bob": 42,
    "Charlie": 12,
    "Diana": 99,
    "Ethan": 23
}

for name, number in favorite_numbers.items():
    print(f'{name} favorite number is: {number}')

# 6.3
print("------------")

glossary = {
    "Variable": "A named location used to store data in memory.",
    "Function": "A block of organized, reusable code that performs a specific task.",
    "Loop": "A control flow statement used to repeat a block of code multiple times.",
    "List": "A collection of ordered items that can be changed (mutable).",
    "Dictionary": "A collection of key-value pairs, used to store data with a relationship between elements."
}

for word, meaning in glossary.items():
    print(f"{word}:\n  {meaning}\n")


person = {'first': 'luan', 'last': 'silva', 'city': 'princesa', 'age': 10}
print(f'Name: {person['first']}')
print(f'City: {person['city']}')

fav_numb = {
    'Alice': 2,
    'Babe': 3,
    'Sofia': 5
}

for person, number in fav_numb.items():
    print(f'O numero fav de {person} é {number}')



abcd = {
    'Love': 'Amor',
    'Hi': 'Olá',
    'Bonjour': 'Olá'
}

for name1, name2 in abcd.items():
    print(f'A tradução de {name1}:\n {name2}')

for name in abcd.keys():
    print(f'Keys: {name}')

for translation in abcd.values():
    print(f'Values: {translation}')

#6-5

artists = {
    'Charli': 'Brat',
    'Arca': "Kick",
    'Loona': 'Yves'
}

for name, album in artists.items():
    print(f'{name} released {album}')

for name in artists.keys():
    print(f'Artists: {name}')

for album in artists.values():
    print(f'Albums: {album}')

#6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

poll_takers = ['jen', 'sarah', 'mike', 'david', 'phil', 'emma']

for person in poll_takers:
    if person in favorite_languages:
        print(f'Thanks {person.title()}, for responding')
    else:
        print(f"{person.title()}, please consider taking our favorite languages poll!")


print("---------------------------------")

#6-7

person1 = {'first_name': 'james', 'last_name': 'brooks', 'age': 19, 'city': 'toronto'}
person2= {'first_name': 'carla', 'last_name': 'brooks', 'age': 19, 'city': 'toronto'}

people = [person1, person2]

for person in people:
    print(f"F name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")

print("---------------------------------")

#6-8
pet_1 = {
    'kind': 'dog',
    'owner': 'Alice'
}

pet_2 = {
    'kind': 'cat',
    'owner': 'Bob'
}

pet_3 = {
    'kind': 'parrot',
    'owner': 'Clara'
}

pet_4 = {
    'kind': 'turtle',
    'owner': 'David'
}

animals = [pet_1, pet_2, pet_3, pet_4]

for pet in animals:
    print(f"Kind of animal: {pet['kind']}")
    print(f"Owner's name: {pet['owner']}")
    print("-" * 20)

print("---------------------------------")

#6-9

favorite_places = {
    'Alice': ['Paris', 'Tokyo', 'New York'],
    'Bob': ['London', 'Rome'],
    'Clara': ['Sydney']
}

for person, places in favorite_places.items():
    print(f'{person} favorite places are: ')
    for place in places:
        print(f"- {place}")
    print()

print("---------------------------------")

#6-10
cities = {
    'Paris': {
        'country': 'France',
        'population': '2.1 million',
        'fact': 'Home to the Eiffel Tower and famous for its art and cuisine.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '14 million',
        'fact': 'Known for its cherry blossoms and bustling Shibuya Crossing.'
    },
    'Rio de Janeiro': {
        'country': 'Brazil',
        'population': '6.7 million',
        'fact': 'Famous for its Carnival festival and the Christ the Redeemer statue.'
    }
}

for city, infos in cities.items():
    print(f'City: {city}')
    for key, value in infos.items():
        print(f"{key}: {value}")

    print()

