# 제작일: 2020.05.15.금요일.
# 기존 어노테이션파일에서, 모델2를 트레이닝시킬수있는 어노테이션파일과 트레이닝이미지들을 만들어주는 함수.

def makeAnnoAndCropForModel2(oriAnno_path,oriData_path,annoForModel2_path,croppedForModel2_path):
    """
    기존 어노테이션파일에서, 모델2를 트레이닝시킬수있는 어노테이션파일과 트레이닝이미지들을 만들어주는 함수.
    - 모델1,2연결시키는 방식 사용할때, 모델1에 넣어주는 인풋이미지(현재는 파노)를 대상으로 어노테이션해준 정보를 가지고,
      모델2를 트레이닝시킬 수 있는 어노테이션파일(크롭된이미지를 대상으로한 어노테이션) 및 트레이닝이미지들(크롭된이미지들)을 만들어주는 함수.
    Args:
        oriAnno_path(str): 기존의 어노테이션json파일의 경로. (모델1이 요걸로 학습/평가. 즉, 파노대상 어노테이션정보.)
        oriData_path(str): 기존의 데이타(파노이미지파일들) 경로. (모델1이 요걸로 학습/평가.). '데이타'라는건 학습데이타일수도잇고 평가용데이타일수도잇고.
        annoForModel2_path(str): 만들어준 (모델2를위한)어노테이션json파일 저장경로.
        croppedForModel2_path(str): 크롭해준 (모델2를위한)데이타(크롭된이미지들) 저장경로.
    하는일:
        위에 설명해놓은대로임.
    Returns:
        일단은 없음.
    제작일: 2020.05.15.금요일.
    """

    import json, cv2, os, copy
    from PIL import Image

    # i. oriAnno_path 로부터 기존어노테이션json파일의 내용을 읽어들임. - json파일의 내용을 파이썬 객체로 만듦(deserialize).
    with open(oriAnno_path) as f:
        oriAnno = json.load(f)

    # i. 모델2를위한 새로운 어노테이션정보 담을 딕셔너리.
    newAnno = {}
    newAnno["images"] = [] # list[dict]
    newAnno["categories"] = [] # list[dict]
    newAnno["annotations"] = [] # list[dict]


    # - newAnno의 "categories"(리스트)에 원소 추가. - "images"랑 "annotations"는 아래의 for loop 에서 추가해줌.
    for ori_cate in oriAnno["categories"]:
        new_cate = copy.deepcopy(ori_cate)
        newAnno["categories"].append(new_cate)

    # i. (파노상의) 각 annotation 1개에 대해서,
    for ori_ann in oriAnno["annotations"]:
        # 값들 예시.
        # ori_ann["id"] - ex) 817
        # ori_ann["image_id"] - ex) 610
        # ori_ann["bbox"] - ex) [ 1127, 316, 53, 83 ] 아마 x0,y0,w,h겟지? COCO데이터형식 설명 보면 나오겟지만.
        # ori_ann["category_id"] - ex) 4
        # ... 뭐 이런식임. 걍 어노테이션json파일(COCO데이터셋형식으로된거.내가계속이용해오고있는.) 함 열어보면 다 나오지.

        # ori_ann["bbox"] 정보를이용해서 [파노이미지파일]을 크롭해서 저장하면 됨.
        # - 이때 파노이미지파일명은 ori_ann["image_id"]로 알수잇음.
        panoImgFileName = imgId2imgFileName_COCOj(ori_ann["image_id"], oriAnno)

        # - 파노이미지파일명으로 이미지를 불러와서 어레이로 변환.        
        panoimg_arr = cv2.imread(os.path.join(oriData_path, panoImgFileName))
        # - ori_ann["bbox"] 정보를이용해서 panoimg_arr 를 크롭하는데, 가로세로 모두 100픽셀씩(100행or100열) 크게 크롭해줌(내코랩플젝에서 내가 그렇게 하고잇고 그정도면 괜찮은크기같음).
        croppedimg_arr = panoimg_arr[ori_ann["bbox"][1]-100 : ori_ann["bbox"][1]+ori_ann["bbox"][3]+100 , ori_ann["bbox"][0]-100 : ori_ann["bbox"][0]+ori_ann["bbox"][2]+100]
        # - 크롭한 어레이를 이미지로 저장.
        if not os.path.exists(croppedForModel2_path):
            os.makedirs(croppedForModel2_path)  
        croppedimg = Image.fromarray(croppedimg_arr)
        croppedimg.save(os.path.join(croppedForModel2_path, "{}_gtCropped_gtAnnoId{}.jpg".format(panoImgFileName, ori_ann["id"])))

        # 이제, 모델2를위한 어노테이션 만들어주자.(위에서 newAnno 라는 이름으로 텅빈 딕셔너리랑 그안에 텅빈 리스트들 만들어줬지. 거기다가 집어넣을거임.)
        # - newAnno의 "images"(리스트)에 원소 추가.
        new_img = {}
        new_img["id"] = int(str(ori_ann["image_id"]) + "000" + str(ori_ann["id"])) # i. gt크롭한 이미지의 id는, [파노의 이미지id + 000 + 어노테이션의 id] 로 정해줬음.
        new_img["file_name"] = "{}_gtCropped_gtAnnoId{}.jpg".format(panoImgFileName, ori_ann["id"])
        newAnno["images"].append(new_img)

        # - newAnno의 "annotations"(리스트)에 원소 추가.
        new_ann = {}
        new_ann["id"] = int(str(ori_ann["image_id"]) + "111" + str(ori_ann["id"])) # i. gt크롭한 이미지상의 어노테이션id는, [파노의 이미지id + 111 + 어노테이션의 id] 로 정해줬음.
        new_ann["img_id"] = int(str(ori_ann["image_id"]) + "000" + str(ori_ann["id"]))
        new_ann["category_id"] = ori_ann["category_id"]
        
        ori_ann_seg_list = ori_ann["segmentation"][0] # i. segmentation은 list[list]로 되어잇는데, 일단 걍 첫번째원소(첫번째리스트) 꺼내와봄. 여기에 여러개의원소(여러개의리스트)들어가잇는경우는 일단 나중에 다시 생각.
        seg_new_x_list = [v-(ori_ann["bbox"][0]-100) for i,v in enumerate(ori_ann_seg_list) if i%2==0]
        seg_new_y_list = [v-(ori_ann["bbox"][1]-100) for i,v in enumerate(ori_ann_seg_list) if i%2==1]
        seg_new_xy_list = []
        for x,y in zip(seg_new_x_list, seg_new_y_list):
            seg_new_xy_list.append(x)
            seg_new_xy_list.append(y)
        new_ann["segmentation"] = [seg_new_xy_list] # i. 다시 리스트 안에 넣어줌. 원래 형식에 맞춰서.        

        new_ann["bbox"] = [100, 100, ori_ann["bbox"][2], ori_ann["bbox"][3]] # i. bbox 의 3,4번째 값은 w,h니까 단순히 원점위치가 바뀌는 좌표변환에서는 값이 그대로지.

        new_ann["iscrowd"] = ori_ann["iscrowd"]
        new_ann["width"] = ori_ann["bbox"][2]+200
        new_ann["height"] = ori_ann["bbox"][3]+200 # i. 왜 '어노테이션'의 w,h가 전체 이미지의 w,h랑 똑같은가 생각해보니(coco_annotator로 어노테이션해준 어노테이션json파일 열어보면 그렇게 돼잇음), 어쨋든 전체이미지상에 어노테이션하는거자나. 전체이미지의 모든 픽셀에 대해 어노테이션이 맵핑되어야하는거자나. 단지 전체이미지중에 특정부분만 어노테이션이 될 뿐이지. 어노테이션이 되지 않은 부분도 어노테이션 정보에 속하는거자나.
        
        ori_ann_kp_list = ori_ann["keypoints"]
        kp_new_x_list = [v-(ori_ann["bbox"][0]-100) for i,v in enumerate(ori_ann_kp_list) if i%3==0]
        kp_new_y_list = [v-(ori_ann["bbox"][1]-100) for i,v in enumerate(ori_ann_kp_list) if i%3==1]
        kp_info_list = [v for i,v in enumerate(ori_ann_kp_list) if i%3==2] # i. 얜 바꿀필요없으니 그대로.
        kp_new_xyinfo_list = []
        for x,y,info in zip(kp_new_x_list, kp_new_y_list, kp_info_list):
            kp_new_xyinfo_list.append(x)
            kp_new_xyinfo_list.append(y)
            kp_new_xyinfo_list.append(info)
        new_ann["keypoints"] = kp_new_xyinfo_list
        new_ann["num_keypoints"] = ori_ann["num_keypoints"]
        newAnno["annotations"].append(new_ann)

    # i. 자, 이제 newAnno가 완성되었으니, json파일로 저장해줌.
    with open(annoForModel2_path, 'w') as f:
        json.dump(newAnno, f)
    
    print('j) finished well... I guess... lol')


