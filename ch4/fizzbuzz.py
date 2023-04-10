#Fizzbuzz. For the heck of it.

i = 0

for i in range(1, 100):
    if i%3 == 0 and i%5 == 0:
        print('fizzbuzz')
    elif i%5 == 0:
        print('buzz')
    elif i%3 == 0:
        print('fizz')
    else:
        print('#'+str(i))