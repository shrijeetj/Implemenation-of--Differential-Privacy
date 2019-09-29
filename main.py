# Author: Shrijeet Joshi sjoshi22@ncsu.edu
# Date: 09/29/2019
# Description: Implementation of epsilon-Differential privacy on salary dataset to achieve 0, 0.05,0.1 ,5.0 differential privacy.
# Packages: Numpy, Pandas, MatPlotLib

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('seaborn-deep')


emp_df = pd.read_csv('IL_employee_salary.csv', keep_default_na=True, skip_blank_lines=True).dropna();
emp_sal = emp_df['Annual Salary'].str.strip();
emp_sal = emp_sal.str.replace('$', '')
emp_sal = emp_sal.str.replace(',', '')
emp_sal = np.array(emp_sal.astype(int))

bins = np.array([50000, 60000, 70000, 80000, 90000, 100000])

highest_sal = 0
second_highest_sal = 0
for sal in emp_sal:
    if highest_sal < sal:
        second_highest_sal = highest_sal
        highest_sal = sal

np.random.seed(1576436)

_EPSILON = 0.05
lmda = float(highest_sal - second_highest_sal)/float(_EPSILON)
noise = np.random.laplace(scale=lmda, size=len(emp_sal))
new_vals1 = []
for i, n in enumerate(noise):
    new_vals1.append(emp_sal[i] + int(abs(noise[i])))

_EPSILON = 0.1
lmda = float(highest_sal - second_highest_sal)/float(_EPSILON)
noise = np.random.laplace(scale=lmda, size=len(emp_sal))
new_vals2 = []
for i, n in enumerate(noise):
    new_vals2.append(emp_sal[i] + int(abs(noise[i])))

_EPSILON = 5.0
lmda = float(highest_sal - second_highest_sal)/float(_EPSILON)
noise = np.random.laplace(scale=lmda, size=len(emp_sal))
new_vals3 = []
for i, n in enumerate(noise):
    new_vals3.append(emp_sal[i] + int(abs(noise[i])))

plt.hist([emp_sal, new_vals1, new_vals2, new_vals3], bins, label=['None', '0.05','0.1','5.0'])
plt.ylabel('Number of Employees')
plt.xlabel('Salary Brackets')
plt.legend(prop={'size': 10})
plt.show()










