import json

COCOformated_anno_json_pathj = "./anno_testj/keypoint30over40pano.json"

def use_partial_points(original_anno_json_path, output_path, *select_opt):
    """
    (제작일: 2020년 4월.)
    어노테이션정보들어있는 json파일을 조금 변환하고싶을때 쓰기위해 내가 만든 함수.
        - 현재 기본적으로 임플에 6개 키포인트 어노테이션 해놨는데, 이중 일부만 가지고 트레이닝/테스팅 해보고싶을경우 사용하기 위함.
        - 예: 6개중에서 좌우측 본레벨포인트만 (총 2개) 사용해보고싶을때.
        - 물론 이렇게 해주면 cfg설정해줄때 키포인트 갯수도 그에맞게 바꿔줘야겠지.
    Args:
        original_anno_json_path (str): 어노테이션정보담긴 json파일을 경로. 지금상황에선 COCOformated_anno_json_pathj를 넣어줘야겠지.
        output_path (str): 수정된 어노테이션json파일을 넣어줄 경로.
        *select_opt (*args): 0,1,2,3,4,5중에서 선택해서 입력. 어떤 포인트들만 고를지(나머지포인트들은 없애버림) 선택하는 옵션값.
                            순서는 "boneright", "boneleft", "apexright", "apexleft", "topright", "topleft" 순서임(어노테이션파일상의 순서가 이러함).
                            즉, 0,1를 넣으면 br,bl만 선택. 4,5을 넣으면 tr,tl만 선택. 0,1,4,5넣으면 br,bl,tr,tl만 선택. 뭐 이런식.
    하는일:
        첫째인풋인자으로 알려준 기존json파일의 정보에서, 셋째인풋인자로알려준 키포인트들만 남기고 다른 키포인트는 없애버린 뒤, 둘째인풋인자로알려준 아웃풋경로에다가 수정된 json파일을 만들어줌. 
    Returns:
        리턴값 없음.
    """

    # i. json파일의 내용을 파이썬 객체로 만듦(deserialize).
    with open(original_anno_json_path) as f:
        ori_anno = json.load(f)


    # i. select_opt값에따라 ori_anno의 밸류들을 새로 바꿔서 넣어줌.

    ## "categories"의
    #### "keypoints"를 바꿔줌.
    ori_anno["categories"][0]["keypoints"] = [ori_anno["categories"][0]["keypoints"][i] for i in select_opt]
    #### "keypoint_colors", "skeleton" 삭제.
    del ori_anno["categories"][0]["skeleton"]
    del ori_anno["categories"][0]["keypoint_colors"]

    ## "annotations"의
    #### "keypoints", "num_keypoints" 를 바꿔줌.
    for _, each_anno in enumerate(ori_anno["annotations"]):
        newKeypointsList = []
        for i in select_opt:
            for kp_val in each_anno["keypoints"][3*i:3*i+3]:
                newKeypointsList.append(kp_val)
        each_anno["keypoints"] = newKeypointsList
        each_anno["num_keypoints"] = len(select_opt)
   

    # 이것만으로 다 됐는데, "events"값들 필요도없는데 넘 장황하게 많아서 다 지워줌.
    for imgdict in ori_anno["images"]:
        del imgdict["events"]
    for annodict in ori_anno["annotations"]:
        del annodict["events"]
    
    # 두번째 인풋인자로 알려준 저장할 경로에다가, modified_annoj.json 이라는 이름으로, 변경된 json파일 저장함.
    with open(output_path+'/modified_annoj.json', 'w') as f:
        json.dump(ori_anno, f)


use_partial_points(COCOformated_anno_json_pathj, "./anno_testj" ,0,1,4,5)