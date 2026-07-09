# ============================================
# Intermediate Python - Chapter 1 - Matplotlib
# PRACTICE
# ============================================

import matplotlib.pyplot as plt
import numpy as np

# ===== LEVEL 1: BASICS =====

# Q1. Which plot type would you use for each scenario?
# Write your answer as a comment:

# 1. Show how model accuracy changed over 10 epochs                line plot
# 2. Show relationship between house size and price                scatter plot
# 3. Show distribution of student exam scores                      histogram
# 4. Show how temperature changed over a week                      line plot
# 5. Show correlation between two features in dataset              scatter plot

# Correlation between 2 variables = scatter plot!

# 1 variable  → histogram
# 2 variables → scatter plot
# over time   → line plot







# Q2. Fix the bugs:
import matplotlib.pyplot as plt
year = [2015, 2016, 2017, 2018, 2019, 2020]
sales = [100, 150, 130, 180, 200, 220]

plt.plot(year, sales)
plt.xlabel = "Year"          # bug 1         plt.xlabel('Year)         xlabel is a FUNCTION not attribute
plt.ylabel = "Sales"         # bug 2         plt.ylabel('Sales')
plt.Title("Sales Over Time") # bug 3         plt.title('Sales over time')
show()                        # bug 4        plt.show()







# ===== LEVEL 2: PLOT TYPES =====

# Q3. Create a line plot:
# You are tracking model training
import matplotlib.pyplot as plt
epochs = list(range(1, 11))
train_loss = [0.9, 0.8, 0.65, 0.55, 0.48, 0.43, 0.40, 0.38, 0.36, 0.35]
val_loss = [0.95, 0.85, 0.72, 0.65, 0.60, 0.58, 0.57, 0.56, 0.56, 0.57]

# Plot BOTH train_loss and val_loss on SAME graph
plt.plot(epochs,train_loss,label="Data Training",  color = "purple")
plt.plot(epochs,val_loss,label="Data Validation",  color = "green")
# Add: xlabel, ylabel, title, legend
plt.xlabel('Epochs')
plt.ylabel('loss')
plt.title("Model Training")
plt.legend()
# Use different colors for each line
# Add grid
plt.grid(True)
plt.show()



# Overfitting = training loss decreasing but validation loss increasing
# Means model memorized training data, fails on new data!
# This graph shows NO overfitting - both losses decrease together




# Training loss → keeps going DOWN ✅ (model is learning)
# Validation loss → goes down then FLATTENS at epoch 7-8

# This is actually a GOOD model — no overfitting here!
# Both losses are decreasing together





# OVERFITTING happens when:
# Training loss   → keeps going DOWN ↓
# Validation loss → starts going UP ↑ (they DIVERGE!)

# Like this:
# epoch    train_loss    val_loss
# 1        0.90          0.95
# 5        0.50          0.55    ← both decreasing = good
# 8        0.30          0.45    ← gap getting bigger = warning!
# 10       0.15          0.60    ← OVERFITTING! train low, val high!

# Model memorized training data
# But fails on new unseen data!






# Overfit model = useless in real world!
# This graph (Q8) will show clear overfitting:
# train_acc → keeps going up to 0.94
# val_acc   → goes up then comes DOWN from epoch 11
# That's why Q8 asks you to mark where overfitting starts!







# Q4. Create a scatter plot:
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
study_hours = np.random.uniform(1, 10, 50)
exam_scores = study_hours * 8 + np.random.normal(0, 5, 50)

# 1. Create scatter plot
plt.scatter(study_hours,exam_scores,color="green",alpha=0.6)
# 2. Add labels and title
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Study Hours vs Exam Scores")
# 3. Make dots green with alpha=0.6
# 4. Add grid
plt.grid(True)
plt.show()
# What relationship do you see? Write as comment!
# it is a scatter plot - number of study hours increase as exam scores also increase



# Relationship observed:
# POSITIVE CORRELATION between study hours and exam scores
# As study hours increase → exam scores increase
# This is a LINEAR relationship (points form diagonal pattern)

