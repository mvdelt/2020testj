# i. from matplotlib 3.2.1 doc.

# <CanvasAgg demo>
# - This example shows how to use the agg backend directly to create images, 
# which may be of use to web application developers who want full control over 
# their code without using the pyplot interface to manage figures, figure closing etc.

# Note
# It is not necessary to avoid using the pyplot interface in order 
# to create figures without a graphical front-end - simply setting the backend to "Agg" would be sufficient.

# In this example, we show how to save the contents of the agg canvas to a file, 
# and how to extract them to a string, which can in turn be passed off to PIL or put in a numpy array. 
# The latter functionality allows e.g. to use Matplotlib inside a cgi-script without needing to write a figure to disk.

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import numpy as np

fig = Figure(figsize=(5, 4), dpi=100)
# A canvas must be manually attached to the figure (pyplot would automatically
# do it).  This is done by instantiating the canvas with the figure as
# argument.
canvas = FigureCanvasAgg(fig)

# Do some plotting.
ax = fig.add_subplot(111)
ax.plot([1, 2, 3,4,5,66,7,8,9,55,100])

# Option 1: Save the figure to a file; can also be a file-like object (BytesIO,
# etc.).
# fig.savefig("test.png") # i. ->잘 작동함. 일단 코멘트아웃.

# Option 2: Retrieve a view on the renderer buffer...
canvas.draw()
buf = canvas.buffer_rgba() # i. canvas.renderer.buffer_rgba() 랑 동일.
# ... convert to a NumPy array ...
X = np.asarray(buf) # i. np.asarray 는 np.array 를 랩핑한것. 편의함수. np.array 에서 몇몇 옵션값 지정해줄뿐 사실상 거의 같음. 주된 차이는, np.array는 디폴트로 복사하게돼잇지만(복사안하게할수도잇음물론) np.asarray는 복사안하게되어잇음.
print(X.shape)
# print(X)
# ... and pass it to PIL.
from PIL import Image
im = Image.fromarray(X)
# Uncomment this line to display the image using ImageMagick's `display` tool.
# i. ->ImageMagick 이라는 이미지 관련 유명한 프로그램이 있나봄. 그거써서 출력할거면 요 im.show() 쓰지말란얘기지.
im.show()