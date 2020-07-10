import numpy as np
import matplotlib.pyplot as plt
import matplotlib

fig, ax = plt.subplots()
print('ax:',ax)

# create a rectangle instance
rect = matplotlib.patches.Rectangle((1, 1), width=5, height=12)

# by default the axes instance is None
print('rect.axes:',rect.axes) # None

# and the transformation instance is set to the "identity transform"
print('rect.get_transform():',rect.get_transform()) # <Affine object at 0x13695544>

# now we add the Rectangle to the Axes
ax.add_patch(rect)

# and notice that the ax.add_patch method has set the axes instance
print('rect.axes:',rect.axes) # Axes(0.125,0.1;0.775x0.8)

# and the transformation has been set too
print('rect.get_transform():',rect.get_transform()) # <Affine object at 0x15009ca4>

# the default axes transformation is ax.transData
print(ax.transData) # <Affine object at 0x15009ca4>

# notice that the xlimits of the Axes have not been changed
print(ax.get_xlim()) # (0.0, 1.0)

# but the data limits have been updated to encompass the rectangle
print(ax.dataLim.bounds) # (1.0, 1.0, 5.0, 12.0)

# we can manually invoke the auto-scaling machinery
ax.autoscale_view()

# and now the xlim are updated to encompass the rectangle
print(ax.get_xlim()) # (1.0, 6.0)

# we have to manually force a figure draw
ax.figure.canvas.draw() # i. 이게 뭐하는거지????? -> 아. 조금 알듯함.

##########################
# i. 위에서 canvas.draw() 안해주면 이거 작동 안하네.
buffj = ax.figure.canvas.buffer_rgba()
arrj = np.asarray(buffj)
print(arrj)

# ...and pass it to PIL.
from PIL import Image
im = Image.fromarray(arrj)
im.show()
##########################

# plt.show()