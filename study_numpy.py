import numpy as np
import matplotlib.pyplot as plt

# A = np.loadtxt('test0.txt', skiprows = 1, converters = {6: lambda x: int(x, 16)})
# A = np.loadtxt('test0.txt', skiprows = 1, usecols = (0,1,2,3,4))
# A = np.loadtxt('test0.txt', skiprows = 1, usecols = (0,1,2,3,4,5), unpack = True)
hex2int = lambda x: int(x, 16)
A = np.loadtxt('test0.txt', skiprows = 1, converters = {6: hex2int})

plt.plot(A)
plt.grid(True)
plt.show()