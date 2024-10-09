import numpy as np


x = np.linspace(0, 10, 101)
print(x)

sin = np.sin(x)
cos = np.cos(x)

np.save("task7_sin.npy", [x, sin])

np.save("task7_cos.npy", [x, cos])

