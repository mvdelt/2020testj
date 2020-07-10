# 어노테이션정보담긴 json파일의 "images"리스트에 이미지정보가 몇개 들어있나 세어주는 간단한 함수.

import json

def count_imgs(anno_file_path):
    """
    어노테이션정보담긴 json파일의 "images"리스트에 이미지정보가 몇개 들어있나 세어주는 간단한 함수.
    Args:
        anno_file_path: 어노테이션정보담긴 json파일의 경로(json파일의 파일명 포함).
    Returns:
        어노테이션정보담긴 json파일의 "images"리스트의 원소 갯수.(이미지정보가 몇개 들어있나 세어줌).        
    """
    with open(anno_file_path) as f:
        anno = json.load(f)
    
    return len(anno["images"])

# 호출 예시. 아래와같이 한 다음, print(imgN)으로 출력하면 됨.
# imgN = count_imgs("C:/Users/starriet/Desktop/pa_keypointj_upper_merged/train/pa_kp_anno_upper_merged.json")

# 근데 좀 짱나는게, 윈도우 탐색기에서 파일경로 복사해와서 여기 붙여넣으면, 백슬래시로 돼서 escape가 되나봄. 
# 해결법: 스트링 앞에 r을 붙여주면 뭐 노말스트링을 raw스트링으로 바꿔준다나? 암튼 일케하면 됨.
#        심지어, 백슬래시랑 포워드슬래시 섞어써도 됨!!!
# imgN = count_imgs(r"C:\Users\starriet\Desktop\pa_keypointj_upper_merged\train\pa_kp_anno_upper_merged.json")
# imgN = count_imgs(r"C:\Users\starriet\Desktop\pa_keypointj_upper_merged\train\pa_kp_anno_upper_merged_include_only4keypoints.json")
# imgN = count_imgs(r"C:\Users\starriet\Desktop\pa_kp_anno_upper_merged.json")
# imgN = count_imgs(r"C:\Users\starriet\Desktop\pa_keypointj_upper_merged\train\pa_kp_anno_upper_merged.json")
# imgN = count_imgs(r"C:\Users\starriet\Desktop\pa_keypointj_upper_merged\pa_kp_anno_upper_merged_until3-87over111.json")
# imgN = count_imgs(r"C:\Users\starriet\Desktop\pa_keypointj_upper_merged\train\pa_kp_anno_upper_merged_until3-102over111.json")
imgN = count_imgs(r"C:\Users\starriet\Desktop\pa_keypoint_validation.json")
# print(r"C:\Users\starriet\Downloads\pa_bbox_upper.json")
print(imgN,'- the number of images annotated in this json file.')


###############아래는 백슬래시를 포워드슬래시로 바꾸려고 찾아본건데, 결국 여기서도 앞에 r 붙여줘야되는듯;; 그니까 요건 별 의미없... 걍 요런함수도 잇다 참고만.###############
# import os
# # path = "C:\\temp\myFolder\example\\"
# path = r"C:\Users\starriet\Downloads"
# newPath = path.replace(os.sep, '/')
# print(newPath) # C:/Users/starriet/Downloads