# In ML terms:
# study_hours = FEATURE (X)
# exam_scores = TARGET (y)
# This data is perfect for LINEAR REGRESSION!








# Q5. Create a histogram:

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
scores = np.random.normal(75, 10, 200)  # 200 students, mean=75, std=10

# 1. Plot histogram with 20 bins
plt.hist(scores,bins=20, color="blue",alpha=0.7)
# 2. Add labels and title
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Students scores")
# 3. Make bars blue with alpha=0.7
# 4. Is this data normally distributed? Write as comment!
plt.show()

# yes, the graph is symmetrical

# Yes this is NORMALLY DISTRIBUTED (bell curve shape)!
# Symmetrical around mean (75)
# Most students scored between 65-85
# Very few scored below 50 or above 100

# In ML this matters because:
# Many ML algorithms assume normal distribution
# If data is NOT normal → needs transformation before training!








# ===== LEVEL 3: CUSTOMIZATION =====

# Q6. Predict what this code does WITHOUT running:
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]
plt.plot(x, y, color="red", linestyle="--", linewidth=2)
plt.xticks([1, 2, 3, 4, 5], ["Mon", "Tue", "Wed", "Thu", "Fri"])
plt.yticks([1, 2, 3, 4, 5])
plt.title("Weekly Sales")
plt.grid(True)
plt.tight_layout()
plt.show()


# plot size is 10,6 ---- x and y has some values , we change the x values thorugh x-ticks 
# now x values are mon-fri and also change y values 1-5        - it has title - it has grid
# the plot shows lines becuase it's some numbers over time(days of weeks) - the line will be red, dotted and of width 2










# ===== LEVEL 4: CHOOSING RIGHT PLOT =====

# Q7. Look at this data and decide which plot is best and WHY:
# Dataset 1: [time_of_day, number_of_users_online]
# line plot - it's users over time

# Dataset 2: [age, salary] for 1000 employees
# 2 variables - scatter plot

# Dataset 3: [pixel_values] for 10000 images (values 0-255)
# histogram - distribution of values

# Dataset 4: [month, revenue] for 2 years
# line plot - revenue over months(time)


# Time on x-axis → LINE PLOT
# Two measurements → SCATTER PLOT
# One variable distribution → HISTOGRAM

# Dataset 4 has months (time) on x-axis → Line plot! 💡






# ===== LEVEL 5: AI/ML CHALLENGE =====

# Q8. Training visualization (most important in ML!):
import matplotlib.pyplot as plt
epochs = list(range(1, 21))
train_acc = [0.60, 0.68, 0.74, 0.79, 0.82, 0.85, 0.87, 0.88,
             0.89, 0.90, 0.91, 0.91, 0.92, 0.92, 0.93, 0.93,
             0.93, 0.94, 0.94, 0.94]
val_acc =   [0.58, 0.65, 0.70, 0.74, 0.77, 0.79, 0.80, 0.80,
             0.81, 0.81, 0.80, 0.79, 0.78, 0.77, 0.76, 0.75,
             0.74, 0.73, 0.72, 0.71]

# Create a professional ML training plot:
# 1. Plot both train_acc and val_acc
plt.figure(figsize=(10,6))
plt.plot(epochs,train_acc,color="blue",label="Training accuracy")
plt.plot(epochs,val_acc,color="orange" , label="Validation accuracy")
plt.axvline(x=11,color="red",linestyle='--', label="Overfitting starts")

# 2. Use blue for train, orange for val
# 3. Add proper labels, title, legend
plt.xlabel("epochs")
plt.ylabel("Loss")
plt.title("Epochs vs Losses")
plt.legend()
# 4. Add grid
plt.grid(True)
# 5. Set figsize=(10, 6)

# 6. Add a vertical line where val_acc starts dropping
#    hint: plt.axvline(x=11, color='red', linestyle='--')

# 7. Print: "Model starts overfitting at epoch X"
#    (look at where val_acc starts decreasing!)

