import numpy as np

x = np.ones((8, 8))
print('Before:')
print(x)

x[1:-1,1:-1] = 0

print('After:') 
print(x)