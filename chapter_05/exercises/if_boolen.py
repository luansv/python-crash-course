# 5.1

artist = 'Bjork'
print("Is artist == 'Bjork'? I predict True.")
print(artist == 'subaru')

print("\nIs artist == 'Kai'? I predict False.")
print(artist == 'audi')

# 5.2

string1 = 'one'
string2 = 'two'
if string1 == string2:
    print('The strings are equal')
else:
    print('The strings are not equal')

food1 = 'Rice'
food2 = 'rice'
if food1.lower() == food2.lower():
    print('The foods are the same')
else:
    print('The foods are not the same')

# 5.3

alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print(f'Alien is green!')

if 'red' in alien_color:
    print(f'Alien is not red!')

# 5.4

if 'green' in alien_color:
    print('You just earned 5 points!')
elif 'yellow' in alien_color:
    print('You just earned 10 points!')
elif 'red' in alien_color:
    print('You just earned 15 points!')

print('----------------------')
# 5.9
usernames = ['admin', 'julia123', 'caio123', 'james123', 'sofia123']
for username in usernames:
    if not usernames:
        print(f'The list is empty!')

    elif username.lower() == 'admin':
        print(f'Hello admin, would you like to see a status report?')

    else:
        print(f'Hello {username}, thank you for logging in again.')

print('----------------------')
# 5.10

current_users = ['Bjork', 'Miley', 'Arca', 'Admin', 'James']

new_users = ['Bjork', 'Ashley', 'Jannet', 'Miley']

current_user_lower = [user.lower() for user in current_users]

for new in new_users:
    if new.lower() in current_user_lower:
        print(f'The username {new} is not available')
    else:
        print(f'The username {new} is available!')

print('----------------------')
# 5.11

numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")


