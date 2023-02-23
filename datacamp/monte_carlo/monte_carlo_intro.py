import random as random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Complete the function definition by defining the yearly_increase variable
def monte_carlo_inflation(year, seed):
    random.seed(seed)
    inflation_rate = 8.6
    yearly_increase = random.randint(1, 3) # stochastic increase 1% 2 % 3%
    for i in range(year - 2022):
        inflation_rate = inflation_rate*((100 + yearly_increase)/100)
    return(inflation_rate)
  
# Simulate the inflation rate for the year 2050 with a seed of 1234
print(monte_carlo_inflation(2050, 1234))

# Simulate the inflation rate for the year 2050 with a seed of 34228
print(monte_carlo_inflation(2050, 34228))

# Law of Large Numbers

# Calculate the average of 1,000 simulation results with a seed between 0 and 20000
rates_1 = []
for i in range(1000):
    seed = random.randint(0, 20000)
    rates_1.append(monte_carlo_inflation(2050, seed))
print(np.mean(rates_1))

# Calculate the average of 10,000 simulation results with a seed between 0 and 20000
rates_2 = []
for i in range(10000):
    seed = random.randint(0, 20000)
    rates_2.append(monte_carlo_inflation(2050, seed))
print(np.mean(rates_2))

# Sampling without replacement

def two_random_ne_states():
    ne_states=["Maine", "Vermont", "New Hampshire", "Massachusetts", "Connecticut", "Rhode Island"]
    return(random.sample(ne_states, 2))

print(two_random_ne_states())
print(two_random_ne_states())

# Sampling with replacement | Bootstrapping

nba_heights = [196, 191, 198, 216, 188, 211, 201, 188, 191, 201, 208, 191, 183, 196]

simu_heights = []

for i in range(1000):
    bootstrap_sample = random.choices(nba_heights, k=15)
    simu_heights.append(np.mean(bootstrap_sample))

upper = np.quantile(simu_heights, 0.975)
lower = np.quantile(simu_heights, 0.025)

print([np.mean(simu_heights), lower, upper])

# plotting 
sns.displot(simu_heights)
plt.axvline(lower, color="red")
plt.axvline(upper, color="red")
plt.axvline(np.mean(simu_heights), color="green")
plt.show()

# permutation

us_heights = [165, 185, 179, 187, 193, 180, 178, 179, 171, 176, 169, 160, 140, 199, 176, 185, 175, 196, 190, 176]
nba_heights = [196, 191, 198, 216, 188, 185, 211, 201, 188, 191, 201, 208, 191, 183, 196]

all_heights = us_heights + nba_heights 

simu_diff = []

for i in range(1000):
    perm_sample = np.random.permutation(all_heights)
    perm_nba, perm_adult = perm_sample[0:15], perm_sample[15:35]
    perm_diff = np.mean(perm_nba) - np.mean(perm_adult)
    simu_diff.append(perm_diff)

# 95% confidence interval for permutation of two random lists:

upper1 = np.quantile(simu_diff, 0.975)
lower1 = np.quantile(simu_diff, 0.025)
mean_heights = np.mean(nba_heights) - np.mean(us_heights)

print([lower1, upper1])

# checking if "difference" is a random result ie., if its outside confidence interval

sns.displot(simu_diff)
plt.axvline(lower1, color="red")
plt.axvline(upper1, color="red")
plt.axvline(mean_heights, color="green")
plt.show()



#----------------------- Sampling w Replacement example--------------------

nba_weights = [96.7, 101.1, 97.9, 98.1, 98.1, 100.3, 101.0, 98.0, 97.4]

simu_weights = []

# Sample nine values from nba_weights with replacement 1000 times
for i in range(1000):
    bootstrap_sample = random.choices(nba_weights, k=9)
    simu_weights.append(np.mean(bootstrap_sample))

# Calculate the mean and 95% confidence interval of the mean for your results
mean_weight = np.mean(simu_weights)
upper = np.quantile(simu_weights, 0.975)
lower = np.quantile(simu_weights, 0.025)
print(mean_weight, lower, upper)

# Plot the distribution of the simulated weights
sns.displot(simu_weights)

# Plot vertical lines for the 95% confidence intervals and mean
plt.axvline(lower, color="red")
plt.axvline(upper, color="red")
plt.axvline(mean_weight, color="green")
plt.show()

#----------------------- Permutation Practice --------------------

# each list has 13 entries
nba_weights = [96.7, 101.1, 97.9, 98.1, 98.1, 100.3, 101.0, 98.0, 97.4, 100.5, 100.3, 100.2, 100.6]
us_adult_weights = [75.1, 100.1, 95.2, 81.0, 72.0, 63.5, 80.0, 97.1, 94.3, 80.3, 93.5, 85.8, 95.1]

# Define all_weights
all_weights = nba_weights + us_adult_weights
simu_diff = []

for i in range(1000):
	# Perform the permutation on all_weights
    perm_sample = np.random.permutation(all_weights)
    # Assign the permutated samples to perm_nba and perm_adult
    perm_nba, perm_adult = perm_sample[0:13], perm_sample[13:26]
    perm_diff = np.mean(perm_nba) - np.mean(perm_adult)
    simu_diff.append(perm_diff)

mean_diff = np.mean(nba_weights) - np.mean(us_adult_weights) 
upper = np.quantile(simu_diff, 0.975)
lower = np.quantile(simu_diff, 0.025)
print(mean_diff, lower, upper)

#----------------------- Leveraging Monte Carlo Simulation --------------------
#----------------------- Biased Dice Simulation --------------------

bag1 = [[1,2,3,6,6,6],[1,2,3,4,4,6],[1,2,3,3,3,5]]
bag2 = [[2,2,3,4,5,6],[3,3,3,4,4,5],[1,1,2,4,5,5]]

def roll_biased_dice(n, seed=1231):
    random.seed(seed)
    results = {}
    for i in range(n):
        bag_index1 = random.randint(0,2)
        die_index1 = random.randint(0,5)
        bag_index2 = random.randint(0,2)
        die_index2 = random.randint(0,5)
        point1 = bag1[bag_index1][die_index1]
        point2 = bag2[bag_index2][die_index2]
        key = "%x_%s" % (point1, point2)
        if point1 + point2 == 8:
            if key not in results:
                results[key] = 1
            else:
                results[key] += 1
    return(pd.DataFrame.from_dict({'dice1_dice2':results.keys(),
		'probability_of_success':np.array(list(results.values()))*100.0/n}))

print(roll_biased_dice(10000))

# Run the simulation 10,000 times and assign the result to df_results
df_results = roll_biased_dice(10000, seed=1231)
sns.barplot(x="dice1_dice2", y="probability_of_success", data=df_results)
plt.show()