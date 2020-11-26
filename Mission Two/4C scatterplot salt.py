import matplotlib.pyplot as plt
import numpy as np

f = open("4B time_to_crack_s", "r").readlines()

x = []
for i in range(len(f)):
    x.append(i)


y = []
for i in f:
    y.append(float(i))

plt.scatter(x, y)
plt.show()

