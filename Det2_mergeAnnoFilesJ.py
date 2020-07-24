# (제작일: 2020.04.19. 일요일.)
# COCO format의 annotation정보담긴 여러 json파일들을 하나의 파일로 합쳐주는 함수.

import json, os

def merge_anno_files(annofiles_path, out_path_with_filename):
    """
    (제작일: 2020.04.19.일욜.)
    COCO format의 annotation정보담긴 여러 json파일들을 하나의 파일로 합쳐주는 함수.
    Args:
        annofiles_path: COCO형식의어노테이션정보담긴 json파일들이 있는 경로.
        out_path_with_filename: 합쳐진 하나의 json파일 저장할 경로.
    하는일:
        - 여러 어노테이션json파일들을 하나의파일로 합쳐서 out_path_with_filename 의 경로&파일명에 저장해줌.
        - 만약 각 json파일에서 이미지id값이 겹친다든지 하는 충돌이 발생하면, 알려줌. 
    Returns:
        리턴값 없음.
    """
    # 첫번째인자로넣어준 경로의 모든 파일명들&폴더명들(스트링)이 담긴 리스트.
    all_list = os.listdir(annofiles_path)
    # 그 중 ".json"으로 끝나는 파일명만 담은 리스트.
    jsonfile_list = [name for name in all_list if ".json" in name]
    print('list of filenames that contains ".json":', jsonfile_list)
    print('above files will be merged into one json file.')

    # 만약 jsonfile_list의 원소가 0개 또는 1개일 경우.
    if len(jsonfile_list) == 0:
        raise ValueError('there is no json file!')
    if len(jsonfile_list) == 1:
        print('there is only one json file! no need to merge! j')
        return

    # jsonfile_list의 원소가 2개이상일 경우.
    ## 첫번째 파일을 deserialize.
    filepath = os.path.join(annofiles_path, jsonfile_list[0])
    with open(filepath) as f:
        anno1 = json.load(f)

    ## jsonfile_list의 두번째~마지막 파일을 deserialize하여 순차적으로 [첫번째파일을 deserialize한것]과 합침.
    ## 이때 merge_two_anno_files함수 사용.
    for name in jsonfile_list[1:]:
        filepath = os.path.join(annofiles_path, name)
        with open(filepath) as f:
            anno2 = json.load(f)
        anno1 = merge_two_anno_obj(anno1, anno2)
    
    with open(out_path_with_filename, 'w') as f:
        json.dump(anno1, f)



