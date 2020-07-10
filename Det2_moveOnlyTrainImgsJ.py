# 트레이닝시킬 이미지들만 잔뜩 모아놓은 폴더에서, 어노테이션파일을 참고하여 실제로 어노테이션 완료된 상태의 이미지들만 골라서,
# 지정해준 폴더로 복사해주는 함수.

import json, os, shutil

def moveOnlyTrainImgs(alltraindata_dir, annofile, copyhere_dir):
    """
    Args:
        alltraindata_dir: 트레이닝시킬 이미지들 잔뜩 모아놓은 폴더의 경로. 아직 어노테이션 완료 안한 이미지들도 다같이 있음.
        annofile: 어노테이션정보담긴 json파일의 경로.
        copyhere_dir: 어노테이션정보를 기반으로, 실제로 어노테이션 된 이미지들만 복사해서 붙여넣기해줄 폴더의 경로.
    하는일: alltraindata_dir에서, annofile의 어노테이션정보를 기반으로, 어노테이션 완료된 이미지들만 복사해서 copyhere_dir에다가 붙여넣기해줌.
    Returns:
        리턴값 없음.
    """
    # 필수는 아닌 부분.
    alltraindata_list = os.listdir(alltraindata_dir)
    alltraindata_set = set(alltraindata_list)

    with open(annofile) as f:
        anno = json.load(f)
    # 핵심.
    annotated_filename_list = [imginfo["file_name"] for imginfo in anno["images"]]

    for annotated_filename in annotated_filename_list:
        # 필수는 아닌 부분.
        if annotated_filename not in alltraindata_set:
            raise ValueError('something is wrong!!! cannot find the file(of which information was taken from the given annotation json file) in alltraindata_dir!!! j')

        srcfilepath = os.path.join(alltraindata_dir, annotated_filename)
        # 핵심.
        shutil.copy(srcfilepath, copyhere_dir)
    
    print('copy finished!! - from {}, only annotated imgs were copied to {}, based on information in {}. j'.format(alltraindata_dir, copyhere_dir, annofile))


# 호출예시.
# alltraindata_dir = r"C:\Users\starriet\Desktop\pa_keypointj_upper_merged\train_temp"
# annofile = r"C:\Users\starriet\Desktop\pa_keypointj_upper_merged\train_temp\pa_kp_anno_upper_merged.json"
# copyhere_dir = r"C:\Users\starriet\Desktop\pa_keypointj_upper_merged\train"
# moveOnlyTrainImgs(alltraindata_dir, annofile, copyhere_dir)

alltraindata_dir = r"C:\Users\starriet\Desktop\pa_kp_val\all_imgs"
annofile = r"C:\Users\starriet\Desktop\pa_kp_val\pa_keypoint_validation.json"
copyhere_dir = r"C:\Users\starriet\Desktop\pa_kp_val"
moveOnlyTrainImgs(alltraindata_dir, annofile, copyhere_dir)