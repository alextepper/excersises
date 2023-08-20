# Data Types
#
# Which of the following is not a mutable data type in Python?
# a) List
# b) Dictionary
# c) Tuple
# d) Set

# c) Tuple

# Lists and Loops
#
# Using a list comprehension, generate a list of the squares of numbers from 1 to 10, but only include squares of even numbers.

numbers = [x**2 for x in [*range(1, 11, 1)] if x%2 == 0]

# Using the range function, create a list of numbers from 1 to 10, then print numbers that are divisible by both 2 and 3.

numbers2 = [x for x in [*range(1, 11, 1)] if x%2 == 0 or x%3==0 ]

# Loop through the provided list of dictionaries and print the names and ages:

student_list = [
    {
    "name": "John",
    "age": 24
    },
    {
    "name": "Anna",
    "age": 22
    },
    {
    "name": "Mike",
    "age": 25
    }
]

for item in student_list:
    print(item['name'], item['age'])

# Function Behavior with *args and **kwargs

# Write a function combine_words that accepts any number of
# positional arguments and key-value arguments. The function should
# return a single sentence combining all the words provided.
def combine_words(*args, **kwargs):
    sentence = ' '.join(args)

    sorted_kwargs = sorted(kwargs.items(), key=lambda x: x[0])
    for _, value in sorted_kwargs:
        sentence += ' ' + value

    return sentence + '.'

print(combine_words("Hello", "world", second="is", third="great!", first="Python"))

# Create a class Vehicle with string attributes type, brand, and integer attribute year.
# Ensure instances of the vehicle cannot be created
# if any of these attributes are missing and include a method to display the vehicle’s info. Use dunder method.

class Vehicle:
    def __init__(self, type, brand, year):
        if not all([type, brand, year]):
            raise ValueError("All attributes must be provided!")
        self.type = type
        self.brand = brand
        self.year = year

    def display_info(self):
        return f"Type: {self.type}, Brand: {self.brand}, Year: {self.year}"


# OOP Inheritance and Decorators
# Create a class Car with string attributes brand, model, and integer attribute mileage.
# Implement a method to return the car’s details.

class Car(Vehicle):
    def __init__(self, brand, model, mileage, year):
        super().__init__('Car', brand, year)
        self.model = model
        self.mileage = mileage

    def details(self):
        return f"{self.display_info()}, Model: {self.model}, Mileage: {self.mileage}"

# Create a subclass ElectricCar inheriting from Car with an additional float private attribute __battery_capacity.
# Override the car’s details method to include the battery capacity.
# Use the @property decorator to get the battery_capacity value and @battery_capacity.setter to modify
# the battery capacity only if the new value is positive.


class ElectricCar(Car):
    def __init__(self, brand, model, mileage, year, battery_capacity):
        super().__init__(brand, model, mileage, year)
        self.__battery_capacity = battery_capacity

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value):
        if value > 0:
            self.__battery_capacity = value
        else:
            print("Battery capacity must be positive!")

    def details(self):
        base_details = super().details()
        return f"{base_details}, Battery Capacity: {self.__battery_capacity} kWh"


# Create a BankAccount class with private float attribute _balance and private string attribute _account_holder.
# Implement methods to deposit, withdraw, and view the balance. Include a class method to track accounts created
# and a static method for a bank policy message. Ensure the balance is non-negative.

class BankAccount:
    _total_accounts = 0  # Class attribute to keep track of the total accounts created

    def __init__(self, account_holder):
        self._balance = 0.0
        self._account_holder = account_holder
        BankAccount._total_accounts += 1

    def deposit(self, amount):
        """Deposits the specified amount to the account."""
        if amount < 0:
            return "Amount to deposit should be non-negative!"
        self._balance += amount
        return f"Deposited ${amount}. New balance: ${self._balance}"

    def withdraw(self, amount):
        """Withdraws the specified amount from the account."""
        if amount < 0:
            return "Amount to withdraw should be non-negative!"
        if amount > self._balance:
            return "Insufficient balance!"
        self._balance -= amount
        return f"Withdrew ${amount}. New balance: ${self._balance}"

    def view_balance(self):
        """Returns the current balance of the account."""
        return f"Balance: ${self._balance}"

    @classmethod
    def total_accounts_created(cls):
        """Returns the total number of accounts created."""
        return f"Total accounts created: {cls._total_accounts}"

    @staticmethod
    def bank_policy():
        """Returns the bank's policy message."""
        return "Welcome to our bank. Keep your money safe with us!"


# Data Science
# Numpy and Pandas Visualization
# Create a numpy array of shape (3,3) filled with integers from 1 to 9 using arange().

import numpy as np

array = np.arange(1, 10)
array_reshaped = array.reshape(3, 3)

# Provided pandas DataFrame df:
import pandas as pd
df = pd.DataFrame({'A': [1, 'apple', 3, 4, 'banana'], 'B': [5, 6, 7, 8, 9]})

# Replace non-numeric values in column “A” with the mean of numeric values.
# Plot a histogram of the “A” column using matplotlib.

import matplotlib.pyplot as plt

df['A'] = pd.to_numeric(df['A'], errors='coerce')

mean_val = df['A'].mean()

df['A'].fillna(mean_val, inplace=True)

plt.hist(df['A'], bins=5, edgecolor='black')
plt.title('Histogram of Column A')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Plot “A” and “B” columns of df using matplotlib. Add x-axis, y-axis labels, and a title.








