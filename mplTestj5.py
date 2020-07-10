"""
Simple demo of the imshow function.
"""
import matplotlib.pyplot as plt

imageArr = plt.imread('./testImgDir/city1.jpg')
# print(imageArr.__class__) # i. <class 'numpy.ndarray'>
# print(type(imageArr)) # i. <class 'numpy.ndarray'>

# fig, ax = plt.subplots() # i. 편의함수인듯. ('편의함수'란 표현은 내가쓴표현으로, 랩퍼펑션 등 편의성을 위해 좀더 상위레벨로 만들어준함수를 말하는거임.)

# i. 위의 편의함수대신 살짝 더 직접적으로(얘네도 아마 일종의 편의함수겟지만) 해주면 아래와같겟지.
fig = plt.figure()
# ax = fig.add_subplot(347) # i. 이렇게해줘도되고, 아래처럼 add_axes 로 axes 추가해줘도됨. Subplot도 결국 Axes 의 특별한 케이스일뿐임!! Subplot 은 Axes 의 서브클래스임.
# ax0 = fig.add_axes([0, 0, 0.1, 0.2]) # i. "... add_axes() method which takes a list of [left, bottom, width, height] values in 0-1 relative figure coordinates: ..."
ax1 = fig.add_axes([0, 0.1, 0.4, 0.2])
ax1_1 = fig.add_axes([0, 0.31, 0.4, 0.2])
# ax2 = fig.add_axes([0.1, 0, 0.5, 0.5])
# ax3 = fig.add_axes([0.25, 0.5, 0.5, 1])

return_val_of_imshowj = ax1.imshow(imageArr)
print(return_val_of_imshowj) # i. AxesImage(0,96;512x192) - 즉, imshow 는 튜토리얼설명대로 AxesImage 를 리턴함. 내(Det2기반)플젝에서 시각화할때 AxesImage 가 필요햇엇는데 이렇게 만들어주면 되겠네!!!
# ax.axis('off')  # clear x- and y-axes
plt.show()