import numpy as np

# sigmas = np.array([.26, .25, .25, .35, .35, .79, .79, .72, .72, .62,.62, 1.07, 1.07, .87, .87, .89, .89])/10.0

sigmas = np.array([3, 6, 0.025, 0.025, 0.025, 0.025])

varsj = (sigmas * 2)**2

print(varsj)

