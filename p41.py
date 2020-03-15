import numpy as np
import matplotlib.pyplot as plt
ts = 100
values = []

for i in range(ts):
    eee = np.random.randn()
    values.append(eee)

plt.plot(values)
plt.show()