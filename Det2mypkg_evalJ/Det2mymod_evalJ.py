# i. 2020.06.13.토욜저녁.) 구글드라이브에 올려서, 내구글코랩플젝에서(현재디텍트론2관련플젝하고있지) 임포트해서 사용하려는 목적으로 만든 모듈(파이썬파일)임.
# i. 2020.06.17.수욜.) 걍 구글드라이브 말고 깃&깃헙사용하는게 내가 수정작업할때 더 편할듯. vscode상에서 바로 커밋하고 푸시하면 업뎃되니까. 구글드라이브로하려면 직접 파일들을 드라이브에 올려줘야하니까 귀찮고, 깃도사용안하니까 작업히스토리도 기록되지않고.
# <이 모듈에 있는것들 목록>
# class COCOEvaluator_j(DatasetEvaluator):

# i. 이 모듈(지금 이 Det2mylib_evalJ.py 파이썬파일)을 내구글코랩플젝에서 임포트해서 사용할예정이니까,
# 아래처럼임포트(내구글코랩플젝에서이렇게임포트함)한다음 지금 이 모듈에서 사용하면 되겠지? (나중에 내구글코랩플젝에서 지금 이 모듈을 임포트해서 사용할때 문제없이 작동하겠지?)
from detectron2.evaluation import COCOEvaluator

# i. 이것들을(전부다필요한건진몰겟지만) 왜 임포트해줘야되나몰겟는데 자꾸 내 코랩플젝에서 not defined로 뜨니까 일단 해줘봄. Det2 의 COCOEvaluator 클래스 정의돼잇는 coco_evaluation.py 의 상단에 적혀잇는 임포트코드들 걍 다 긁어온거임.
# 이미 위에서임포트한 COCOEvaluator 가 정의돼잇는 파이썬파일(모듈)인 coco_evaluation.py 에서 import itertools 해주고있는데....
import contextlib
import copy
import io
import itertools
import json
import logging
import numpy as np
import os
import pickle
from collections import OrderedDict
import pycocotools.mask as mask_util
import torch
from fvcore.common.file_io import PathManager
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
from tabulate import tabulate

import detectron2.utils.comm as comm
from detectron2.data import MetadataCatalog
from detectron2.data.datasets.coco import convert_to_coco_json
from detectron2.structures import Boxes, BoxMode, pairwise_iou
from detectron2.utils.logger import create_small_table

from detectron2.evaluation.evaluator import DatasetEvaluator # i. coco_evaluation.py 파일에서는 상대경로로 from .evlauator import DatasetEvaluator 이렇게 해줬는데, 난 절대경로로 바꿔줬음.




