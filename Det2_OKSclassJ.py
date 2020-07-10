# i. 2020.06.23.화욜낮.

import json, os
import numpy as np

class OKS_j: 
    """
    (요 클래스 첫제작일: 2020.06.25.목욜오전. 요 클래스 안의 함수들은 23일부터 만들기시작.)
    ***할수있는일: 1) OKS sigmas 계산. 2) mean OKS 계산.
    설명: OKS(Object Keypoint Similarity) 관련 클래스.
    제작배경: 원래 OKS sigma값들 계산하는 함수를 통째로 만들었었는데, OKS 평균값을 구할라니 그 코드들을 재사용해야겠고, 그러려니 통으로된 함수를 좀 나눠야겠고,
    그러고보니 각 함수들이 서로 의존적이고 공유하는 변수들도 있고 해서 더 큰 그룹으로 감싸고싶어지고,
    자연스럽게 클래스가 왜 생겼는지를 깨닫게됐음. 그래서 클래스 만들어서 함수들 및 공유변수들 넣어주려고 이 클래스 만들게됐음.
    근데 공유변수는 아직 크게 만들필요를 못느껴서 안만듦. 생각해보니, 공유변수를 사용하면 함수들의 독립성이 떨어져서 다른데서 특정함수만 갖다쓸때 난감할듯?아마도? 그래서 공유변수 안만듦 일단.
    ->근데 다시생각해보니, 임포트할때 클래스에속하지않은 function을 임포트하는경우는 있어도, 클래스에 속한 method를 임포트하진 않지않나? 
      임포트는 클래스 또는 함수(method가 아닌, function)를 하는거아님?
      즉, 어떤 클래스에 속한 어떤 메서드를 임포트해서 사용하고싶으면, 그 클래스를 통째로 임포트한뒤에 그클래스에있는 그 원하는 해당메서드를 사용해야되지않나 보통?
      클래스가 한 덩어리고 그클래스의 메서드는 (항상그런건아니겠지만)그클래스와 분리되어 작동할수 없는것같음.
      -->자, 그럼, 메서드들에서 공통으로 사용하는부분이 있으면 빼주자. __init__ 등으로 빼도될테고. 이제 __init__ 을 만들 필요성이 느껴지네. 
    """

    # self.oks_sigmasj = [0.08953876, 0.08166177, 0.0193918, 0.01967773, 0.02095149, 0.02738186]

    def __init__(self, annos_dir:str, gt_anno_filename:str=None, oks_sigmasj:list=None):
        """
        Args:
            annos_dir (str): 어노테이션json파일들(손으로 해준 어노테이션이든, 모델의 디텍션결과든) 있는 디렉토리 경로.
            gt_anno_filename (str): annos_dir 에 들어있는 어노테이션json파일들 중, gt(ground truth)가 될 파일의 파일명.
                              만약 지정해주지 않으면, OKS sigmas 만 계산한다고 간주함.
            oks_sigmasj (list): (OKS sigmas 계산하고자할땐 사용안함.) OKS sigmas 값을 파이썬 리스트로 직접 넣어줘도 됨. 안넣어주면 내가정한 디폴트값을 사용. 
        """
        self.annos_dir = annos_dir
        self.gt_anno_filename = gt_anno_filename
        if oks_sigmasj == None: print('j) oks_sigmasj is not set, set the default value for upper implant 6 keypoints...')
        self.oks_sigmasj = np.array(oks_sigmasj) if oks_sigmasj != None else np.array([0.08953876, 0.08166177, 0.0193918, 0.01967773, 0.02095149, 0.02738186])
        print('j) oks_sigmasj:{}'.format(self.oks_sigmasj))
        self.flag_compute_OKS = True if gt_anno_filename != None else False  # i. False 면 OKS말고 OKS sigmas 만 계산한다고 가정, gt가 의미없으니 그냥 (두파일중)아무거나(정확히는 os.listdir 의 맨앞에오는놈을) gt로 지정.        

        gtdt_filename_list = os.listdir(annos_dir)
        assert len(gtdt_filename_list)==2, 'j) something is wrong!! there should be only 2 files in annos_dir, but it is not!!'
        # i. gt 어노json파일 지정해줬을경우, 그 파일의 파일명을 os.listdir 의 아웃풋 리스트의 첫번째 원소가 되게 순서 조정.
        if gt_anno_filename != None:
            if gtdt_filename_list[0] != gt_anno_filename:
                gtdt_order = [1,0] # i. change the order, so that gt comes first.
                gtdt_filename_list[:] = [gtdt_filename_list[i] for i in gtdt_order] # i. in-place 로 바꿔줬음. [:] 붙여서.
            assert gtdt_filename_list[0] == gt_anno_filename, 'j) something is wrong!!'
            print('j) gt annojson:{}, dt annojson:{}'.format(gtdt_filename_list[0], gtdt_filename_list[1]))

        self.gtdt_anno_list = []
        for jsonfileName in gtdt_filename_list:
            jsonfile_path = os.path.join(annos_dir, jsonfileName)
            with open(jsonfile_path) as f:
                anno = json.load(f)
            print('j.debug) type of anno=json.load(f) is:', type(anno))
            if 'annotations' not in anno: # i. Det2 의 프레딕션결과를 COCO 형식으로 바꾼건 'annotations'키의 밸류인 어노테이션정보(dict)들 모여있는 리스트 일거기때문에, 그경우에 손어노테이션결과랑 같게('image', 'categories' 키&밸류는 없겠지만) 형식 맞춰줌.
                anno = {'annotations': anno}
                # i. TODO: setting 'self.flag_imginfo_in_allannos' depends on the order of the annotation json files!!
                self.flag_imginfo_in_allannos = False  # i. 그럴경우 'images'키&밸류가 없을거기때문에 이와같이 불리언값 설정해줬음. 어노정보들은 있지만(키만 없었을뿐이지 내용물(밸류)은 있었지) 이미지정보들은 없으니.
            elif 'images' not in anno: # i. 이럴경우는 거의없겠지만 혹시나모를케이스대비(지금내경우처럼 손으로 좀 json파일을 고쳐줬다든가).
                self.flag_imginfo_in_allannos = False
            else:
                self.flag_imginfo_in_allannos = True
            self.gtdt_anno_list.append(anno)
            print('j) num of annotated objects in {}: {}'.format(jsonfileName, len(anno['annotations'])))
        self._sort_annos_j()

        
        # i. 지금 이 __init__함수에서 만들진 않았지만, 다른함수들 실행시 만들어지는 변수들.
        # self.sorted_tot_anlist1 # i. to be made after self._sort_annos_j()
        # self.sorted_tot_anlist2 # i. to be made after self._sort_annos_j()
        # self.mean_oks # i. to be made after compute_meanOKS_j(), if it's called.

    def compute_meanOKS_j(self):
        assert self.flag_compute_OKS == True, 'j) set gt_anno_filename!!'
        assert len(self.sorted_tot_anlist1) == len(self.sorted_tot_anlist2), 'j) something is wrong!! num of ans is different!!(만약 갯수 다르더라도 순서맞추는함수에서 갯수 일치하게 만들어놨는데 내기억엔..)'
        oks_list = []
        for (an1, an2) in zip(self.sorted_tot_anlist1, self.sorted_tot_anlist2):
            oks = self.compute_OKS_j(an1['keypoints'], an2['keypoints'], an1['area'])
            # print('j) oks for this 1 pair:{}, its type(should be float or sth like that):{}'.format(oks, type(oks))) # i. 타입은 <class 'numpy.float64'> 이네.
            oks_list.append(float(oks)) # i. 걍 혹시몰라서, 넘파이float64 에서 파이썬float으로 바꿔줌.
        print('j) len(oks_list):', len(oks_list))
        print('j) oks_list:', oks_list)
        self.mean_oks = sum(oks_list)/len(oks_list)  # i. 타입은 파이썬float.
        print('j) meanOKS:',self.mean_oks) 

    def compute_OKS_j(self, dt_kpts, gt_kpts, area):
        """
        하나의 물체에 대한 OKS 계산.
        cocoanalyze프로젝트의 compute_kpts_oks함수 사용.
        """
        g = np.array(gt_kpts)
        xg = g[0::3]
        yg = g[1::3]
        vg = g[2::3]
        assert( np.count_nonzero(vg > 0) > 0)
        d = np.array(dt_kpts)
        xd = d[0::3]
        yd = d[1::3]
        dx = xd - xg; dy = yd - yg
        variances = (self.oks_sigmasj * 2)**2
        e = (dx**2 + dy**2) / variances / (area+np.spacing(1)) / 2
        e=e[vg > 0]
        return np.sum(np.exp(-e)) / e.shape[0]

    def compute_OKSsigmas_j(self):
        """
        _sort_annos_j 함수가 순서일치시켜준 어노리스트들과 compute_OKSsigmas_with_sortedannos_j 함수를 이용하는, (적어도 OKS sigma값들 구할땐)최종적인 함수.
        """
        self.compute_OKSsigmas_with_sortedannos_j(self.sorted_tot_anlist1, self.sorted_tot_anlist2)



    ## i. 첨엔 요함수 이름이 걍 sort_annos_j 였는데, 클래스안에넣어준뒤로 외부에서갖다쓸일없을듯해서 이름앞에 언더스코어 붙였음.
    ## -> 이후에 함수명에 gtgt라는 표현도 추가삽입함. 왜냐면, 이건 내가 손으로 어노테이션해준 두개를 정렬해주는건데
    ## (둘다 gt의 형식을 가지고있는거지. 근데, 같은이미지에대한 어노라도 이미지id가 다름. 두번 어노테이션해줄때 어노테이션툴에서 이게 같은이미지라고 판단하지 않으니까. 그래서 요함수에선 이미지id가 아닌 이미지파일명을 이용한거고.),
    ## gt랑 dt를 비교해서 mean OKS 구하려할때는 요함수를 쓸수가없음. dt 형식에는 이미지파일명 정보가 없어서. 대신, 이미지id가 gt와 일치함. 그래서 함수 하나 더 만들어서 _sort_gtdt_annos_j 라고 이름붙이고 이미지id 사용해서 정렬해줄예정.
    ## -> 걍 요 _sort_annos_j 함수를 좀 수정해서 이함수로 다 되게 했음. 함수하나더만들자니 어차피 중복되는내용이 대부분이라.
    def _sort_annos_j(self):
        """
        (처음제작일: 2020.06.23.화욜낮.)
        [동일한 데이터셋(동일한 이미지들)대해 어노테이션해준 어노테이션json파일들(일단 2개)로부터 OKS sigma 값들을 계산해주는 함수] 를 위해,
        각 물체에 해당하는 어노테이션들(일단 2개씩)을 매치시켜주기위해 어노테이션들(일단 2개)에서 각물체어노들의 순서를 일치시켜주는 함수.
        (원래 OKS sigma값들 계산하는 함수를 통째로 만들었었는데, OKS 평균값을 구할라니 그 코드들을 재사용해야겠고, 그러려니 통으로된 함수를 좀 나눠야겠고,
        그러고보니 각 함수들이 서로 의존적이고 공유하는 변수들도 있고 해서 더 큰 그룹으로 감싸고싶어지고,
        자연스럽게 클래스가 왜 생겼는지를 깨닫게됐음. 그래서 클래스 만들어주고 이함수는 그안에 넣을예정.)
        Args:
            annos_dir (str): (같은이미지들에대한)어노테이션json파일들이 있는 디렉토리의 경로. -> 없애버림. 클래스만들어서.
        Returns:
            tot_anlist1 (list), tot_anlist2 (list): 순서 일치된 두 어노리스트(각물체에대한 어노테이션들의 총 리스트). ->없애버림. 클래스만들어서.
        """
        
        def imgid2filename(imgid, anno):
            imginfo_list = anno['images']
            for imginfo in imginfo_list:
                if imginfo['id'] == imgid:
                    return imginfo['file_name']

        def compute_objCloseness_byKP(obj1kp, obj2kp):
            """
            Args:
                obj1kp (list), obj2kp (list): [x1,y1,v1,...,xn,yn,vn] 형태의 리스트. 일단 내플젝에선 옵젝당 키포인트갯수가 6이라 n=6 임.
            Returns:
                mean_dsq (float): 두 옵젝의 각 키포인트들간의 거리의 제곱들의 평균.
            """
            assert len(obj1kp)==len(obj2kp) and len(obj1kp)%3==0, 'j) something is wrong!!'
            if int(len(obj1kp)/3) != 6: print('j) num of keypoints per obj is {}. Warning: It is NOT 6! the original implant project is using 6kps in one implant.'.format(int(len(obj1kp)/3)))
            obj1kp = np.asarray(obj1kp)
            obj2kp = np.asarray(obj2kp)
            obj1kp_x = obj1kp[0::3]
            obj1kp_y = obj1kp[1::3]
            obj2kp_x = obj2kp[0::3]
            obj2kp_y = obj2kp[1::3]
            dsq = (obj1kp_x-obj2kp_x)**2+(obj1kp_y-obj2kp_y)**2
            mean_dsq = np.sum(dsq)/obj1kp_x.size   # i. 현재내플젝에선 obj1kp_x.size 는 6인거지. 임플1개당 키포인트6개니까.
            return mean_dsq  # i. 이 값이 '작을'수록 두 옵젝의 키포인트들이 근접한거지.


        ## i. 두 어노테이션에서 각물체어노들 순서 일치시키기위해, 두단계로 진행:
        ## 1)이미지파일별로 어노들 묶음. 2)각이미지의 어노에서 순서 일치시킴.
        
        ## i. 1) 이미지파일별로 어노들 묶는 단계.
        
        # i. 요 _sort_annos_j 함수가 sort_annos_j 라는이름이엇을때(앞에 언더스코어 없었을때), 인풋인자로 annos_dir(어노테이션json파일들(두개)담긴디렉토리경로)를 받았었을때 사용했던 코드.
        # annos_ofSameData_list = os.listdir(annos_dir) ## i. 요 순서를 계속 사용하는거임. 
        # print('j) annotation JSON files in the given dir:', annos_ofSameData_list)
        # # anlist_list = []
        # filename2anlist_list = []
        # for anno_fileName in annos_ofSameData_list:
        #     anno_path = os.path.join(annos_dir, anno_fileName)
        #     with open(anno_path) as f:
        #         anno = json.load(f)

        ## i. 2020.06.26.금욜낮.) 요 코드부분에서 'filename2anlist' 라는 표현의 'filename' 이라는 표현을 'filenameOrImgid' 로 바꿈.
        filenameOrImgid2anlist_list = []
        for anno in self.gtdt_anno_list:
            # imgid2anlist = {}
            # for an in tot_anlist:
            #     if an['image_id'] in imgid2anlist: imgid2anlist[an['image_id']].append(an)
            #     else: imgid2anlist[an['image_id']] = [an]
            
            tot_anlist = anno['annotations']
            filenameOrImgid2anlist = {}
            for an in tot_anlist:
                if self.flag_imginfo_in_allannos == True:
                    filenameOrImgid = imgid2filename(an['image_id'], anno) # i. 여기서 파일네임이란건 각 이미지파일의 파일명 말하는거임. 어노테이션json파일의 파일명 말고.
                else: # i. Det2의 프레딕션결과를 COCO형식으로 바꾼거는 이럴수있음.
                    filenameOrImgid = an['image_id']
                
                if filenameOrImgid in filenameOrImgid2anlist: filenameOrImgid2anlist[filenameOrImgid].append(an)
                else: filenameOrImgid2anlist[filenameOrImgid] = [an] # i. 여기서부터 바로 anlist 가 시작되는거지.

            filenameOrImgid2anlist_list.append(filenameOrImgid2anlist)
            # anlist_list.append(anno['annotations']) # i. anno['annotations'] 는 list[dict] 임. 즉 [{어노1정보}, {어노2정보}, ...] 형태임(어노n정보라는건 특정 옵젝에 대한거.).

        filenameOrImgid_list = [filenameOrImgid_key for filenameOrImgid_key in filenameOrImgid2anlist_list[0]]
        
        ## i. 2) 특정 이미지 내에서 각물체에대한어노테이션의 순서를 일치시키는 부분.
        tot_anlist1=[]
        tot_anlist2=[]
        for filenameOrImgid in filenameOrImgid_list: # i. 여기서 filenameOrImgid(파일명 또는 이미지id)가 만약 파일명이라면, 그건 이미지파일명임. 어노테이션json파일명 말고.
            anlist1 = filenameOrImgid2anlist_list[0][filenameOrImgid]
            anlist2 = filenameOrImgid2anlist_list[1][filenameOrImgid]
            if self.flag_imginfo_in_allannos == True: # i. 이경우, 두 어노테이션json파일 모두 사람이 손으로 어노테이션해준거라고 간주.
                assert len(anlist1)==len(anlist2), 'j) MAYBE something is wrong!! 두개다 사람이 어노테이션해준건데 아예 물체 갯수가 다를정도일 가능성은 별로 없자나!!'
            # i. 두 어노테이션의 어노테이션해준 물체갯수가 달라도 작동하도록 이후의 코드 작성되어있음.
            else:
                if len(anlist1)!=len(anlist2):
                    imgfilename = imgid2filename(anlist1[0]['image_id'], self.gtdt_anno_list[0])
                    print('j) (WARNING) in {}(imgid:{}), num of ans is different btw gt and dt!! gt:{}ans, dt:{}ans!!'.format(imgfilename, anlist1[0]['image_id'], len(anlist1), len(anlist2)))
             
            if len(anlist1)==1 and len(anlist2)==1:
                tot_anlist1.extend(anlist1)
                tot_anlist2.extend(anlist2)
                continue

            detObjClosenessMat_for1img = np.zeros((len(anlist1), len(anlist2))) # i. int32인 0 가 아닌, float64인 0. 들이 생성되므로, 이후에 float 들을 할당가능.(numpy ndarray의 dtype이 int32면 float 할당해도 int로 바껴서 들어감.)

            for idx1, an1 in enumerate(anlist1):
                for idx2, an2 in enumerate(anlist2):
                    detObjClosenessMat_for1img[idx1, idx2] = compute_objCloseness_byKP(an1['keypoints'], an2['keypoints'])
            
            # print('j.debug) detObjClosenessMat_for1img:',detObjClosenessMat_for1img)

            lowtohigh_sorted_ind = np.unravel_index(np.argsort(detObjClosenessMat_for1img, axis=None), detObjClosenessMat_for1img.shape) # i. lowtohigh_sorted_ind 형태는 (axis0_arr, axis1_arr) 임. numpy 공홈의 numpy.argsort 의 예시들 보면 나옴. 예를들면 다음과같음: (array([0, 1, 1, 0], dtype=int64), array([1, 0, 1, 0], dtype=int64))
            # print('j.debug) lowtohigh_sorted_ind:',lowtohigh_sorted_ind)
            minlen = min(len(anlist1), len(anlist2))
            matchedIdxTup_list = [idx_tup for idx_tup in zip(*lowtohigh_sorted_ind)][:minlen]  # i. -> 예를들어, (이 이미지1개에서)두 어노테이션이 둘다 2개씩 물체 어노테이션했다면(또는, 두 어노중 적은 어노갯수가 2개라면), matchedIdxTup_list 의 형태는 예를들면 [(0,1), (1,0), (1,1), (0,0)] 이런식임.
            # print('j.debug) matchedIdxTup_list:',matchedIdxTup_list)
            matchedIdxTup_sorted_list = sorted(matchedIdxTup_list, key=lambda tup: tup[0]) # i. anlist1 의 순서대로 정렬. 이제 이걸토대로 anlist2의 순서를 바꿔주면됨.

            anlist2_sorted = [anlist2[IdxTup[1]] for IdxTup in matchedIdxTup_sorted_list] # i. minlen 만큼만.

            filenameOrImgid2anlist_list[1][filenameOrImgid] = anlist2_sorted  # i. 정렬해준놈으로 변경. 근데사용안할지도.

            tot_anlist1.extend(anlist1[:minlen]) # i. minlen 만큼만.
            tot_anlist2.extend(anlist2_sorted)
        
        self.sorted_tot_anlist1 = tot_anlist1
        self.sorted_tot_anlist2 = tot_anlist2


    def compute_OKSsigmas_with_sortedannos_j(self, sorted_tot_anlist1, sorted_tot_anlist2):
        """
        순서일치된 각물체에대한어노테이션의리스트 들(현재는 2개)을 사용해서, OKS sigma 값들 출력하는 함수. 
        """
        ## i. 위에서 각옵젝에대한어노들 순서 일치시켜준걸 가지고, OKS 계산하는 부분.
        # i. 이전코멘) 여기서 tup 는 ({어노1정보},{어노1정보},{어노1정보},...) 이런식임. 중복되게 어노테이션 해준 갯수만큼. 일단 2개겟지. 2개만 해줄예정이니. 즉, tup는 걍 ({(물체a에대한 첫번째 어노테이션의)어노a정보},{(동일한물체a에대한 두번째 어노테이션의)어노a정보}) 이렇게되는거지 2개만.
        #  -> ㄴㄴ!!! 다시보니 어노정보들이 순서가 일치하지가 않는듯!!! 위에서 일치시켜준뒤에 이부분 실행돼야함.
        anlist_list = [sorted_tot_anlist1, sorted_tot_anlist2] ## i. 위에서 순서일치 완료한거 넣어줌. ->(혹시 나중에 내가 까먹을까봐 적어놓자면)여기서 '위'라고 햇는데, 사실 원래는 하나의 통으로된 함수였어서 '위에서'라는 표현을 썼었던거임. 지금은 분리하고 클래스에 집어넣어놨지만. 그리고 지금 좀 깔끔하지 못하고 불필요한 코드들도 있고 한데, 기존코드를 수정하면서 생긴것들임.
        d2_over_s2_summed = np.zeros(6)
        for tup in zip(*anlist_list): 
            # one_anno_kp_dict = {}
            # one_anno_kp_dict[........blah blah]

            # # i. 내가원하는건 이런식으로 돼야함.
            # # one_anno_kp_dict = {......지금 급해서 일단 출근. }


            # 2020.06.23.화욜 13:20. 지금 내가종이에써놓은 OKS 수식 이론 생각중이엇음. OKS sigma 구할때랑 OKS값을 구할때랑 조금 달라지는것같은데?? OKS시그마 구할때는 gt라는게 없자나.
            # gt 와 모델의프레딕션키포인트의 차이(거리)를 d_i 라 한다치고, 그럼 OKS시그마 구할때는 중복되게 어노테이션을 여러번 하면 뭘 gt로 쳐서 그거랑의 거리를 구할거냐 이거지.
            # 중복 어노테이션 키포인트들의 평균지점을 gt로 치고, 그거와의 거리에 대해서 분산or표준편차를 구하면 가장 합리적일텐데,
            # 글케치면, 어노테이션을 딱 두번만 한다면 그 중간지점을 gt라고 쳐야할테니 거리는 두 어노테이션지점간거리의 1/2이 되겠지. 근데 걍 굳이 그렇게 하지말고 두 포인트 거리를 갖다써도 뭐 어차피 상수팩터만큼달라지는것뿐이니 상관없을거란거임.
            # -> 퇴근후 화욜저녁 생각: 뭐 별거아닌건데 깊게생각 ㄴㄴ. 걍 간단히 고고. 걍 두번 어노테이션해서 그 차이(거리)를 d_i라고 하고 계산해도 사실 문제없음.
            # 그리고 COCO공홈에서 'dually annotated data' 라고 언급한걸 봐선, OKS시그마 구할때 걍 두번만 어노테이션 해서 그 차이를 d_i 라고 치는듯함.
        
            # i. 원래 중복어노 여러개여도 되게 하려햇는데, 걍 두개만 잇는걸로 하자. 어차피 그이상 써먹을것도 아니고.
            diffs = np.array(tup[0]['keypoints'])-np.array(tup[1]['keypoints']) # i. 참고로 keypoints키의 밸류는 [x1,y1,v1,...,x6,y6,v6] 형태지. 나의경우 키포인트 6개니까.
            print('j) diffs:',diffs)
            squareds = diffs**2 # i. 참고로 keypoints키의 밸류는 [x1,y1,v1,...,x6,y6,v6] 형태지. 나의경우 키포인트 6개니까.        
            dsquareds = squareds[0::3]+squareds[1::3] # i. 원소6개.
            d2_over_s2_summed += dsquareds/tup[0]['area']   # i. 마찬가지로 원소6개. # i. 첫번째 어노의 넓이를 사용하자.
        print('j) 첫번째, 두번째 어노테이션에서 각각 어노테이션된 물체들 갯수: {}, {}'.format(len(anlist_list[0]), len(anlist_list[1])))
        var6 = d2_over_s2_summed/len(anlist_list[0]) # i. 역시 원소6개. 여기에 루트취하면 드뎌 OKS sigmas 임.
        oks_sigmas = np.sqrt(var6)
        self.oks_sigmasj = oks_sigmas # i. 넘파이어레이임.
        print('j) OKS sigmas:', oks_sigmas)



