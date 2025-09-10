filename1 = 'output-onlinefiletools.txt'

with open(filename1) as file_object:
    for line in file_object:
        print(f'{line[:30]}')

filename2 = 'python.text'

with open (filename2, 'w') as file_object2:
    file_object2.write('I love procrastinate')

with open(filename2, 'r') as file_object2:
    for line2 in file_object2:
        print(line2)
