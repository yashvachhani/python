from matplotlib import colors, pyplot as plt

ages = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]

plt.plot(ages,dev_y,color='#000000',linestyle='-',label='all dev')

py_dev_y = [45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]

plt.plot(ages,py_dev_y,'b--', label='python dev')

plt.title("median salary USD by age")
plt.xlabel("age")
plt.ylabel("midium salary")
plt.legend()
plt.show()