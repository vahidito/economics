import numpy as np
import matplotlib.pyplot as plt

t_vals = np.linspace(0, 2, 10)
x = np.linspace(0, 5, 200)
fig, ax = plt.subplots()
for tet in t_vals:
    ax.plot(x, np.cos(np.pi * tet * x) * np.exp(- x))
plt.show()
