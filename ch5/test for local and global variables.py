greeting = 'Greetings'


def greet(name, message):
    global greeting
    greeting = 'Hi'
    # greeting = 'Hello'
    print(greeting, name + '.', message)

greet('June', 'See you soon!')
print(greeting)