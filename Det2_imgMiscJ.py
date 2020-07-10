from skimage import io, img_as_float
from matplotlib import pyplot as plt
import numpy as np

import os

# i. 흑백이미지 예시코드.
# image = io.imread('http://i.stack.imgur.com/Y8UeF.jpg')
# print(image.shape)
# print(np.mean(image))

# i. 칼라이미지 예시코드.
# image = io.imread('./testImgDir/sea1.jpg')  # i. scikit-image use RGB (cf. opencv use BGR).
# print(image.shape)
# print(np.mean(image))
# print(np.mean(image, axis=(0,1)))
# r = image.copy(); g = image.copy(); b = image.copy()
# r[:,:,1] = 0; r[:,:,2] = 0
# g[:,:,0] = 0; g[:,:,2] = 0
# b[:,:,0] = 0; b[:,:,1] = 0
# io.imshow(r)
# plt.show()
# io.imshow(g)
# plt.show()
# io.imshow(b)
# plt.show()


img_dir = r'C:\Users\starriet\Desktop\pa_keypointj_upper_merged\train'
allfilename_list = os.listdir(img_dir)
# print('j) allfilenames:',allfilename_list)
imgfilename_list = [fn for fn in allfilename_list if (('.jpg' in fn) or ('.png' in fn))]
# print('j) only imgfilenames:',imgfilename_list)

tot_mean_list = []
perChannel_mean_list = []
for imgfilename in imgfilename_list:
    img_path = os.path.join(img_dir, imgfilename)
    image = io.imread(img_path)
    # print('j) image shape:', image.shape)
    tot_mean_list.append(np.mean(image))
    perChannel_mean_list.append(np.mean(image, axis=(0,1)))
tot_mean_list = np.array(tot_mean_list)
perChannel_mean_list = np.array(perChannel_mean_list)
print('j) total {} img files were calculated...'.format(len(imgfilename_list)))
print('j) tot_mean_list shape:{}  perChannel_mean_list shape:{}'.format(tot_mean_list.shape, perChannel_mean_list.shape))
print('j) total mean:',np.mean(tot_mean_list))
print('j) total std:',np.std(tot_mean_list))
print('j) per channel(RGB) mean:',np.mean(perChannel_mean_list, axis=0))
print('j) per channel(RGB) stds:',np.std(perChannel_mean_list, axis=0))
# print('j) tot_mean_list:', tot_mean_list)
# print('j) perChannel_mean_list:', perChannel_mean_list)

# image = io.imread(r'C:\Users\starriet\Desktop\pa_kp_val_36over122_anno2\20200603_0.jpg')
# print(image.shape)
# print(np.mean(image)) # i. 이렇게하면 모든원소들의 평균.
# print(np.mean(image, axis=(0,1))) # i. 이렇게하면 각 채널(R,G,B)별 평균 계산됨.
