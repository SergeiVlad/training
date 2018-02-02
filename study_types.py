import numpy as np
import matplotlib.pyplot as plt

y = {}
# Data for plotting
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y[0] = np.cos(2 * np.pi * x1) 
y[1] = np.cos(2 * np.pi * x2)
y[2] = np.cos(2 * np.pi * x2)

# Create two subplots sharing y axis
fig, ax = plt.subplots(3, sharey=True)

for i in range(3):
	ax[i].plot(y[i])
	ax[i].set(title='title', ylabel='ffffffff')

plt.show()