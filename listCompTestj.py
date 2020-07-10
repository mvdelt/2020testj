# i. Detectron2 코드 관련 테스트.

import copy

num_images = 7

anchors_in_image = [[1,2,3],[4,5,6],[7,8,9]]

anchors = [copy.deepcopy(anchors_in_image) for _ in range(num_images)]

print(anchors)

