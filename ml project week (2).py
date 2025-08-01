# Titanic Dataset - Exploratory Data Analysis (EDA) - Micro Project
# Author: Renu Kumari Prajapati

# Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Optional: Check current working directory
print("Current Directory:", os.getcwd())

# Step 2: Load the Titanic Datasets (Change the paths if needed)
train = pd.read_csv(r"C:\Users\RENU\Downloads\Project week 1\train.csv")
test = pd.read_csv(r"C:\Users\RENU\Downloads\Project week 1\test.csv")
gender = pd.read_csv(r"C:\Users\RENU\Downloads\Project week 1\gender_submission.csv")

# Step 3: Basic Info
print("Train Data Info:")
print(train.info())
print("\nTest Data Info:")
print(test.info())
print("\nGender Submission Info:")
print(gender.info())

# Step 4: Preview the data
print("Train Head:\n", train.head())
print("Test Head:\n", test.head())
print("Gender Submission Head:\n", gender.head())

# Step 5: Descriptive Statistics
print("Descriptive Statistics:\n", train.describe())

# Step 6: Central Tendency & Dispersion
print("\n--- AGE Statistics ---")
print("Mean Age:", train['Age'].mean())
print("Median Age:", train['Age'].median())
print("Mode Age:", train['Age'].mode()[0])
print("Age Variance:", train['Age'].var())
print("Age Std Dev:", train['Age'].std())
print("Age Range:", train['Age'].max() - train['Age'].min())
print("Age Skewness:", train['Age'].skew())
print("Age Kurtosis:", train['Age'].kurt())

print("\n--- FARE Statistics ---")
print("Mean Fare:", train['Fare'].mean())
print("Fare Skewness:", train['Fare'].skew())
print("Fare Kurtosis:", train['Fare'].kurt())

# Step 7: Univariate Visualizations
plt.hist(train['Age'].dropna(), bins=10, color='lightblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

sns.boxplot(x=train['Fare'], color='orange')
plt.title('Boxplot of Fare')
plt.show()

# Step 8: Distribution and Density Plots
sns.displot(train['Fare'], kde=True, bins=30, color="purple")
plt.title("Fare Distribution")
plt.show()

sns.kdeplot(train['Age'].dropna(), fill=True, color='green')
plt.title("Density Plot of Age")
plt.show()

# Step 9: Categorical Visualizations
sns.countplot(x='Survived', data=train)
plt.title("Survival Count")
plt.xticks([0, 1], ['Not Survived', 'Survived'])
plt.show()

sns.countplot(x='Sex', hue='Survived', data=train)
plt.title("Survival by Sex")
plt.show()

sns.countplot(x='Pclass', hue='Survived', data=train)
plt.title("Survival by Passenger Class")
plt.show()

# Step 10: Bivariate Scatter Plot
sns.scatterplot(data=train, x='Age', y='Fare', hue='Survived')
plt.title("Age vs Fare (by Survival)")
plt.show()

# Step 11: Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(train.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Step 12: Merge test with gender_submission (Optional - for Prediction Analysis)
merged_test = pd.merge(test, gender, on='PassengerId', how='left')
print("\nMerged Test with Gender Submission:\n", merged_test.head())

# Step 13: Summary Insights
print("\n📝 Summary Insights:")
print("1. Females and 1st-class passengers had higher survival rates.")
print("2. Age and Fare have some outliers (shown in boxplots).")
print("3. Age and Fare are slightly skewed.")
print("4. Strong negative correlation between Pclass and Fare.")
print("5. Young children also had better chances of survival.")
