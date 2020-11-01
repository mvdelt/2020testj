# i. 테스트해본거. 잘 작동.
import os, torch, cv2
PA_dir = r'C:\Users\starriet\Desktop\박사논문\20200724sndh\20200724sndh_PA_upper'
PA_filenames = [i for i in os.listdir(PA_dir) if os.path.isfile(os.path.join(PA_dir, i)) and not i.endswith('.json') and not i.endswith('.txt')]           
print(len(PA_filenames))
# print(PA_filenames)
img_path = os.path.join(PA_dir, PA_filenames[0])
print(img_path) # 참고: s.path.join 의 리턴 type 은 str.

from skimage import io
img_arr = io.imread(img_path)
cv2.imshow('img_arr', img_arr)
cv2.waitKey(0)
print(f'type img_arr: {type(img_arr)}') # <class 'numpy.ndarray'>
print(f'shape img_arr: {img_arr.shape}') # (1404, 1876, 4)

img_tensor = torch.from_numpy(img_arr)
# print(f'img_tensor: {img_tensor}')

print(f'type img_tensor: {type(img_tensor)}') # <class 'torch.Tensor'>
print(f'size() img_tensor: {img_tensor.size()}') # torch.Size([1874, 1404, 3])