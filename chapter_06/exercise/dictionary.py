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