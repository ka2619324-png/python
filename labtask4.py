# --------------------------------------------------------------- 
# Mini Project: Basic Data Visualizer
# Course: Foundations of Programming using Python (ETCCFP103)
# File Name: data_visualizer.py
# Student: (Your Name)
# ---------------------------------------------------------------

# IMPORTING REQUIRED LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# TASK 1: DATASET LOADING
# ---------------------------------------------------------------

print("Loading dataset...")
df = pd.read_csv("C:/Users/91628/Downloads/temperature.csv")

# FIX 1: Clean column names (important!)
df.columns = df.columns.str.strip().str.lower()

print("\nCleaned column names:", df.columns.tolist())

# Display first 10 rows
print("\nFirst 10 rows of the dataset:")
print(df.head(10))

# ---------------------------------------------------------------
# TASK 2: DATA CLEANING
# ---------------------------------------------------------------

print("\nChecking for missing values:\n")
print(df.isnull().sum())

# Fill missing temperature values with mean
if "temperature" in df.columns:
    df["temperature"].fillna(df["temperature"].mean(), inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# ---------------------------------------------------------------
# TASK 3: LINE PLOT (Temperature Over Time)
# ---------------------------------------------------------------

print("\nGenerating line plot...")

# FIX 2: Convert date column to datetime format
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"])
else:
    print("ERROR: 'date' column NOT found. Please check CSV.")
    exit()

plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["temperature"], marker="o")
plt.title("Temperature Variation Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig("line_plot.png")
plt.close()
print("line_plot.png saved successfully.")

# ---------------------------------------------------------------
# TASK 4: BAR CHART (Group by Month)
# ---------------------------------------------------------------

print("Generating bar chart...")

# FIX 3: Create month column from date
df["month"] = df["date"].dt.strftime("%B")

# Group by month and calculate average temperature
monthly_avg = df.groupby("month")["temperature"].mean()

plt.figure(figsize=(10, 5))
plt.bar(monthly_avg.index, monthly_avg.values)
plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Average Temperature")
plt.xticks(rotation=45)
plt.tight_layout()

# Save bar chart
plt.savefig("bar_chart.png")
plt.close()
print("bar_chart.png saved successfully.")

# ---------------------------------------------------------------
# FINAL OUTPUT
# ---------------------------------------------------------------
print("\nAll tasks completed successfully!")
print("Plots saved as: line_plot.png and bar_chart.png")
print("Check your working directory for the images.")

# ---------------------------------------------------------------
# OPTIONAL BONUS (Uncomment to enable)
# ---------------------------------------------------------------

# SCATTER PLOT (Bonus)
plt.figure(figsize=(10, 5))
plt.scatter(df["temperature"], df["humidity"])
plt.title("Temperature vs Humidity")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.savefig("scatter_bonus.png")
plt.close()
print("scatter_bonus.png saved successfully.")
