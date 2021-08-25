import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data_name   = "total.csv"
data        = open(data_name, "r", encoding="utf-8").readlines()
labels = data[0].split(",")[2:len(data)]
data.pop(0)

fig, ax = plt.subplots()

colors = ['red','orange','yellow','yellowgreen','limegreen','lightskyblue','blue','purple','crimson']

def myFunc(e):
    return e[0]

def update(frame):
    ax.clear()
    row = data[frame].split(",")

    sizes = row[2:len(row)]
    group = [[int(x)] for x in sizes]

    for i in range(len(group)):
        group[i].append(labels[i])
        group[i].append(colors[i % len(colors)])

    group.sort(key=myFunc, reverse=True)

    new_colors = [x[2] for x in group]
    new_labels = [x[1] for x in group]
    new_sizes  = [x[0] for x in group]
    ax.pie(new_sizes, labels=new_labels, autopct='%1.1f%%', colors=new_colors, shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

ani = FuncAnimation(fig, update, frames=len(data), interval=100, repeat=False)
#ani.save("total.gif")
plt.show()