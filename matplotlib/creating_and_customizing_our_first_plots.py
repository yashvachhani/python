from matplotlib import  pyplot as plt

# get the avilabel style list
# print(plt.style.available)

# use style
plt.style.use('seaborn')

# Median Developer Salaries by Age
ages = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages,dev_y,'.:k',label='dev')

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages,py_dev_y,color='b',linestyle='--',linewidth='3',marker='o',label='python devloper')


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages,js_dev_y,color='#adad3b',linewidth='3',label='javascript devloper')

plt.title('midian selery (usd) by age')
plt.xlabel('ages')
plt.ylabel('midium selery')

# for showing labels
plt.legend()

# for padding issues
plt.tight_layout()

# for grid 
plt.grid(True)

plt.show()



plt.style.use('seaborn')

# Ages 18 to 55
ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

# Median Developer Salaries by Age
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]
plt.plot(ages,dev_y,label='dev')

# Median Python Developer Salaries by Age
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]
plt.plot(ages,py_dev_y,label='python devloper')


# Median JavaScript Developer Salaries by Age
js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
plt.plot(ages,js_dev_y,label='javascript devloper')

plt.title('midian selery (usd) by age')
plt.xlabel('ages')
plt.ylabel('midium selery')

# for showing labels
plt.legend()

# for padding issues
plt.tight_layout()

plt.show()
