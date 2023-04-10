import time

first = 'somewhere'
last = 'over the rainbow'

print(first, last)

time.sleep(2)

switch = [first, last]

print(switch)

time.sleep(2)

first = switch[1]
last = switch[0]

time.sleep(2)

print(first, last)