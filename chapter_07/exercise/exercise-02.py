#7.4

toppings = []

while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")

    if topping.lower() == 'quit':
        print('Finished adding!')
        break
    else:
        toppings.append(topping)
        print(f"I'll add {topping} to your pizza.")

print(f"These are your topping:")
for t in toppings:
    print(f"- {t}")

#7.5

while True:
    age_input = input("Enter your age (or type 'quit' to stop): ")

    if age_input.lower() == 'quit':
        print("Exiting the program. Enjoy your movie!")
        break

    # Convert input to integer
    age = int(age_input)

    # Determine ticket price based on age
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15

    print(f"Your movie ticket will cost ${price}.")
