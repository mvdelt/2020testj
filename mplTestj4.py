# i. 튜토리얼 굿: https://matplotlib.org/tutorials/intermediate/artists.html

import numpy as np
import matplotlib.pyplot as plt # i. pyplot 이 모듈명임. pyplot.py 파일인거임.
import matplotlib

fig = plt.figure()
# fig2 = plt.figure() # i. fig2도 만들어주면 저밑에서 plt.show() 했을때 figure 1, figure 2 이렇게 두개가 뜸(창이 2개가 뜸).
ax1 = fig.add_subplot(231) # i. 211 은 2,1,1 과 동일. 신택틱슈거인듯 걍 쉼표빼도되는. 211은 row 2개, column 1개 의 그리드에서 1번째 셀이라는 뜻.
ax2j = fig.add_subplot(235)
print(ax2j.patch) # i. Rectangle(xy=(0, 0), width=1, height=1, angle=0) - 튜토리얼에나온대로네.
ax2j.zorder = 10
rectj = matplotlib.patches.Rectangle((0,0),0.7,0.7,edgecolor="red",facecolor="blue",alpha=0.7) # i. 걍 plt.Rectangle 이라고 해도 똑같은것같음.
ax2j.add_patch(rectj)

ax2j.patch.set(facecolor="red", alpha=0.5, edgecolor="blue", width=1.5, linewidth = 3)
rectj.set(facecolor="black")
print('ax2j.patches:',ax2j.patches) # i. add_patch 로 rectj 를 추가해줬는데 두개 안뜨고 하나만 뜨네.
print('fig.patches:',fig.patches)

print(ax2j.patch)
# ax1_for_fig2j = fig2.add_subplot(347)
fig.subplots_adjust(top=0.8) # i. 크기 조정.
ax1.set_ylabel('volts')
ax1.set_title('a sine wave')

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax1.plot(t, s, color='blue', lw=2)

ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.2])
n, bins, patches = ax2.hist(np.random.randn(1000), 50, facecolor='yellow', edgecolor='skyblue')
ax2.set_xlabel('time (s)')

print('fig.axes:',fig.axes)

for ax in fig.axes:
    ax.grid(True)

plt.show() # i. 만들어준 모든 figure 들을 보여주는듯.