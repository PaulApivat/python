import numpy as np
import matplotlib.pyplot as plt


# Parameters
initial_price = 2500  # Initial ETH/USDC price (May 2025, based on context)
initial_value = 10000  # Initial LP position value in USDC
fee_tier = 0.0005  # 0.05% fee tier
base_volume = 1e6  # Base daily trading volume in USDC
volume_alpha = 5  # Volume sensitivity to price changes
range_width = 0.05  # Liquidity range width (±5%)
days = 90  # Simulation period

# Market parameters
trend_rate = 0.001  # 0.1% daily increase for trending market
trend_noise = 0.005  # Noise in trending market
choppy_volatility = 0.02  # 2% daily volatility for choppy market
choppy_drift = 0  # No net drift in choppy market

# Arbitrage parameters
arb_sigma = 0.005  # 0.5% price discrepancy volatility
arb_threshold = 0.003  # 0.3% threshold for arbitrage
arb_intensity = 0.1  # Arbitrage volume intensity
arb_adjustment = 0.5  # Price adjustment factor
gas_cost = 50  # Gas cost per rebalance in USDC

# Initialize arrays
np.random.seed(42)
time = np.arange(days)
prices_trending = np.zeros(days)
prices_choppy = np.zeros(days)
fees_trending = np.zeros(days)
fees_choppy = np.zeros(days)
il_trending = np.zeros(days)
il_choppy = np.zeros(days)
rebalance_costs_trending = np.zeros(days)
rebalance_costs_choppy = np.zeros(days)

# Initialize prices and ranges
prices_trending[0] = initial_price
prices_choppy[0] = initial_price
lower_bound_trending = initial_price / (1 + range_width)
upper_bound_trending = initial_price * (1 + range_width)
lower_bound_choppy = initial_price / (1 + range_width)
upper_bound_choppy = initial_price * (1 + range_width)

# Liquidity share (simplified: assume constant total liquidity)
your_liquidity = initial_value
total_liquidity = initial_value * 10  # 10x your liquidity
liquidity_share = your_liquidity / total_liquidity

# Track position value for IL calculation
value_trending = initial_value
value_choppy = initial_value
last_rebalance_price_trending = initial_price
last_rebalance_price_choppy = initial_price

