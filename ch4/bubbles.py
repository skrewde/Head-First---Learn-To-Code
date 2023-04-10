# The list of scores for different bubble formulas

scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .25, .33, .31, .25, .29, .27, .22, .31, .25, .25, .33, .21, .25, .25, .25, .28, .25, .24, .22, .20, .25, .30, .25, .24, .25, .25, .25, .27, .25, .26, .29]

# Initialising the i and length variables to loop over
i = 0
length = len(scores)
high_score = 0

# *While* the 'while' loop can to tweaked to iterate over sequences [like lists], that isnt convention.
    # The 'for' loop is much suited *for* such tasks, *while* the former is better for looping Boolean conditions.
    # So I'll be replacing the original 'while' loop with a much cleaner 'for' loop.
        # while i < length:
        #     print('Bubble solution #'+str(i) ,'score:',scores[i])
        #     i = i + 1

# Loop for printing all the bubble solutions' scores
for i in range(length):
    print('Bubble solution #'+str(i) ,'score:',scores[i])
    if scores[i] > high_score:
        high_score = scores[i]

print('Bubbles tests:', length)
print('Highest bubble score:', high_score )

# Initialising a variable to hold a list of the best bubble solutions
best_solutions = []

# Loop for finding the best solutions and appending them to the empty list
for i in range(length):
    if scores[i] == high_score:
        best_solutions.append(i)

print('Solutions with the highest score:', best_solutions)

# Finding the most cost effective bubble solution
most_effective = 0
cost = 100.0

# Old loop for finding the most cost effective bubble solution. Discarded for efficiency reasons.
    # Loop for finding the most cost effective bubble solution
    # for i in range(length):
    #     if scores[i] == high_score and costs[i] < cost:
    #         most_effective = i
    #         cost = costs[i]

    # print(cost)
    # print(most_effective)

# Loop for finding the most cost effective bubble solution
for i in range(len(best_solutions)):
    index = best_solutions[i]
    if cost > costs[index]:
        most_effective = index
        cost = costs[index]

print('Solution', most_effective, 'is the most effective with a cost of', costs[most_effective])