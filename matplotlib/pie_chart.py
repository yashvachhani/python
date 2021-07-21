from matplotlib import colors, pyplot as plt

plt.style.use("fivethirtyeight")

slice = [120,80,30,20]
labels = ['forty','sixty','extra1','extra2']
colors=['blue','red','yello','green']
explode= [0,0.1,0.2,0]
plt.pie(slice, labels = labels, explode = explode, startangle=90,autopct='%1.1f%%', shadow = True, wedgeprops = { 'edgecolor' : 'black' } )

plt.title("my awsome pychart")

plt.tight_layout()

plt.show()