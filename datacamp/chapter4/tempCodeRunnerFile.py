# Q10. Dataset preprocessing challenge:
# You have a dataset of house prices
import numpy as np
np.random.seed(42)
prices = np.array([250000, 380000, 150000, 520000, 290000,
                   410000, 175000, 340000, 1200000, 310000])

# 1. Check mean vs median — are there outliers?
print(np.mean(prices))

print(np.median(prices))                # mean is greater than median so there r outliers

# 2. Find the outlier (price > 800000)

print(prices[prices > 800000])

# 3. Remove the outlier and store as clean_prices
clean_prices= prices[prices < 800000]
print(clean_prices)


# 4. Recalculate mean and median of clean_prices
print(np.mean(clean_prices))
print(np.median(clean_prices))


# 5. Normalize prices to 0-1 range:
min_prices = np.min(clean_prices)
max_prices = np.max(clean_prices)
normalized = (clean_prices - min_prices) / (max_prices - min_prices)



# 6. Print: "Original mean: X | Clean mean: X | Difference: X"
diff= np.mean(clean_prices) - np.mean(prices)
print(f"Original mean: {np.mean(prices):.0f} | Clean mean: {np.mean(clean_prices):.0f} | Difference: {diff:.0f}")