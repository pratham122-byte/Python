import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([3, 8, 1, 10])
ypoints = np.array([10, 5, 8, 4])
plt.bar(xpoints, ypoints)
plt.title("Bar Graph")
plt.legend(["bar"])
plt.show()