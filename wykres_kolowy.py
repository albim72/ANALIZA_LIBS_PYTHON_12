import matplotlib.pyplot as plt


labels = 'Warszawa','Kraków','Lublin','Katowice','Zakopane'
print(type(labels))

sizes = [56,34,27,28,39]
explode = (0,0.1,0,0,0.2)

fig,ax = plt.subplots()
ax.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.show()