# i. 호출!!
# i. 아!!!!!!!!!!!!!!!! OKS시그마값들 거의 1가까이되는 큰값들이길래 이상하다 햇는데, 엄청난 문제가 있었네!!!!!!!!!!!!
# 두 어노테이션json파일의 어노정보들이 순서가 일치하지가 않겠네!!!!!!!! 그니까 지금 이상한놈들끼리 비교한거임!!! 동일물체에대한 두 어노를 비교해야하는데!!
# 근데, 어노테이션json파일의 정보에, 이미지파일명은 나오지만 한 이미지(한 PA방사선사진)내에서 어떤물체(어떤임플란트)인지는 알 도리가 없겠네!!!!
# 한 이미지 내에 n개의 어노테이션된 임플 잇다치면 걍 n x n 으로 모두 비교해서 젤 겹치는애들로 골라야할것같은데.... 일단 자자 넘 늦엇다..
## i. ->담날(2020.06.24.수욜.) 해결완료!! 일단 n x n 으로 돌아가긴 하는데, 나중을위해 n x m 으로 갯수 달라도 작동할수있도록 해놨음(assert 부분 정도만 제외하면).
##    잘 작동함!!
# compute_OKSsigmas_j(r'C:\Users\starriet\Desktop\for_OKS_simgas')

