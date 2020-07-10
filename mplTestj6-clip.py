import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.cbook as cbook

# i. test 용.
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure


imageArrj = plt.imread('./testImgDir/sea1.jpg')

fig, ax = plt.subplots() # i. 이렇게해서그런가 FigureCanvasAgg(fig) 에서 에러가 나네.
# figj = Figure()
# ax = figj.add_subplot(111)

im_AxesImagej = ax.imshow(imageArrj)
# patch = patches.Circle((1000, 500), radius=500, transform=ax.transData)
patch = patches.Circle((1000, 500), radius=500) # i. 오!!! transform=ax.transData 없으니 이상하게 되네!!!!!
im_AxesImagej.set_clip_path(patch)

# canvasj = FigureCanvasAgg(figj) # i. 이거 없어도 savefig 는 작동함.
# figj.savefig('./testImgDir/sea1_clipped2.jpg')



# ax.axis('off')
plt.show() # i. 아무것도 출력안됨. 내가만들어준 figj 는 plt 가 모르는 figure니까.