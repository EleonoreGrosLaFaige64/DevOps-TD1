import pytest
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random
from math import sqrt

#faire un triangle

import matplotlib.patches as patches
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.gca()
path = [
    [0, 0.5],
    [0, 0],
    [0.5,0],
]
ax.add_patch(patches.Polygon(path))

plt.xlim([-1, 1])
plt.ylim([-1, 1])
  
plt.show()

#test
