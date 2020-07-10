import numpy as np

bbox = [100,200,130,270]
# bbox = (100,200,130,270)
crop_size = (80,40) # h,w (tuple)
image_size = (400,500) # h,w (tuple)
print('crop_size:',crop_size)
crop_size = np.asarray(crop_size, dtype=np.int32)
print('crop_size to np.assaray:',crop_size)



center_yx = (bbox[1] + bbox[3]) * 0.5, (bbox[0] + bbox[2]) * 0.5
print('center_yx:',center_yx)
# print('type of center_yx:',center_yx.__class__)
print(np.ceil(center_yx).astype(np.int32))


min_yx = np.maximum(np.floor(center_yx).astype(np.int32) - crop_size, 0)
print('min_yx:',min_yx)
max_yx = np.maximum(np.asarray(image_size, dtype=np.int32) - crop_size, 0)
print('max_yx:',max_yx)
max_yx = np.minimum(max_yx, np.ceil(center_yx).astype(np.int32))
print('max_yx:',max_yx)

y0 = np.random.randint(min_yx[0], max_yx[0] + 1)
x0 = np.random.randint(min_yx[1], max_yx[1] + 1)
print('y0,x0:',y0,x0)