# WORK - INTRO PROGRAMMING
# AUTHOR: BRUNO BARBOSA
# REVISER: DIEGO PINHEIRO
# AIM: MONTE CARLO SIMULATION WITH TWO DICE


# MODULES --------------------------------------------------------------------------------------------------------------------------------------------
import random
import matplotlib.pyplot as plt


# MONTE CARLO SIMULATIONS ---------------------------------------------------------------------------------------------------------------------------
# Record the results of each advantage roll to calculate the frequency of each possible outcome
results = []
num_simulations = 100000

for i in range(num_simulations):
    die1 = random.randint(1, 20)
    
    # Determine the probability of rolling a 20 on the second die based on the result of the first die
    if die1 == 1:
        probability_of_twenty = 1
    else:
        probability_of_twenty = 1 / die1
    
    # Roll the second die
    rand_num = random.random()
    if rand_num < probability_of_twenty:
        die2 = 20
    else:
        die2 = random.randint(1, 19)
    
    # Store the higher of the two rolls 
    results.append(max(die1, die2))


# CALCULATION OF PROBABILITIES ----------------------------------------------------------------------------------------------------------------------
frequency = {}

# Count the frequency of each number in the results list
for num in results:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Print the frequency dictionary
print(frequency)

# Print the sorted frequency dictionary
myKeys = list(frequency.keys())
myKeys.sort()
sorted_frequency = {i: frequency[i] for i in myKeys} 
print(sorted_frequency)

# Calculate the probability of each outcome from 1 to 20 based on the frequency
for num in sorted_frequency:
    sorted_frequency[num] = (sorted_frequency[num]/num_simulations)*100

# Print the frequency dictionary, now with percentages
print(sorted_frequency)


# PLOT ----------------------------------------------------------------------------------------------------------------------------------------------
# Plot the results to visually inspect the distribution of outcomes 
plt.hist(results, bins=range(1, 22), density=True, align='left', rwidth=0.8)
plt.title('Probability Distribution of Dice Rolls')
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.xticks(range(1, 21))
plt.grid(axis='y', alpha=0.75)
plt.show()



# END OF SCRIPT -------------------------------------------------------------------------------------------------------------------------------------