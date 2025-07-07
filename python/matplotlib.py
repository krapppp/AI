import matplotlib.pyplot as plt

x = [2016, 2017, 2018, 2019, 2020]
y = [350, 410, 520, 695, 543]
plt.title('Annual sales')
plt.xlabel('years')
plt.ylabel('sales')
plt.plot(x,y)
plt.show()

#############################################

y1 = [350, 410, 520, 695]
y2 = [200, 250, 385, 350]
x = range(len(y1))
xLabel = ['first', 'second', 'third', 'fourth'] 

plt.bar(x, y1, width = 0.7, color = "blue")
plt.bar(x, y2, width = 0.7, color = "red", bottom = y1)
plt.title('Quarterly sales')
plt.xlabel('Quarters')
plt.ylabel('sales')
plt.xticks(x, xLabel, fontsize = 10)
plt.legend(['chairs', 'desks'])
plt.show()