def imgId2imgFileName_COCOj(imgId, anno):
    """
    설명:
        이미지id와 어노테이션객체를 인풋으로 넣으면 이미지파일명을 리턴하는 맵퍼 함수(COCO 데이터셋 형식의 어노테이션객체일때 사용가능한 함수).
    Args:
        imgId: 이미지id
        anno: 어노테이션 객체(딕셔너리겟지)
    하는일:
        설명에 나와있음.
    Returns:
        imgFileName(str): 어노테이션객체에 들어있는 이미지파일명.
    제작일: 2020.05.15.금요일.
    """
    eachMapDict_list = [{img["id"]: img["file_name"]} for img in anno["images"]]
    mapDict = {}
    for d in eachMapDict_list:
        mapDict.update(d)
    return mapDict[imgId]


# i. 호출!!!
oriAnno_path = r'C:\Users\starriet\Desktop\pano_kp_upper\train\pano_kp_uplow.json'
oriData_path = r'C:\Users\starriet\Desktop\pano_kp_upper\train'
annoForModel2_path = r'C:\Users\starriet\Desktop\pano_kp_upper\train\forModel2\newAnnoForModel2.json'
croppedForModel2_path = r'C:\Users\starriet\Desktop\pano_kp_upper\train\forModel2'
makeAnnoAndCropForModel2(oriAnno_path, oriData_path, annoForModel2_path, croppedForModel2_path)
