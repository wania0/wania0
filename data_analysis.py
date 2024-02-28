import pandas as pd
import matplotlib.pyplot as plt

location = "C:\\Users\HP\Documents\mybook.xlsx"
df = pd.read_excel(location)
column_data = df["Amount of Rainfall"]

mean = column_data.mean()
median = column_data.median()
mode = column_data.mode()[0]  # mode() returns a Series, get the first mode if there are multiple
std_dev = column_data.std()
variance = column_data.var()

print(f"The value of mean is : {mean}")
print(f"The value of median is : {median}")
print(f"The value of standard deviation is: {std_dev}")
print(f"The value of variance is : {variance}")
print(f"The value of mode is : {mode}")

# Create a figure and a set of subplots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))  # Adjust figsize to fit your screen

# Plotting the histogram on the first subplot
axs[0].hist(column_data, bins=20, alpha=0.7, color='blue', edgecolor='black')
axs[0].set_title('Distribution of Amount of Rainfall')
axs[0].set_xlabel('Amount of Rainfall')
axs[0].set_ylabel('Frequency')
axs[0].axvline(mean, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean:.2f}')
axs[0].axvline(median, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median:.2f}')
axs[0].axvline(mode, color='orange', linestyle='dashed', linewidth=1, label=f'Mode: {mode:.2f}')
axs[0].legend()

# Creating a box plot on the second subplot
axs[1].boxplot(column_data, vert=True, patch_artist=True)
axs[1].set_title('Box Plot of Amount of Rainfall')
axs[1].set_ylabel('Amount of Rainfall')
axs[1].set_xticks([1])
axs[1].set_xticklabels(['Rainfall'])
axs[1].grid(True)

plt.tight_layout()  # Adjust the layout to make sure everything fits without overlapping
plt.show()  # Display the plots
