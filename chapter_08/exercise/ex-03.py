#8-9

text_messages = [
    "Hey, what time are we meeting?",
    "Sounds good! See you soon.",
    "Did you remember to grab the milk?",
    "Just finished the project, sending it now."
]

def show_message(messages):
    for message in messages:
        print(f"{message} \n")

show_message(text_messages)

print('----------------------')
#8-10

sent_messages = []
def send_messages(messages):
    while messages:
        current = messages.pop()
        print(f'Sending message: {current}')
        sent_messages.append(current)

send_messages(text_messages)
print('Original: ', text_messages) #Empty
print('Sent ones: ', sent_messages)

print('----------------------')
#8-11

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Hey, what time are we meeting?", "Sounds good! See you soon."]
sent_messages = []

send_messages(messages[:], sent_messages)

print("\nOriginal (no modify):", messages)
print("Sent ones (copy):", sent_messages)
