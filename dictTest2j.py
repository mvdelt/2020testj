import numpy as np


names = ("br","bl","ar","al","tr","tl")
# names = ("bonelevel_upper",)

keypoint_flip_map = (("br","bl"),("ar","al"),("tr","tl"))
# keypoint_flip_map = ()

kp_fm_dict = dict(keypoint_flip_map)
print(kp_fm_dict)

kp_fm_dict.update({v: k for k, v in kp_fm_dict.items()})
print(kp_fm_dict)


flipped_names = [i if i not in kp_fm_dict else kp_fm_dict[i] for i in names]
print(flipped_names)


flip_indices = [names.index(i) for i in flipped_names]
print(flip_indices)



# i. just for testing. -> 아하! 요렇게 해보니 이제 알겠네!! IndexError: index 31 is out of bounds for axis 0 with size 4 이렇게 뜨네!! 요 에러 문장에서 index 'n' 에서 'n'이 뭘말하는지 몰랐는데, 이제 알겠음.
# 아래에서 요 flip_indices를 넘파이 어레이로 바꾼담에 그걸 keypoints[요기, :] 요기다가 넣어주자나. 근데 keypoints라는 어레이는 axis 0에서 사이즈가 4뿐인데 31이란 값의 인덱스를 찾을라니까 index 31 is out of bounds for axis 0 with size 4 라고 에러가 뜨는거지! 이해완료.
# flip_indices = [1,0,31,2,51,4]


keypoint_hflip_indices = np.asarray(flip_indices)
print('keypoint_hflip_indices:',keypoint_hflip_indices)



# 예를들어 키포인트가 1개라서 아래와같다고쳐보자.(앞에두개가 x,y, 뒤에숫자는 COCO형식의 0/1/2 알지?). 키포인트가 여러개면, 예를들어 3개면 [333,444,2,555,666,2,777,888,2] 이런식으로 됏엇지.
keypoints = [111,112,2,222,223,2,333,334,2,444,445,2,555,556,2,666,667,2,]

# (N*3,) -> (N, 3)
keypoints = np.asarray(keypoints, dtype="float64").reshape(-1, 3)
print(keypoints)

keypoints = keypoints[keypoint_hflip_indices, :]
print(keypoints)