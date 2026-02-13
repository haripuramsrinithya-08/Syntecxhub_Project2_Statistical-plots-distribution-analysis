import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset

df = sns.load_dataset("tips")

# Histogram + KDE

sns.histplot(df['total_bill'], kde=True)
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.savefig("histogram_total_bill.png")  
plt.show()

# Boxplot for Outliers

sns.boxplot(x=df['total_bill'])
plt.title("Boxplot of Total Bill")
plt.savefig("boxplot_total_bill.png")
plt.show()

# Group Comparison by Day

sns.boxplot(x='day', y='total_bill', data=df)
plt.title("Total Bill Comparison Across Days")
plt.savefig("comparison_by_day.png")
plt.show()

print("All graphs generated and saved successfully.")
