import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()  # Turn on interactive mode

x = np.arange(0, 10, 0.1)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

for i in range(100):
    y = np.sin(x + i/10)
    line.set_ydata(y)
    plt.draw()
    plt.pause(0.1)  # Pause for a short time to allow the plot to update