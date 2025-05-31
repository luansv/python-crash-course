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

# 5.7
person = 2
