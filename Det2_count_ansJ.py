# 어노테이션정보담긴 json파일의 "annotations" 리스트에 어노테이션정보가 몇개 들어있나 세어주는 함수.

import json

def count_ans(anno_file_path):
    """
    어노테이션정보담긴 json파일의 "annotations"리스트에 이미지정보가 몇개 들어있나 세어주는 간단한 함수.
    Args:
        anno_file_path: 어노테이션정보담긴 json파일의 경로(json파일의 파일명 포함).
    Returns:
        어노테이션정보담긴 json파일의 "annotations"리스트의 원소 갯수.(어노테이션정보가 몇개 들어있나 세어줌).        
    """
    with open(anno_file_path) as f:
        anno = json.load(f)
    
    try:
        return len(anno["annotations"])
    except TypeError: # i. 만약 anno가 COCO형식에서 'annotations'키의 밸류인 list[dict] 일 경우.
        return len(anno)

# num_ans = count_ans(r"C:\Users\starriet\Desktop\for_meanOKS\meanOKS2\cocoformatted_anlist_dt.json")
num_ans = count_ans(r"C:\Users\starriet\Desktop\for_meanOKS\meanOKS2\pa_keypoint_validation.json")
print(num_ans,'- the number of annotation(per 1 object)s in this json file.')


