from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

minutes = [1,2,3,4,5,6,7,8,9]

player1 = [1,2,3,0,8,4,4,4,5]
player2 = [1,1,1,5,4,2,2,3,4]
player3 = [1,1,1,8,0,2,3,3,3]

# simple pie plote
#plt.pie([1,1,1],labels=['player1','player2','player3'])

# stackplot
plt.stackplot(minutes,player1,player2,player3)
plt.title("my awsome stack plot")
plt.tight_layout()
plt.show()