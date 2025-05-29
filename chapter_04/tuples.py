#Tuples creates a list of items that cannot change

dimensions = (200, 50)
# dimensions[0] = 250 it cannot be changed
print(dimensions[0])
print(dimensions[1])

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 500)
print("Changed dimensions:")
for dimension in dimensions:
    print(dimension)
