# 테스트할 이미지들 있는 폴더에 일단 이미지들 죄다 넣어놓고 요 함수 돌리면,
# 어노테이션 된 이미지들(트레이닝에 사용될 이미지들)은 다 삭제하고 어노테이션 안된 이미지들만 남겨주는 함수.

import os, json

def leaveOnlyTestImgs(annofile_path, testdir_path):
    """
    제작일: 2020.04.23.목욜 새벽1시.
    Args: 
        annofile_path: 어노테이션json파일의 경로. 파일명 포함.
        testdir_path: 테스트데이터들이 들어있는 디렉토리의 경로.
    하는일: 테스트데이터들이 있는 디렉토리에서, 어노테이션 된 이미지들(트레이닝에 사용될 이미지들)은 다 삭제하고 어노테이션 안된 이미지들만 남겨놓음.
    Returns:
        리턴값 없음.
    """

    print('annofile_path:',annofile_path)
    print('testdir_path:',testdir_path)

    testdir_list = os.listdir(testdir_path)

    with open(annofile_path) as f:
        anno = json.load(f)

    trainimg_filename_list = [imginfo["file_name"] for imginfo in anno["images"]]

    trainimg_filename_set = set(trainimg_filename_list)
    
    for testimg in testdir_list:
        if testimg in trainimg_filename_set:
            # delete testimg
            os.remove(os.path.join(testdir_path,testimg))
    
    # os.remove 작동햇나 함 체크하려고 써줘본거. 잘작동하면 요거 지울거임.
    testdir_list = os.listdir(testdir_path)
    for testimg in testdir_list:
        if testimg in trainimg_filename_set:
            raise ValueError('Error!!! removing files did not work correctly!!!! j')
    print('finished well! j')

# 호출예시.
leaveOnlyTestImgs(r"C:\Users\starriet\Desktop\pa_kp_up\pa_kp_anno_upper_merged.json", r"C:\Users\starriet\Desktop\pa_kp_up")

