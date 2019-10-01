# Author: Shrijeet Joshi sjoshi22@ncsu.edu
# Date: 09/29/2019
# Description: Implementation of epsilon-Differential privacy on salary dataset to achieve 0, 0.05,0.1 ,5.0 differential privacy.
# Packages: Numpy, Pandas, MatPlotLib

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

emp_df = pd.read_csv('IL_employee_salary.csv', keep_default_na=True, skip_blank_lines=True).dropna();
emp_df['Annual Salary'] = emp_df['Annual Salary'].str.replace(',', '')
emp_df['Annual Salary'] = emp_df['Annual Salary'].str.replace('$', '')
emp_df['Annual Salary'] = emp_df['Annual Salary'].astype(float)
bins = [50000, 60000, 70000, 80000, 90000, 100000]
count, bins, bars = plt.hist(emp_df['Annual Salary'], bins=bins)
plt.show()

#np.random.seed(1576436)
sensitivity = 1
epsilon1 = 0.05
epsilon2 = 0.1
epsilon3 = 5.0

lmda1 = sensitivity/epsilon1
lmda2 = sensitivity/epsilon2
lmda3 = sensitivity/epsilon3

noise1 = np.random.laplace(0., lmda1, len(bins)-1)
noise2 = np.random.laplace(0., lmda2, len(bins)-1)
noise3 = np.random.laplace(0., lmda3, len(bins)-1)

data = np.arange(len(count))
data1 = [x + 0.2 for x in data]
data2 = [x + 0.2 for x in data1]
data3 = [x + 0.2 for x in data2]

plt.bar(data, count, color='#eb4034', width=0.2, edgecolor='white', label='NA')
plt.bar(data1, count + noise1, color='#ebe534', width=0.2, edgecolor='white', label='0.05')
plt.bar(data2, count + noise2, color='#43eb34', width=0.2, edgecolor='white', label='0.1')
plt.bar(data3, count + noise3, color='#3440eb', width=0.2, edgecolor='white', label='5.0')
plt.legend()
plt.show()