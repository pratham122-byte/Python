import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0.12*np.pi,4)
y=np.exp(np.sin(x))
plt.stream(x,y,use_line_collection=True)
plt.show()