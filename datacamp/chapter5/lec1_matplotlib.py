# intermediate python

# ============================================
# Intermediate Python - Chapter 1 - Matplotlib
# COMPLETE NOTES
# ============================================

import matplotlib.pyplot as plt
import numpy as np

# ===== 1. WHAT IS MATPLOTLIB? =====
# Matplotlib = Python library for data visualization
# Most used visualization library in AI/ML
# Shows patterns, trends, distributions in data
# ALWAYS import as: import matplotlib.pyplot as plt

# ===== 2. LINE PLOT =====
# Used for: trends over TIME or continuous data
# X-axis = time/sequence, Y-axis = values

year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
population = [2.5, 3.0, 3.7, 4.4, 5.3, 6.1, 6.9, 7.8]

plt.plot(year, population)
plt.xlabel("Year")
plt.ylabel("Population (billions)")
plt.title("World Population Over Time")
plt.show()

# ⚠️ AI/ML use:
# Plotting training loss over epochs!
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
loss = [0.9, 0.8, 0.7, 0.6, 0.5, 0.45, 0.42, 0.40, 0.38, 0.37]
plt.plot(epochs, loss)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Over Epochs")
plt.show()

# ===== 3. SCATTER PLOT =====
# Used for: relationship/correlation between 2 variables
# Each point = one data sample

heights = [1.73, 1.68, 1.71, 1.89, 1.79, 1.65, 1.75]
weights = [65.4, 59.2, 63.6, 88.4, 68.7, 55.0, 72.0]

plt.scatter(heights, weights)
plt.xlabel("Height (m)")
plt.ylabel("Weight (kg)")
plt.title("Height vs Weight")
plt.show()

# ⚠️ AI/ML use:
# Check if features are correlated before building model
# Visualize predictions vs actual values
# Check if data is linearly separable (classification)

# ===== 4. HISTOGRAM =====
# Used for: distribution of ONE variable
# Shows how many times each value appears
# X-axis = value ranges (bins), Y-axis = frequency (count)

ages = [22, 25, 23, 28, 24, 26, 22, 27, 25, 23,
        24, 26, 28, 22, 25, 27, 23, 26, 24, 25]

plt.hist(ages, bins=6)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()

# bins = number of bars
# more bins = more detail but noisier
# fewer bins = smoother but less detail

# ⚠️ AI/ML use:
# Check distribution of features before training
# Detect skewed data (needs normalization!)
# Check if target variable is balanced/imbalanced

# ===== 5. CUSTOMIZATION =====

# --- Labels ---
plt.xlabel("X axis label")
plt.ylabel("Y axis label")
plt.title("Plot Title")

# --- Ticks ---
# Change what values appear on axes
plt.xticks([0, 1, 2, 3], ["zero", "one", "two", "three"])
plt.yticks([0, 25, 50, 75, 100])

# --- Size ---
# Change figure size (width, height in inches)
plt.figure(figsize=(10, 6))   # wider, taller plot

# --- Colors & Styles ---
plt.plot(year, population, color="red")
plt.plot(year, population, color="blue", linestyle="--")  # dashed
plt.scatter(heights, weights, color="green", alpha=0.7)   # transparency

# --- Labels on data points ---
plt.scatter(heights, weights, c=weights, cmap="viridis")  # color by value!
plt.colorbar()   # shows color scale

# ===== 6. MULTIPLE PLOTS =====
# Plot multiple lines on same graph
plt.plot(epochs, loss, label="Training Loss")
plt.plot(epochs, val_loss, label="Validation Loss")
plt.legend()    # shows labels!
plt.show()

# ⚠️ AI/ML use: Compare training vs validation loss!

# ===== 7. plt.show() vs plt.clf() =====
plt.show()   # displays the plot and clears it
plt.clf()    # clears plot WITHOUT showing
# Always call plt.show() to display!
# Call plt.clf() when starting a new plot

# ===== 8. CHOOSING THE RIGHT PLOT =====
# Line plot    → trend over time (loss, accuracy per epoch)
# Scatter plot → relationship between 2 variables (correlation)
# Histogram   → distribution of 1 variable (feature distribution)

# ===== KEY TAKEAWAYS FOR AI/ML =====
# 1. Line plot → training loss/accuracy over epochs
# 2. Scatter plot → feature correlation, predictions vs actual
# 3. Histogram → check data distribution before training
# 4. Always add labels and title — makes plots professional!
# 5. figsize=(10,6) → standard size for ML reports
# 6. alpha → transparency, useful when points overlap
# 7. legend() → essential when plotting multiple lines







# ===== THINGS I MISSED =====

# 1. plt.xscale() - logarithmic scale
plt.xscale('log')   # used when data spans huge range!
# Example: population data 1000 to 7,000,000,000
# ⚠️ AI/ML use: learning rate plots (0.0001 to 1.0)

# 2. Scatter plot with size parameter
plt.scatter(x, y, s=sizes)    # s = size of each dot
plt.scatter(x, y, c=colors)   # c = color of each dot
# ⚠️ AI/ML use: bubble charts showing 3 variables at once!

# 3. plt.grid() - add grid lines
plt.grid(True)    # makes plots easier to read

# 4. plt.tight_layout() - fixes overlapping labels
plt.tight_layout()   # always call before plt.show()!

# 5. Comparing histograms
plt.hist(data1, bins=10, label="Group 1", alpha=0.5)
plt.hist(data2, bins=10, label="Group 2", alpha=0.5)
plt.legend()
plt.show()
# alpha=0.5 makes them transparent so both visible!
# ⚠️ AI/ML use: compare distribution of 2 features!

# 6. plt.xticks rotation
plt.xticks(rotation=45)   # rotate labels so they don't overlap
# used when x-axis labels are long strings!