print(f"Model start overfitting at epoch 11")
plt.show()







# Before epoch 11:
# Both lines going UP together → model is LEARNING ✅

# After epoch 11:
# Training acc → still going UP (model memorizing!)
# Validation acc → going DOWN (failing on new data!)
# Gap getting BIGGER → OVERFITTING! ⚠️

# Best model = save weights at epoch 11
# (called "Early Stopping" in ML!)







# Q9. Feature distribution analysis:
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
feature_normal = np.random.normal(50, 10, 1000)
feature_skewed = np.random.exponential(20, 1000)

plt.hist(feature_normal,bins=30,color="pink",alpha=0.5,label="Normal")
plt.hist(feature_skewed,bins=30,color="crimson",alpha=0.5,label="skewed")

plt.xlabel("Normal")
plt.ylabel("Values")
plt.title("Dist Analysis")
plt.legend()
plt.show()

# 1. Plot both histograms on SAME graph
# 2. Use different colors and alpha=0.5
# 3. Add legend, labels, title
# 4. Which feature needs normalization? Write as comment!
# 5. Why does skewed data cause problems in ML? Write as comment!





# 4
# Look at your plot:
# Pink (Normal) → bell shape, centered around 50
#                 values between 20-80 mostly
# Red (Skewed)  → huge bar at left, tiny bars going right
#                 most values near 0, few values up to 150!

# feature_skewed needs normalization!
# Because its values are all over the place (0 to 150+)
# feature_normal is already nice and centered




# 5
# Imagine teaching a student (ML model) with these exam scores:
# [1, 2, 1, 3, 2, 1, 95, 1, 2, 1]

# Model sees mostly 1s and 2s
# So it thinks "normal score = 1 or 2"
# When it sees 95 → treats it as weird outlier
# → makes wrong predictions!



# In ML:
# Most algorithms calculate distances between points
# Skewed data → distances become meaningless
# Model gets confused by huge values

# Example:
# House prices: most are 100k-300k
# One house: 10,000,000 (outlier!)
# Model focuses too much on that one house
# → bad predictions for normal houses!

# Fix = log transformation:
import numpy as np
fixed = np.log(feature_skewed)
# Now values are compressed and more normal!









# Q10. Complete analysis plot:
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
x = np.linspace(0, 10, 100)
y_true = 2 * x + 1
y_pred = y_true + np.random.normal(0, 2, 100)

# Create figure with 2 subplots side by side:
# Left plot: scatter of y_true vs y_pred
#            add diagonal line (perfect predictions line)
#            title: "Predictions vs Actual"

# Right plot: histogram of errors (y_pred - y_true)
#             title: "Error Distribution"
# hint: fig, axes = plt.subplots(1, 2, figsize=(12, 5))
#       axes[0].scatter(...)
#       axes[1].hist(...)
# 5. plt.tight_layout()
# 6. plt.show()



fig,axes = plt.subplots(1,2,figsize=(12,5))
axes[0].scatter(y_true,y_pred)
axes[0].plot([y_true.min(),y_true.max()],[y_true.min(),y_true.max()],color="red", linestyle="--", label="Perfect prediction")

axes[0].set_xlabel("Actual")
axes[0].set_ylabel("Predicted")
axes[0].set_title("Predictions vs Actual")
axes[0].legend()
axes[0].grid(True)



errors = y_pred - y_true
axes[1].hist(errors,bins=20,color="orange", alpha=0.7)
axes[1].set_title("Error Distribution")
axes[1].set_xlabel("Error")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.show()







# Single plot:        # Subplots:
# plt.title()          axes[0].set_title()
# plt.xlabel()         axes[0].set_xlabel()
# plt.ylabel()         axes[0].set_ylabel()
# plt.legend()         axes[0].legend()




# Left plot tells us:
# Points follow the red line closely → model predicts well!
# Some scatter = normal random error

# Right plot tells us:
# Errors centered at 0 → no systematic bias!
# Symmetric distribution → model not over/under predicting
# This is exactly what you WANT to see in a good ML model!