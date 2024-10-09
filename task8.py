import numpy as np
import matplotlib.pyplot as plt

x1, sin = np.load("task7_sin.npy")
x2, cos = np.load("task7_cos.npy")

plt.plot(x1, sin)
plt.plot(x2, cos)
plt.legend(["sin(x)","cos(x)"])
plt.show()