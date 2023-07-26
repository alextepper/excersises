# Exercise 2: Import
import datetime

from func import adding
from func import random_string
from func import get_current_date, days_till_date, minutes_since_birth

adding(1,2)

print(random_string())

print(get_current_date())

print(days_till_date(datetime.datetime(year=2024, month=1, day=1)))

print(minutes_since_birth(datetime.datetime(1992, 6, 14)))