## i. 06.25.목욜오전.) 함수들 나누고 클래스로감싸줬음.
## 호출예시.
# oks_j = OKS_j(r'C:\Users\starriet\Desktop\for_OKS_simgas')
# oks_j.compute_OKSsigmas_j()

## i. 06.25.목욜늦은밤.) mean OKS 구하는함수도 구현완료. ->문제발생. 손으로한 어노파일 두개 비교는 되는데, 손어노랑 Det2결과(를 COCO형식으로바꾼거) 비교는 안됨. ->담날 해결!
## 호출예시.
# oks_j = OKS_j(r'C:\Users\starriet\Desktop\for_OKS_simgas', 'pa_keypoint_validation.json')
# oks_j.compute_meanOKS_j()

## i. 2020.06.26.금욜낮.) mean OKS 구하는함수 수정완료. ->손어노 두개 비교도 되고, 손어노랑 Det2결과를COCO형식으로바꾼거 비교도 됨. 물론 OKS sigmas 구하는것도 잘 됨.
## 호출예시.
# oks_j = OKS_j(r'C:\Users\starriet\Desktop\for_meanOKS', gt_anno_filename='pa_keypoint_validation.json')
# oks_j.compute_meanOKS_j()


### i. 2020.06.28.새벽01:45) 지금이거 깃헙에올린뒤에 내코랩플젝에서 깃클론해서 임포트해서 쓸거기때문에, 위의 호출예시같은거 다 코멘트아웃해놔야함!!
###    만약 저런 호출예시가 있어버리면, 임포트하면서 이 모듈(이 .py파일)자체가 다 실행되면서 No such file or directory: 'C:\\Users\\starriet\\Desktop\\for_meanOKS' 이런 에러가 뜨지.
### ->아!!!!! 이럴때 if __name__=="__main__" 을 쓰는거구나!!!!! 써주자!!!!!
if __name__ == "__main__":
    oks_j = OKS_j(r'C:\Users\starriet\Desktop\for_meanOKS\meanOKS2', gt_anno_filename='pa_keypoint_validation.json')
    oks_j.compute_meanOKS_j()