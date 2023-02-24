# Required imports
import random 
import scipy.stats as st
import seaborn as sns
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


# Estimating the value of PI using monte carlo

"""
Area circle = Pi
Area square = 2 x 2 = 4
Area circle / Area square = Pi / 4

circle_points / square_points = Pi / 4

Pi = 4 * (circle_points/square_points)
"""



# sample 4 million times 
n = 4000000
circle_points = 0
square_points = 0

for i in range(n):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    dist_from_origin = x**2 + y**2
    if dist_from_origin <= 1:
        circle_points += 1
    square_points += 1

pi = 4 * circle_points / square_points

print(pi)

#-------------------------- Generating Discrete Random Variables 

# Picking the correct probability distribution 

# sampling from discrete ----------Uniform Distribution 
low = 3
high = 21 
samples = st.randint.rvs(low, high, size=1000) #rvs = random variable sampling
samples_dict = {"nums": samples}
sns.histplot(x="nums", data=samples_dict, bins=6, binwidth=0.3)
plt.show()

# sampling from ---------Geometric Distribution
p = 0.2
samples = st.geom.rvs(p, size=1000)  # geom.rvs = geometric random variable sampling
samples_dict = {"nums": samples}
sns.histplot(x="nums", data=samples_dict)
plt.show()

# sampling from discrete -------Uniform Distribution

# Define low and high for use in rvs sampling below
low = 1
high = 7  # for 1-6, 7 non-inclusive
# Sample 1,000 times from the discrete uniform distribution
samples = st.randint.rvs(low, high, size=1000)

samples_dict = {'nums':samples}
sns.histplot(x='nums', data=samples_dict, bins=6, binwidth=0.3)
plt.show()


# sampling from ------Geometric distribution

# Set p to the appropriate probability of success
p = 0.2

# Sample from the geometric distribution 10,000 times
samples = st.geom.rvs(p, size=10000)
samples_dict = {"nums":samples}
sns.histplot(x="nums", data=samples_dict)  
plt.show()

# Betting the difference between TWO Probability Distributions ---- Uniform Discrete vs Geometric

"""
Tom to score less than Eva when p has a value of 0.1 or 0.2. 
He is expected to score more when p is 0.3 and above!
"""

for p in [0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9]: 
    low = 1
    high = 7
	# Simulate rolling Tom's die 10,000 times
    die_samples = st.randint.rvs(low, high, size=10000)
	# Simulate Eva's coin flips to land heads 10,000 times
    coin_samples = st.geom.rvs(p, size=10000)
    diff = np.mean(die_samples - coin_samples)
    print(diff)


#-------------------------- Generating Continuous Random Variables 

# Sampling from Normal Distribution -----

heights = st.norm.rvs(loc=177, scale=8, size=10000)  # random variable sampling
qualified = (heights < 165) | (heights > 190)

print(np.sum(qualified) * 100/10000)

heights_dict = {"heights": heights}
sns.histplot(x="heights", data=heights_dict)
plt.axvline(x=165, color="red")
plt.axvline(x=190, color="red")
plt.show()


# ---------Changing the MEAN of normal distributions 
random.seed(1222)

# Sample 1,000 times from the normal distribution where the mean is 177
heights_177_8 = st.norm.rvs(loc=177, scale=8, size=1000)
print(np.mean(heights_177_8))
upper = np.quantile(heights_177_8, 0.975)
lower = np.quantile(heights_177_8, 0.025)
print([lower, upper])

# Sample 1,000 times from the normal distribution where the mean is 185
heights_185_8 = st.norm.rvs(loc=185, scale=8, size=1000)
print(np.mean(heights_185_8))
upper = np.quantile(heights_185_8, 0.975)
lower = np.quantile(heights_185_8, 0.025)
print([lower, upper])

# ---------Change the Standard Deviation of normal distributions 
random.seed(1231)

heights_177_8 = st.norm.rvs(loc=177, scale=8, size=1000)
print(np.mean(heights_177_8))
upper = np.quantile(heights_177_8, 0.975)
lower = np.quantile(heights_177_8, 0.025)
print([lower, upper])

# Sample 1,000 times from the normal distribution where the standard deviation is 15
heights_177_15 = st.norm.rvs(loc=177, scale=15, size=1000)
print(np.mean(heights_177_15))
upper = np.quantile(heights_177_15, 0.975)
lower = np.quantile(heights_177_15, 0.025)
print([lower, upper])

#----------------Two Independent Normal Distributions
# Simulate TWO income steams to find 95% confidence interval for the TOTAL income from BOTH jobs.

# Sample from the normal distribution
income1 = st.norm.rvs(loc=500, scale=50, size=1000)
income2 = st.norm.rvs(loc=1000, scale=200, size=1000)

# Define total_income
total_income = income1 + income2
upper = np.quantile(total_income, 0.975)
lower = np.quantile(total_income, 0.025)
print([lower, upper])


#-------------------------- Generating Multivariate Random Variables 

# Sampling from Multinomial Distributions ---------

# two biased coins, one with 20% chance heads, one with 80% chance heads
# 500 people flipping the coin 50 times

results = st.multinomial.rvs(50, [0.2, 0.8], size=500)

df_results = pd.DataFrame(
    {"Head": results[:, 0],
     "Tail": results[:, 1]}
)
sns.pairplot(df_results)
plt.show()



# Sampling from Multivariate Normal Distributions -----------
# Price and Demand are sampled independently

results = st.multivariate_normal.rvs(mean=[2,6], size=500)

df_results=pd.DataFrame(
    {"Price": results[:,0],
     "Demand": results[:,1]}
)
sns.pairplot(df_results)
plt.show()

# COVARIANCE MATRIX -------
# Price and Demand are negatively correlated

cov_mat = np.array([[1, -0.9], [-0.9, 1]])

results = st.multivariate_normal.rvs(
    mean=[2,6], size=500, cov=cov_mat
)

df_results = pd.DataFrame(
    {"Price": results[:,0],
    "Demand": results[:,1]}
)

sns.pairplot(df_results)
plt.show()

# Exercise: Multinomial Sampling ----------------------------
p_sunny = 300/365
p_cloudy = 35/365
p_rainy = 30/365
num_of_days_in_a_year = 365
number_of_years = 50

# Simulate results
days = st.multinomial.rvs(num_of_days_in_a_year,
    [p_sunny, p_cloudy, p_rainy], size=number_of_years)

# Complete the definition of df_days
df_days = pd.DataFrame({
     "sunny": days[:,0],
     "cloudy": days[:,1],
     "rainy":  days[:,2]})

sns.pairplot(df_days)
plt.show()

# Exercise: Multivariate Normal Sampling (w/ Covariance) ---------------------

mean_value = [20, 500]
sample_size_value = 5000
cov_mat = np.array([[19, 950], [950, 50000]])

# Simulate the results using sampling
simulated_results = st.multivariate_normal.rvs(mean=mean_value, size=sample_size_value, cov=cov_mat)
simulated_house_price_size = pd.DataFrame({"price":simulated_results[:,0],
                         				   "size":simulated_results[:,1]})

# Visualize the results 
sns.pairplot(simulated_house_price_size)
plt.show()

