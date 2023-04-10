import random
import time

customers = ['Jimmy', 'Kim', 'Stacie']
winner = random.choice(customers)
flavor = 'vanilla'

print('Congrations ' + winner + ', you have won an ice cream sundae!')

time.sleep(2)

prompt = 'would you like cherry on top? '

wants_cherry = input(prompt)
order = flavor + ' sundae'

if (wants_cherry == 'yes'):
    order = order + ' with a cherry on top'

time.sleep(1)
print('One ' + order + ' for ' + winner + ' coming right up...')