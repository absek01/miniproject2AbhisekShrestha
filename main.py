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

