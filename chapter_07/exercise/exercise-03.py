#7.8
sandwich_orders = ["tuna", "chicken", "veggie", "ham and cheese", "grilled cheese"]

finished_sandwiches = []

# Deli runs out of pastrami
print("Sorry, the deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # take the first order
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("All sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")

print("---------------------------------")


