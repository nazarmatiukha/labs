import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = lambda x: np.cos(x)
plt.plot(x, -x**(y(5*x)))
plt.show()