# i. Det2의 동명의(_j만 뺀)클래스를 내가 수정해준 클래스.
class COCOEvaluator_j(COCOEvaluator): # i. 참고로 COCOEvaluator는 DatasetEvaluator의 자식클래스임.
    def _eval_predictions(self, tasks, predictions):
        """
        Evaluate predictions on the given tasks.
        Fill self._results with the metrics of the tasks.
        """
        self._logger.info("Preparing results for COCO format ...")
        coco_results = list(itertools.chain(*[x["instances"] for x in predictions]))

        # unmap the category ids for COCO
        if hasattr(self._metadata, "thing_dataset_id_to_contiguous_id"):
            reverse_id_mapping = {
                v: k for k, v in self._metadata.thing_dataset_id_to_contiguous_id.items()
            }
            for result in coco_results:
                category_id = result["category_id"]
                assert (
                    category_id in reverse_id_mapping
                ), "A prediction has category_id={}, which is not available in the dataset.".format(
                    category_id
                )
                result["category_id"] = reverse_id_mapping[category_id]

        if self._output_dir:
            file_path = os.path.join(self._output_dir, "coco_instances_results.json")
            self._logger.info("Saving results to {}".format(file_path))
            with PathManager.open(file_path, "w") as f:
                f.write(json.dumps(coco_results))
                f.flush()

        if not self._do_evaluation:
            self._logger.info("Annotations are not available for evaluation.")
            return

        self._logger.info("Evaluating predictions ...")
        # i. 2020.06.26.) 참고로 요기서 sorted(tasks)라는건 sorted(set(tuple))임. 여기서 tuple 은 ('bbox', 'segm', 'keypoints') 임. tuple은 순서 고정임.
        # 즉, 요기서 sorted(tasks)는 tuple ('bbox', 'segm', 'keypoints') (순서고정) 을 set (순서랜덤)에다 넣고, 그걸 다시 sorted 함수에 넣어서 리턴된 리스트(순서고정) ['bbox', 'keypoints', 'segm'] 임. 파이썬의 sorted 함수는 아마 알파벳순서로 정렬해주는듯. 대문자는 더 먼저 정렬되는것같고.
        # 아 근데, cfg.MODEL.MASK_ON 이랑 cfg.MODEL.KEYPOINT_ON 설정값에따라 'segm' 과 'keypoints' 는 들어갈수도있고 안들어갈수도있음.
        for task in sorted(tasks):
            coco_eval = (
                # i. 내가수정해준함수 사용! 딱 이부분만 바꿔줬음.
                self._evaluate_predictions_on_coco_j(
                    self._coco_api, coco_results, task, kpt_oks_sigmas=self._kpt_oks_sigmas
                )
                if len(coco_results) > 0
                else None  # cocoapi does not handle empty results very well
            )

            res = self._derive_coco_results(
                coco_eval, task, class_names=self._metadata.get("thing_classes")
            )
            self._results[task] = res

    # i. Det2 의 동명의(이름 뒤에서 _j만 뺀)함수를 내가 조금 수정해준 함수로, 내가 COCOEvaluator_j 안으로 넣었음. 원래 COCOEvaluator클래스 안에 들어있던 함수 아님.
    def _evaluate_predictions_on_coco_j(self, coco_gt, coco_results, iou_type, kpt_oks_sigmas=None):
        """
        Evaluate the coco results using COCOEval API.
        """
        assert len(coco_results) > 0

        if iou_type == "segm":
            coco_results = copy.deepcopy(coco_results)
            # When evaluating mask AP, if the results contain bbox, cocoapi will
            # use the box area as the area of the instance, instead of the mask area.
            # This leads to a different definition of small/medium/large.
            # We remove the bbox field to let mask AP use mask area.
            for c in coco_results:
                c.pop("bbox", None)


        # i. 요한줄도 내가추가. cocoanalyze 의 run_analysis.py 파일 실행시 사용하려고. 일단 바로위에서 bbox 다 없애준거 사용해보자.
        # 여기서 coco_results는 [{어노1정보}, {어노2정보},...] 이런 리스트일거임(bbox정보는 삭제됐고. 바로위에서 bbox는 다 없앴으니).
        ## i. 2020.06.26.금욜저녁.) ->아니지!! 지금 이 _evaluate_predictions_on_coco_j 함수는(_j뺀 원래함수도 마찬가지고) for문에서 task 종류별로 실행되잖아!!!
        ## 즉, 내 기존 코드에서는 self.coco_dt_WObbox_j 라는 변수가 반복적으로 새로운값을 가리키게 되는거지!! 뭐 내가 마스크 옵션 꺼놔서 for문의 마지막 task 종류가 키포인트라서 결과는 뭐 내내 똑같긴한데, 그래도 언제 마스크옵션 켜줄지 모름!
        ## task 종류가 'keypoints' 일 경우에만 작동하도록 수정함. 이렇게하면 반복해서 할당되지 않지. (참고로 나는 평소에, 변수가 어떤 값을 가리키는거랑(사실 이게 정확한표현임) '할당'이란 표현을 걍 섞어쓰고있음.)
        ## 사실 바로위에서 task가 'segm'일때 bbox 없애주는거 말고는, 지금이시점에서는 task에따른 차이 없기때문에 큰 상관 없기는 함.
        ## 그리고 변수명도 self.coco_dt_WObbox_j 에서 self.cocoformatted_anlist_dt_j 로 바꿔줌. bbox 안없앤상태니까 WO(without)라고 써놓으면 안되지.
        ## - 참고로, 여기서 'anlist'라는 표현에서 'an'은 물체1개에 대한 어노테이션정보를 의미함. 즉 'anlist' 는 COCO형식의 어노테이션json에서 'annotations'키의 밸류에 해당하는 list[dict] 를 의미함.
        if iou_type == 'keypoints':

            cocoformatted_anlist_dt_j = copy.deepcopy(coco_results)

            ## i. 코랩에다가 작성했던코드(및 코멘트) 여기 붙여넣기로 적용한거라 코드가 좀 덕지덕지스러울수있는데 일단 걍 하자.
            ## i. 2020.06.26.금욜저녁.) 요 cocoformatted_anlist_dt_j 의 내용을 보면, 각 어노정보에 'score'라는 키와 그 밸류(0.9884~~이런식의)가 있는데, 이게 bbox 에 대한 스코어일거임.
            ## 근데, coco이밸류에이션 관련 툴들은 다 요 bbox 스코어를 사용해서 Precision-Recall 그래프를 그리는것 같음(참고로, Precision-Recall curve 의 각 점은 모델이 내놓은 스코어에대해 특정 threshold를 적용한걸 나타내잖아.). 
            ## 근데 키포인트에 관련해서 Precision-Recall 그래프 그리려면 bbox가 아니라 키포인트 스코어로 해야하는거 아니냐는게 지금 내 생각인거임. 특히 지금내플젝의경우 임플 디텍션은 넘 쉽고 어노테이션도 대충했기때매 bbox 점수는 별 의미가 없는데 말이지.
            ## 그래서, 요 cocoformatted_anlist_dt_j 에서 각 어노정보에 들어있는 'score' 키의 밸류를 키포인트 스코어의 평균값으로 바꿔서 넣어줘보려함(덮어씌우는거지).
            ## 이렇게하면 이후에 coco관련 이밸류에이션코드들(Det2에 포함된 coco이밸류에이션 코드들이나, cocoanalyze 코드나 뭐 죄다.)이 요 'score'키의 밸류를 가지고 계산하겠지!! 자, 함 해줘보자.
            ## 3종류의 대푯값을 구해봤음.
            for an in cocoformatted_anlist_dt_j:
                ## i. 1) 걍 6개 스코어 평균(모든 키포인트의 가중치 동일하게 1/6 인 셈).
                kpscore_list = an['keypoints'][2::3] ## i. 6개 키포인트들의 스코어 리스트. 예: [0.5142306685447693, 0.13451290130615234, 0.8434943556785583, 0.5492475628852844, 0.5927586555480957, 0.458468496799469]
                kpscore_mean = np.mean(kpscore_list) ## i. 6개 키포인트 스코어 평균. 예: 0.5154521067937216
                ## i. 2) 본레벨 키포인트 2개 스코어만 평균.
                bl_kpscore_list = [kpscore_list[0], kpscore_list[1]] ## i. 좌우 본레벨 키포인트 2개 스코어만 담은 리스트. 예: [0.5142306685447693, 0.13451290130615234]
                bl_kpscore_mean = np.mean(bl_kpscore_list) ## i. 좌우 본레벨 키포인트 2개 스코어 평균. 예: 0.3243717849254608
                ## i. 3) 6개 키포인트마다 가중치 다르게 부여한 평균.
                oks_sigmas = [0.08953876, 0.08166177, 0.0193918, 0.01967773, 0.02095149, 0.02738186] ## i. 각 키포인트의 가중치를 OKS sigmas 로 해봄. 지금이값은 테스트데이타에서 얻은 OKS sigmas 값이라 엄밀히는 안되겠지만 어차피 트레이닝데이타에서 얻은 OKS sigmas 도 크게 다르지 않을것같으니까 일단 써봄.
                kp_weights = np.array(oks_sigmas)/np.sum(oks_sigmas) ## i. 계산결과: array([0.34623967, 0.31577994, 0.07498664, 0.07609231, 0.08101784, 0.1058836]). 원소들의 합은 당연히 1임.
                weighted_kpscore_mean = np.sum([kpscore*weight for kpscore, weight in zip(kpscore_list, kp_weights)]) ## i. 계산결과: 0.42213617505635503
                ## i. 자, 이제 위에서구한 대푯값들중 하나 골라서 넣어줘보자(score 키의 밸류(원래는 bbox score에 해당하는)에 덮어씌우기).
                an['score'] = weighted_kpscore_mean ## i. 일단 가중치 달리 부여한 대푯값으로 해봄.

            coco_results = cocoformatted_anlist_dt_j
            self.cocoformatted_anlist_dt_j = copy.deepcopy(coco_results)
        ####### i. 여기까지 내가추가해준거임. 첨엔 deepcopy 해서 원래코드에 영향 안가게 하려 했는데, 일부러 coco_results 값을 바꿔줬음. COCO관련 이밸류에이션 코드들 모두 bbox스코어 대신 키포인트스코어를 이용하게 해보려고. #########

        coco_dt = coco_gt.loadRes(coco_results)


        # i. 요 두줄 내가추가함. - coco_gt, coco_dt 를 복사해서 이 객체의 변수에 할당시킨뒤, 나중에 객체 밖으로 꺼내서 사용할거임.
        # 원래의 코드에는 전혀 영향 안미침.
        ## 이것도 task 종류가 키포인트일때만 작동하게끔 수정. 사실 이시점까지는 task별로 다르게 해준건 (위에서 segm일때 bbox 제거해준거 말고는)아직 아무것도 없기때매 별상관은 없지만.
        if iou_type == 'keypoints':
            self.cocoapi_gt_j = copy.deepcopy(coco_gt)
            self.cocoapi_dt_j = copy.deepcopy(coco_dt)


        coco_eval = COCOeval(coco_gt, coco_dt, iou_type)
        # Use the COCO default keypoint OKS sigmas unless overrides are specified
        if kpt_oks_sigmas:
            coco_eval.params.kpt_oks_sigmas = np.array(kpt_oks_sigmas)

        if iou_type == "keypoints":
            num_keypoints = len(coco_results[0]["keypoints"]) // 3
            assert len(coco_eval.params.kpt_oks_sigmas) == num_keypoints, (
                "[COCOEvaluator] The length of cfg.TEST.KEYPOINT_OKS_SIGMAS (default: 17) "
                "must be equal to the number of keypoints. However the prediction has {} "
                "keypoints! For more information please refer to "
                "http://cocodataset.org/#keypoints-eval.".format(num_keypoints)
            )

        coco_eval.evaluate()
        coco_eval.accumulate()
        coco_eval.summarize()

        return coco_eval