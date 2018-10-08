import numpy as np
import matplotlib.pyplot as plt

a = np.zeros( [3,2] )

a[0,0] = 3
a[0,1] = 7
a[1,0] = 1
a[2,1] = 4

plt.imshow(a, interpolation="nearest")
plt.show()

print(a)
