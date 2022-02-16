import matplotlib.pyplot as plt
import random
import numpy as np


np.random.seed(123)
x = np.random.rand(10)
y = np.random.rand(10)
color = list(range(0,100,10))

plt.scatter(x, y , c = color, cmap= 'viridis')
#cmap为画布

plt.colorbar() #显示颜色条

plt.show()