# Simulate market conditions, fees, IL, and rebalancing
for t in range(1, days):
    # Trending market
    prices_trending[t] = prices_trending[t - 1] * (1 + trend_rate) + np.random.normal(
        0, trend_noise * prices_trending[t - 1]
    )

    # Choppy market (geometric Brownian motion)
    drift = (choppy_drift - 0.5 * choppy_volatility**2) * 1
    shock = choppy_volatility * np.sqrt(1) * np.random.normal(0, 1)
    prices_choppy[t] = prices_choppy[t - 1] * np.exp(drift + shock)

    # Arbitrage simulation (apply to both markets)
    for market, prices, lower_bound, upper_bound, last_rebalance_price in [
        (
            "trending",
            prices_trending,
            lower_bound_trending,
            upper_bound_trending,
            last_rebalance_price_trending,
        ),
        (
            "choppy",
            prices_choppy,
            lower_bound_choppy,
            upper_bound_choppy,
            last_rebalance_price_choppy,
        ),
    ]:
        # Simulate CEX price with discrepancy
        cex_price = prices[t] * (1 + np.random.normal(0, arb_sigma))
        price_diff = cex_price - prices[t]

        # Arbitrage trade if discrepancy exceeds threshold
        arb_volume = 0
        if abs(price_diff) > arb_threshold * prices[t]:
            arb_volume = arb_intensity * abs(price_diff) * base_volume
            # Adjust pool price toward CEX price
            prices[t] += arb_adjustment * price_diff

        # Trading volume (including arbitrage)
        price_change = abs(np.log(prices[t] / prices[t - 1])) if t > 0 else 0
        volume = base_volume * (1 + volume_alpha * price_change) + arb_volume

        # Fees (only earned if in range)
        in_range = lower_bound <= prices[t] <= upper_bound
        fees = fee_tier * volume * liquidity_share * in_range
        if market == "trending":
            fees_trending[t] = fees
            lower_bound_trending = lower_bound
            upper_bound_trending = upper_bound
            last_rebalance_price_trending = last_rebalance_price
        else:
            fees_choppy[t] = fees
            lower_bound_choppy = lower_bound
            upper_bound_choppy = upper_bound
            last_rebalance_price_choppy = last_rebalance_price

        # Rebalancing: adjust range if price moves out
        if not in_range:
            # Realize IL since last rebalance
            k = prices[t] / last_rebalance_price
            il = (
                value_trending * (2 * np.sqrt(k) / (1 + k) - 1)
                if market == "trending"
                else value_choppy * (2 * np.sqrt(k) / (1 + k) - 1)
            )
            # Update position value
            if market == "trending":
                value_trending -= il
                il_trending[t] = il
                rebalance_costs_trending[t] = gas_cost
                lower_bound_trending = prices[t] / (1 + range_width)
                upper_bound_trending = prices[t] * (1 + range_width)
                last_rebalance_price_trending = prices[t]
            else:
                value_choppy -= il
                il_choppy[t] = il
                rebalance_costs_choppy[t] = gas_cost
                lower_bound_choppy = prices[t] / (1 + range_width)
                upper_bound_choppy = prices[t] * (1 + range_width)
                last_rebalance_price_choppy = prices[t]
        else:
            # IL accumulates even without rebalancing
            k = prices[t] / last_rebalance_price
            il = (
                value_trending * (2 * np.sqrt(k) / (1 + k) - 1)
                if market == "trending"
                else value_choppy * (2 * np.sqrt(k) / (1 + k) - 1)
            )
            if market == "trending":
                il_trending[t] = il
            else:
                il_choppy[t] = il

# Cumulative metrics
cum_fees_trending = np.cumsum(fees_trending)
cum_fees_choppy = np.cumsum(fees_choppy)
cum_il_trending = np.cumsum(il_trending)
cum_il_choppy = np.cumsum(il_choppy)
cum_rebalance_costs_trending = np.cumsum(rebalance_costs_trending)
cum_rebalance_costs_choppy = np.cumsum(rebalance_costs_choppy)

# Profit
profit_trending = cum_fees_trending - cum_il_trending - cum_rebalance_costs_trending
profit_choppy = cum_fees_choppy - cum_il_choppy - cum_rebalance_costs_choppy

# Plotting
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(time, prices_trending, label="Trending Market")
plt.plot(time, prices_choppy, label="Choppy Market")
plt.title("ETH/USDC Price")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(time, cum_fees_trending, label="Fees (Trending)")
plt.plot(time, cum_il_trending, label="IL (Trending)")
plt.plot(time, cum_fees_choppy, label="Fees (Choppy)")
plt.plot(time, cum_il_choppy, label="IL (Choppy)")
plt.title("Cumulative Fees vs. IL")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(time, profit_trending, label="Profit (Trending)")
plt.plot(time, profit_choppy, label="Profit (Choppy)")
plt.title("Cumulative Profit")
plt.legend()

plt.tight_layout()
plt.show()

# Print final results
print("Trending Market:")
print(f"Final Fees: ${cum_fees_trending[-1]:.2f}")
print(f"Final IL: ${cum_il_trending[-1]:.2f}")
print(f"Final Rebalancing Costs: ${cum_rebalance_costs_trending[-1]:.2f}")
print(f"Final Profit: ${profit_trending[-1]:.2f}")

print("\nChoppy Market:")
print(f"Final Fees: ${cum_fees_choppy[-1]:.2f}")
print(f"Final IL: ${cum_il_choppy[-1]:.2f}")
print(f"Final Rebalancing Costs: ${cum_rebalance_costs_choppy[-1]:.2f}")
print(f"Final Profit: ${profit_choppy[-1]:.2f}")
