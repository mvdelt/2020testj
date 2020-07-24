import cv2
import numpy as np

# img_path = r'C:\Users\starriet\1JUN\2020vision\2020testj\testImgDir\sea1.jpg'
# img_cv = cv2.imread(img_path)
img_cv = cv2.imread('./testImgDir/city1.jpg')

img_cv = cv2.resize(img_cv, (300,300) )

# img_arr = np.array(img)
# print(img_arr.shape)
cv2.imshow('windowName_j', img_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()