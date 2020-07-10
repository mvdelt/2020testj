# i. 데이터셋중 일부만 사용하기위해 내가만들어준 함수.

import os, json

def del_nonexistimg_anno(original_anno_json_path, output_path_with_filename, train_imgs_path):
    """
    (제작일: 2020년 4월.)
    어노테이션정보담긴 json파일에서, 골라준 이미지들에 대한 어노테이션정보만 남기고 다른이미지들에대한 어노테이션정보들은 다 삭제하는 함수. 상악임플 하악임플 나누려고 만들었음.
        - 기존의 상하악 다 한뭉탱이인 데이타셋 이용하지만, 그중 상악임플 또는 하악임플만 고르다든지 하는 식으로 일부 데이터들만 사용하고싶을경우 요함수 이용하면됨.
        - 근데 수작업으로 원하는 이미지들을 골라주는건 해줘야댐.
        - 상악/하악임플 원하는 이미지만 골라서 폴더에 넣어준 뒤, 요 함수 작동시키면 어노테이션정보담긴json파일에서 폴더에 있는 이미지들에 대한 어노테이션정보만 남기고 나머지 이미지들의 어노테이션정보들은 삭제시킴.
    Args:
        original_anno_json_path: 어노테이션정보담긴 json파일의 경로(해당json파일의 파일명 포함).
        train_imgs_path: 트레이닝시키고자하는 이미지들이 있는 디렉토리의 경로. 이 디렉토리에 없는 이미지들에 대한 어노테이션들은 다 삭제되는거임(어노테이션정보담긴json파일에서).
    하는일:
        위 설명에 적어놨음.
    Returns:
        리턴값 없음.
    사용 예시:
        아래와 같이 호출.
        del_nonexistimg_anno(COCOformated_anno_json_pathj, COCOformated_anno_json_pathj, train_imgs_pathj)
    """

    exist_imgs_list = os.listdir(train_imgs_path)
    exist_imgs_set = set(exist_imgs_list) # i. set에 넣어주면 검색속도가 훨 빠르다함.

    # i. json파일의 내용을 파이썬 객체로 만듦(deserialize).
    with open(original_anno_json_path) as f:
        anno = json.load(f)



    # 아래에 코멘트아웃해논 코드 대신 요렇게 해줘서 성공.
    anno["images"][:] = [img_info for img_info in anno["images"] if img_info["file_name"] in exist_imgs_set]
    exist_img_id_list = [img_info["id"] for img_info in anno["images"]]
    exist_img_id_set = set(exist_img_id_list)
    anno["annotations"][:] = [anno_info for anno_info in anno["annotations"] if anno_info["image_id"] in exist_img_id_set]


    # 요부분 자료구조적으로 매우 느린 코드이고, 개선해야되나, 일단 당장 써먹어야하니 걍 이렇게 해놓음.
    # 주의!!!) 리스트A를 대상으로 for loop 돌리면서 리스트A에서 값 삭제하면, 한칸씩 땡겨지는 효과 발생!!->enumerate등을 사용해줘야함!!->또안되네;;머지;;작은예시에선됏는데;;        
    # for _, img_info in enumerate(anno["images"]):
    #     if img_info["file_name"] not in exist_imgs_set:
    #         # get img id of this non exist img, and delete its img info.
    #         nonexistimg_id = img_info["id"]
    #         anno["images"].remove(img_info)
            
    #         # find annotation of this non exist img, and delete it.
    #         for _, anno_info in enumerate(anno["annotations"]):
    #             if anno_info["image_id"] == nonexistimg_id:
    #                 anno["annotations"].remove(anno_info)


    # 이제 anno 수정완료되었으니, anno를 파일로 json파일로 serialize시켜서 지정 디렉토리에 넣어주면 됨.
    # 두번째 인풋인자로 알려준 저장할 경로에다가 변경된 json파일 저장함. 이렇게해주면 만약 동일한 경로&파일일 경우, overwrite됨.
    with open(output_path_with_filename, 'w') as f:
        json.dump(anno, f)
    
    # 함수의 끝.

# i. 호출! - 얜 걍 항상 호출해줘도 작동은 되지. 느려지는게 문제긴 하겠지만. - 요아래 호출 두개 다 작동 잘 됨. 두번째껀 절대경로 넣어주고 해봤는데 잘 됨.
# del_nonexistimg_anno("./anno_testj/pa_keypoint_annoj.json", "./anno_testj/pa_keypoint_annoj_modif.json", "./anno_testj")
# del_nonexistimg_anno("C:/Users/starriet/Desktop/pa_keypointj/train/pa_keypoint_annoj.json", "C:/Users/starriet/Desktop/pa_keypointj/train/pa_keypoint_annoj_annoforonlyexistimgs.json", "C:/Users/starriet/Desktop/pa_keypointj/train")