# import time

characters = ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c']
output = ''
length = len(characters)
i = 0
while (i < length):
 output = output + characters[i]
 i = i + 1
length = length * -1
i = -2

# print(length)
# print(i)
# time.sleep(3)

while (i >= length):
 output = output + characters[i]
 i = i - 1
print(output)