from name import message

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(f'You have choose:', bicycles[0].title())
print(f'The last element:',bicycles[-1].title())

message = f'Your first bicycle was: {bicycles[0].title()}'
print(message)

print("----------")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Replace the first element
motorcycles[0] = 'abcd'
print(motorcycles)

#Add a new element at the end of the list
motorcycles.append('ducati')
print(motorcycles)

#Add a new element in a specific place on the list
motorcycles.insert(0, 'arca')
print(motorcycles)

#Removing
del motorcycles[0]
print(motorcycles)

#Remove the last element of a stack (pop)
popped = motorcycles.pop()
print(motorcycles)
print(f'Popped element:',popped)
print(f'The last motorcycle i owned was a {popped}')
first = motorcycles.pop(0)
print(f'The first motorcycle i owned was a {first}')
print(motorcycles) #abcd is not located in the list anymore because was used a pop which remove the element

#Using 'remove'
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)