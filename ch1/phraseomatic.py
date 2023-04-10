#Import the random module into our program
import random

#Create lists containing various instances of the different parts of speech
verbs = ['Leverage', 'Sync', 'Target', 'Gamify', 'Offline', 'Crowd-sourced', '24/7', 'Lean-in', '30,000 foot']
adjectives = ['A/B Tested', 'Freemium', 'Siloed', 'B-to-B', 'Oriented', 'Cloud-based', 'API-based']
nouns = ['Early Adopter', 'Low-hanging Fruit', 'Pipeline', 'Splash Page', 'Productivity', 'Process', 'Tipping Point', 'Paradigm']

#Using the random module,.choose one word from each list, and equate them to the following variables
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

#Gnerate a phrase by combining all the words chosen
phrase = verb + ' ' + adjective + ' ' + noun

#Print the phrase generated
print(phrase)