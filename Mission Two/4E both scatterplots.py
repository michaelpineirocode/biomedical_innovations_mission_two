import matplotlib.pyplot as plt
import numpy as np

f = open("4B time_to_crack_s", "r").readlines()
e = open("2B time_to_crack_ns", "r").readlines()

x = []
for i in range(len(e)):
    x.append(i)


y = []
for i in e:
    y.append(float(i))

z = []
for i in f:
    z.append(float(i))

for i in range(len(x) - len(z)):
    z.append(0)

plt.scatter(x, z)
plt.scatter(x, y)
plt.show()


