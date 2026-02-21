# Lecture 08: Data Visualization using Matplotlib and Seaborn
# Topics covered:
# 1. Line plots using Matplotlib
# 2. Bar plots using Seaborn
# 3. Customizing titles and styles


# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns


# -----------------------------------------
# Sample Data

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 10, 12]

print("X values:", x)
print("Y values:", y)


# -----------------------------------------
# Example 1: Line Plot using Matplotlib

plt.figure(figsize=(6, 4))
plt.plot(x, y, label="Line Plot", color="blue", marker="o")

plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

plt.show()


# -----------------------------------------
# Example 2: Bar Plot using Seaborn

sns.set(style="whitegrid")

plt.figure(figsize=(6, 4))
sns.barplot(x=x, y=y, palette="viridis")

plt.title("Simple Bar Graph")

plt.show()
