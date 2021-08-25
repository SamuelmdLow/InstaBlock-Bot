import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data_name   = "rolling_sum.csv"
data        = open(data_name, "r", encoding="utf-8").readlines()
data.pop(0)

fig, ax = plt.subplots()
xdata   = []
ydata   = []
ln,     = plt.plot([], [])
ax.set_xlim(0, len(data))
ax.set_ylim(0, 20)

def update(frame):
    xdata.append(frame)
    row = data[frame].split(",")
    ydata.append(int(row[0]))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=len(data), interval=20, blit=True, repeat=False)
#ani.save("blocked_rolling_sum.gif")
plt.show()