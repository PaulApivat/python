import matplotlib.pyplot as plt 
import random 

def roll_dice():
    """
    Randomize an integer from 1 to 6 for both dice (simulating a roll)
    Compare two dice
    Return a Boolean
    """
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)

    # determine if numbers are same
    if die_1 == die_2:
        same_num = True
    else:
        same_num = False
    return same_num

"""
Number of rolls per game is 1000
player bets $1 on each roll
Track: win probability (wins per game / total number of rolls)
Ending balance
"""

# Inputs
num_simulations = 10000
max_num_rolls = 1000
bet = 1

# Tracking
win_probability = []
end_balance = []

# Setting up FIgure Plot
fig = plt.figure()
plt.title("Monte Carlo Dice Game [" + str(num_simulations) + "simulations]")
plt.xlabel("Roll Number")
plt.ylabel("Balance [$]")
plt.xlim([0, max_num_rolls])

"""
Outer for loop: iterates through number of simulations: 10000
Nested While loop: runs each game: 1000 rolls
"""

# For loop to run number of simulations 

for i in range(num_simulations):
    balance = [1000]
    num_rolls = [0]
    num_wins = 0

    # Run until the player has rolled 1,000 times 
    while num_rolls[-1] < max_num_rolls:
        same = roll_dice()

        # Result if the dice are the same number 
        if same:
            balance.append(balance[-1] + 4 * bet)
            num_wins += 1 
        # Result if the dice are different numbers 
        else:
            balance.append(balance[-1] - bet)

        num_rolls.append(num_rolls[-1] + 1)

# Store tracking variables and add line to figure 
    win_probability.append(num_wins/num_rolls[-1])
    end_balance.append(balance[-1])
    plt.plot(num_rolls, balance)

"""
Obtaining Results
"""

plt.show()

# Averaging win probability and end balance
overall_win_probability = sum(win_probability)/len(win_probability)
overall_end_balance = sum(end_balance)/len(end_balance)

# Displaying the averages 
print("Average win probability after " + str(num_simulations) + " runs: " + str(overall_win_probability))
print("Average ending balance after " + str(num_simulations) + " runs: $" + str(overall_end_balance))

"""
source: https://towardsdatascience.com/how-to-create-a-monte-carlo-simulation-using-python-c24634a0978a
"""