def merge_two_anno_obj(anno1, anno2):
    """
    (제작일: 2020.04.19.일욜.)
    Args:
        anno1, anno2: 하나로 합쳐줄 두 어노테이션 객체(dictionary아니면 dictionary-like라고 볼수잇겟지? 암튼 json파일로부터 deserialize해서 만들어준).
    Returns:
        merged annotation object (dictionary 또는 dictionary-like 쯤 되는).
    """

    # check if there is same image id. - 두 옵젝에 혹시 같은 image id가 있진 않은지 체크하는부분. -> 작동 잘 됨.
    anno1_imgid_list = [imginfo["id"] for imginfo in anno1["images"]] # ex: [351, 352, 353, 354, ...]
    anno2_imgid_list = [imginfo["id"] for imginfo in anno2["images"]]
    anno1_imgid_set = set(anno1_imgid_list)
    for i in anno2_imgid_list:
        if i in anno1_imgid_set:
            raise ValueError('two different annotation json files have at least one same image id!!! j')
    
    # check if the values of "categories" are same. - 두 옵젝의 "categories"리스트가 동일한지 체크하는 부분. 머 걍 내가 대충 한거라 허접한방법일수도잇고 완전하지못할수도있음.
    anno1_category_list = anno1["categories"]
    anno2_category_list = anno2["categories"]
    ## first, check the number of elements in both "categories" list.
    if len(anno1_category_list) != len(anno2_category_list):
        raise ValueError('two different annotation json files have different number of categories!!! j')    
    ## second, check if there is any different category in two objects. - 참고로,해보진않앗지만, 위의 리스트는 원소들이 딕셔너리기때문에, 위의 리스트를 set으로 만드는건(더 빨리 검색하기위한) 안될듯. 왜냐면 딕셔너리는 non-hashable? 해서 딕셔너리를 담고있는 리스트는 set으로 만들수없다고 어디서 봤음. 
    ## 참고로, 바로위에서 양쪽 카테고리 리스트의 원소갯수가 같은지 체크했기때매 한쪽리스트에서 포문돌려서 다른리스트랑 비교하기만 하면 될거임(반대로 후자 리스트에서 전자 리스트로 비교하는건 안해도될거다이거지. 만약 원소갯수 다르면 반대로도 해야겠지만.).
    ## 참고로, 에러메시지에도 내가 적어놨지만, 카테고리가 다르다고해서 합치면 안되는건 아님. 합쳐도 되는데, 일단은 카테고리 동일할때만 작동하도록 해놓은것뿐임. 즉, 안돼서 체크하는게 아니고, 사용자의 실수를 방지하려는 의도임. - 혹시나 내가(사용자가), 합치려고의도하지않았던 파일들을 실수로 합치려 시도할지도 모르니 그럴경우를 대비해서 알려주는 역할 정도일 뿐임.
    ### i. Q: 2020.05.15. 위엔 내가써논말인데 왜저렇게써논거지? 왜 카테고리가 달라도 합쳐도 된다는거지??? 아. 진짜로 다른 카테고리(예: 강아지,고양이)를 말햇던건가보네.
    ###  근데, 똑같은 임플이라서 같은카테고리로 분류해야하는데, 어노테이션프로그램이 어쩌다보니 예전에 어노테이션할때는 카테고리id를 1로해줫는데 다음에 어노테이션한것에선 카테고리id를 2로해줫다 뭐 이런상황이라면?? 그런상황은 어노테이션 프로그램의 잘못이지. 잘 확인하자.

    for i in anno1_category_list:
        if i not in anno2_category_list:
            raise ValueError('two different annotation json files have at least one different pair of categories!!! If you wanna merge annotation files that have different categories, you can do it by modifying this function a little bit, but as a default it is considered that all annotation files have the same categories. j')
       
    # check if there is same annotation id. - 두 옵젝에 혹시 같은 annotation id가 있진 않은지 체크하는부분. 
    anno1_annoid_list = [annoinfo["id"] for annoinfo in anno1["annotations"]] # ex: [562, 563, 564, 565, ...]
    anno2_annoid_list = [annoinfo["id"] for annoinfo in anno2["annotations"]]
    anno1_annoid_set = set(anno1_annoid_list)
    for i in anno2_annoid_list:
        if i in anno1_annoid_set:
            raise ValueError('two different annotation json files have at least one same annotation id!!! j')


    # 만약 두 옵젝에 같은 image id도 없고, "categories"리스트도 동일하고, 같은 annotation id도 없다고 판단되면, merge 시행!!
    merged_anno = {
        "images": anno1["images"] + anno2["images"],
        "categories": anno1["categories"],
        "annotations": anno1["annotations"] + anno2["annotations"],
    }

    return merged_anno


# 호출예시.
# merge_anno_files("C:/Users/starriet/Desktop/pa_keypointj_upper_merged/train", "C:/Users/starriet/Desktop/pa_keypointj_upper_merged/train/pa_kp_anno_upper_merged.json")
# merge_anno_files("C:/Users/starriet/Desktop/pa_keypointj_upper_merged", "C:/Users/starriet/Desktop/pa_keypointj_upper_merged/train/pa_kp_anno_upper_merged.json")
# merge_anno_files(r"C:\Users\starriet\Desktop\pa_keypointj_upper_merged", r"C:\Users\starriet\Desktop\pa_keypointj_upper_merged\pa_kp_anno_upper_merged_until3-47over111.json")
# merge_anno_files(r"C:\Users\starriet\Desktop\pa_keypointj_upper_merged", r"C:\Users\starriet\Desktop\pa_keypointj_upper_merged\pa_kp_anno_upper_merged_until3-102over111.json")
merge_anno_files(r"C:\Users\starriet\Desktop\pa_keypointj_lower_merged", r"C:\Users\starriet\Desktop\pa_keypointj_lower_merged\pa_kp_anno_lower_merged_until2-61over103.json")
