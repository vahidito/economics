import numpy as np
import matplotlib.pyplot as plt


def generate_data(n: int):
    eee = []
    for i in range(n):
        e = np.random.randn()
        eee.append(e)
    return eee


data = generate_data(100)
plt.plot(data)
plt.show()
