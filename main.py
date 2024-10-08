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