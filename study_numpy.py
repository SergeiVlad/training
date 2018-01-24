import numpy as np
import matplotlib.pyplot as plt

A = np.loadtxt('test5.txt')

plt.plot(A[:,2])
plt.grid(True)

plt.show()