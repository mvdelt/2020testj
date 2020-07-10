# i. from matplotlib 3.2.1 doc.

# <Agg Buffer To Array>
# - Convert a rendered figure to its image (NumPy array) representation.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvas  # i. -> FigureCanvasAgg 의 alias 라 함. 걍 똑같은거인듯. 

# Create a figure that pyplot does not know about.
fig = Figure()
# attach a non-interactive Agg canvas to the figure
# (as a side-effect of the ``__init__``)
canvas = FigureCanvas(fig) # i. 이걸 플롯팅 이후에 해줘도 상관없음.
ax = fig.subplots()
ax.plot([1, 2, 3])
ax.set_title('a simple figure')
# Force a draw so we can grab the pixel buffer
canvas.draw() # i. 이걸 해줘야 canvas 에 renderer 가 생기나봄. 이걸 해주지 않으면 에러뜸 - AttributeError: 'FigureCanvasAgg' object has no attribute 'renderer'.
# grab the pixel buffer and dump it into a numpy array
X = np.array(canvas.renderer.buffer_rgba())

# now display the array X as an Axes in a new figure
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, frameon=False)
ax2.imshow(X)
plt.show()
