import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(["A", "B", "C", "D", "E"])
ypoints = np.array([240, 258, 245, 276, 298])

plt.bar(xpoints, ypoints)
plt.xlabel("Avg Pulse")
plt.ylabel("Calorie Burnage")

plt.show()