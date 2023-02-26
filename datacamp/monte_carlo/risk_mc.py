import random 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Liquidity Risk due to High Insolvencies as % of Available Liquidity 
# Probability of Loss over 1 year: 9% or 0.09
def insolvency_occurs(probability):
    return np.random.rand() < probability


# 90% CI of Impact: lower: $12,500, upper: $50,000
# not equally likely
# more likely loss skews to lower-end, huge losses happen less frequently
# lognormal distribution is ideal for representing the probabilities associated with each possible loss amount

# The probability density function for the log-normal distribution is:
# < insert equation >

# The formula to derive the mean and standard deviation from upper and lower estimates is:
# < insert equation > ...where 2.0 and 3.29 are used

# For standard deviation, we divide by 3.29, as 90% of values fall within 3.29 std dev of mean of normal distribution
# Take natural log of upper and lower bounds to get std dev for log-normal distribution 

# note: the total area under the curve for any probability distribution must add up to 1

# using Python Numpy, get simulated loss amount from log-normal distribution

def insolvency_loss_amount(lower, upper):
    mean = (np.log(lower) + np.log(upper))/2.0
    std_dv = (np.log(upper) - np.log(lower))/3.29 

    return np.random.lognormal(mean, std_dv)

# The above two functions allow us to simulate Liquidity Risk due to Insolvencies 



# let's simulateda year of operation simulated 20 times---then 1000 times

# Probability of Loss over 1 year: 9% or 0.09
# 90% CI of Impact: lower: $12,500, upper: $50,000

i = 0
while i < 20:
    if insolvency_occurs(0.09):
        loss_due_to_insolvencies = insolvency_loss_amount(12500, 50000)
        print('Loss due to insolvencies was ${:,.2f}'.format(loss_due_to_insolvencies))
    else:
        print('A loss due to insolvency did not occur.')
    i += 1


"""

def simulate_scenario(events):
    total_loss = 0
    for _, event in events.iterrows():
        if insolvency_occurs(event['Probability']):
            total_loss += insolvency_loss_amount(event['Lower'], event['Upper'])
    return total_loss

def monte_carlo(events, rounds):
    list_losses = []
    for i in range(rounds):
        loss_result = simulate_scenario(events)
        list_losses.append(loss_result)
    return list_losses

# Visualize 1000 monte carlo simulation results
results = monte_carlo(events, 1000)
results_series = pd.Series(results)
results_series.plot()

"""

# Building a Liquidity Risk Portfolio 

liquidity_risk_data = {
    "Risk": ['Liquidity_Risk_Depositors', 'Liquidity_Risk_Borrowers', 'Insolvencies', 'Liquidations'],
    "Probability": [0.03, 0.02, 0.09, 0.20],
    "Lower": [12500, 12500, 12500, 12500],
    "Upper": [50000, 50000, 50000, 50000]
}

liquidity_risk_df = pd.DataFrame(liquidity_risk_data)
print(liquidity_risk_df)

def simulate_risk_portfolio(liquidity_risk_df):
    total_loss_amount = 0
    for risk in liquidity_risk_df.itertuples():
        if insolvency_occurs(risk.Probability):
            total_loss_amount += insolvency_loss_amount(risk.Lower, risk.Upper)
    return total_loss_amount

def monte_carlo_simulation(liquidity_risk_df, iterations):
    yearly_losses = []
    for i in range(iterations):
        loss_amount = simulate_risk_portfolio(liquidity_risk_df)
        yearly_losses.append(loss_amount)
    return yearly_losses

yearly_losses = monte_carlo_simulation(liquidity_risk_df, iterations = 10000)

print(yearly_losses)

results_series = pd.Series(yearly_losses)
results_series.plot()
plt.show()

results_series.hist(bins = 15)
plt.show()


results_nparray = np.array(results_series)
hist, edges = np.histogram(results_nparray, bins = 40)
cumrev = np.cumsum(hist[::-1])[::-1]*100/len(results_nparray)
plt.plot(edges[:-1], cumrev)
plt.show()