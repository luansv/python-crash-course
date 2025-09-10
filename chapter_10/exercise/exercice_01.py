#10-1
filename = 'learning_python'


with open(filename) as f:
    contents = f.read()
print('-----------------')

with open(filename) as f:
    for line in f:
        print(line.rstrip())

print('-----------------')

lines = []
with open(filename) as f:
    lines = f.readline()

for line in lines:
    print(line)

#10-2

message = "I really like python."
new_message = message.replace('python', 'java')
print(new_message)