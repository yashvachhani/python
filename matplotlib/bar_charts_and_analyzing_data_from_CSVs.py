from matplotlib import  pyplot as plt
import numpy as np
import csv
plt.style.use('seaborn')
'''
# Median Developer Salaries by Age
ages = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_index = np.arange(len(ages))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_index - width, dev_y, width=width, label='dev')

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_index, py_dev_y, width=width, label='python devloper')

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_index + width, js_dev_y, width=width, label='javascript devloper')

# set diffrent labals and difrent index as a x values
plt.xticks(ticks=x_index, labels=ages)

plt.title('midian selery (usd) by age')
plt.xlabel('ages')
plt.ylabel('midium selery')

# for showing labels
plt.legend()

# for padding issues
plt.tight_layout()

plt.show()
'''

with open("matplotlib/data.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    row = next(reader)
    print(row['LanguagesWorkedWith'].split(';'))