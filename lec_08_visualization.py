import matplotlib.pyplot as plt
import seaborn as sns

# x = [1,2,3,4,5]
# y = [10,15,7,10,12]

# print("X value: ",x)
# print("Y value: ",y)

# plt.figure(figsize=(6,4))
# plt.plot(x,y,label='Line Plot',color='blue',marker='o')

# plt.title("Simple Line Plot")
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# plt.legend()

# plt.show()











x = [1,2,3,4,5]
y = [10,15,7,10,12]

print("X value: ",x)
print("Y value: ",y)

sns.set(style="whitegrid")
plt.figure(figsize=(6,4))
sns.barplot(x=x,y=y,palette="viridis")

plt.title("Simple Bar Graph")
plt.show()