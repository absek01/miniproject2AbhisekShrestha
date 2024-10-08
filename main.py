# INF601 - Advanced Programming in Python
# Abhisek Shrestha
# Mini Project 2

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import os
from faker import Faker
import numpy as np

# Create a "charts" folder if it doesn't exist
if not os.path.exists('charts'):
    os.makedirs('charts')

# Initialize the Faker object to generate fake data
fake = Faker()

# Generate fake data for 100 people
data = {
    'Name': [fake.name() for _ in range(100)],
    'Age': [fake.random_int(min=18, max=80) for _ in range(100)],
    'Country': [fake.country() for _ in range(100)],
    'Salary': [round(fake.random_number(digits=5), 2) for _ in range(100)]
}

# Store data in a Pandas DataFrame
df = pd.DataFrame(data)

# Display the first 5 rows of the data
print(df.head())

# Some basic statistics about Age and Salary
age_stats = df['Age'].describe()
salary_stats = df['Salary'].describe()

print("\nAge Statistics:\n", age_stats)
print("\nSalary Statistics:\n", salary_stats)

# Visualize Age Distribution with Histogram
plt.figure(figsize=(10,6))
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution of Individuals')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('charts/age_distribution.png')  # Save the chart as a PNG file

# Visualize Salary Distribution with a Boxplot
plt.figure(figsize=(10,6))
plt.boxplot(df['Salary'])
plt.title('Salary Distribution of Individuals')
plt.ylabel('Salary ($)')
plt.savefig('charts/salary_distribution.png')  # Save the chart as a PNG file

# Bar chart showing average salary by age group
age_groups = pd.cut(df['Age'], bins=[18, 30, 40, 50, 60, 80], labels=["18-30", "31-40", "41-50", "51-60", "61+"])
avg_salary_by_age = df.groupby(age_groups)['Salary'].mean()

plt.figure(figsize=(10,6))
avg_salary_by_age.plot(kind='bar', color='orange', edgecolor='black')
plt.title('Average Salary by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Salary ($)')
plt.grid(True)
plt.savefig('charts/avg_salary_by_age_group.png')  # Save the chart as a PNG file

# Pie chart for countries representation
plt.figure(figsize=(10,6))
country_counts = df['Country'].value_counts().head(5)  # Get top 5 countries
plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'pink'])
plt.title('Top 5 Countries Represented')
plt.savefig('charts/top_countries.png')  # Save the chart as a PNG file

plt.show()