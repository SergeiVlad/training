import numpy as np
import matplotlib.pyplot as plt

# A = np.loadtxt('test0.txt', skiprows = 1, converters = {6: lambda x: int(x, 16)})
# A = np.loadtxt('test0.txt', skiprows = 1, usecols = (0,1,2,3,4))
# A = np.loadtxt('test0.txt', skiprows = 1, usecols = (0,1,2,3,4,5), unpack = True)
float2int = lambda x: int(x)
hex2int = lambda x: int(x, 16)

A = np.loadtxt('test0.txt', skiprows = 1, converters = {6:hex2int})

# plt.plot(A)
# plt.grid(True)
# plt.show()

# from io import StringIO
# c = StringIO("0 1\n2 3")
# # B = np.loadtxt(c, dtype = {'names': ('one', 'two'), 'formats':('i4','f4')})
# B = np.loadtxt(c, dtype = {'formats':('i4','f4'),'names':('i','f')})
# c = StringIO("0 1\n2 3")
# C = np.loadtxt(c)