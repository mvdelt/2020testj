# i. 2020.09.03.목욜저녁.첫작성.) 
# 설명: 내 디텍트론2 코랩플젝(치과의료영상 딥러닝. 현재 임플 x-ray bone level 탐지 하는중이지)
#       에서 줄줄이 죄다 코딩해논것들 깔끔히 리팩토링하기위해 이 모듈 만듦.
#       일단 지금 PA_kp_paper.ipynb 코랩플젝을 리팩토링중이어서(엔드유저용으로, cfg랑 체크포인트는 다 다운받아서 인퍼런스만 하게끔), 
#       PA_kp_paper.ipynb 의 코드들(중 인퍼런스에만 관계된것들만) 여기에 복사해옴.


################################ i. 키포인트 로짓(히트맵) 넣어주는 코드. ###############################################################
from detectron2.modeling.roi_heads.keypoint_head import KRCNNConvDeconvUpsampleHead, ROI_KEYPOINT_HEAD_REGISTRY, keypoint_rcnn_loss, keypoint_rcnn_inference
## i. keypoint head 클래스(의 (부모클래스의)forward함수)를 새로작성해줌. 여기서 keypoint_rcnn_inference 함수가 등장하거든. - Det2 소스코드가 업뎃돼서 이렇게 바뀐거임. 
@ROI_KEYPOINT_HEAD_REGISTRY.register()
class KRCNNConvDeconvUpsampleHead_heatmapj(KRCNNConvDeconvUpsampleHead):
def forward(self, x, instances):
    """
    Args:
        x: input region feature(s) provided by :class:`ROIHeads`.
        instances (list[Instances]): contains the boxes & labels corresponding
            to the input features.
            Exact format is up to its caller to decide.
            Typically, this is the foreground instances in training, with
            "proposal_boxes" field and other gt annotations.
            In inference, it contains boxes that are already predicted.

    Returns:
        A dict of losses if in training. The predicted "instances" if in inference.
    """
    x = self.layers(x) ## i. 요 x (self.layers(x) 의 값) 가 바로 키포인트 logits 인듯.
    if self.training:
        num_images = len(instances)
        normalizer = (
            None if self.loss_normalizer == "visible" else num_images * self.loss_normalizer
        )
        return {
            "loss_keypoint": keypoint_rcnn_loss(x, instances, normalizer=normalizer)
            * self.loss_weight
        }
    else:
        # i. 요놈은 직접적으로 임포트 안해줬는데 왜 잘 되지?? 어디서 얘가 임포트되는거지?? -> 역시. 지금 이 셀에선 문제없는데, 다음셀(트레이닝해주는부분)에서 이놈이 not defined 라고 에러뜨네.
        keypoint_rcnn_inference(x, instances)
        ## i. 내가 만들어준 함수 실행. - keypoint_rcnn_inference 함수 안에다가 코드 작성할수도 잇는데, 걍 어제(Det2소스코드업뎃된줄몰랏을때) 따로 함수 만들어둿던거 사용. 
        self._put_kplogits_into_instancesj(x, instances)
        return instances      

# i. Instances객체에 pred_keypoint_logits 라는 (내가정해준)이름으로 키포인트 로짓 정보 넣어주는 함수. -  keypoint_rcnn_inference 함수 참고해서 내가만들어준 함수임.
def _put_kplogits_into_instancesj(self, pred_kp_logits, pred_instances):
    num_objects_per_image_list = [len(i) for i in pred_instances]
    pred_kp_logits_splited = pred_kp_logits.split(num_objects_per_image_list, dim=0)

    for pred_kp_logits_per_image, one_instances in zip(pred_kp_logits_splited, pred_instances):
    # i. pred_kp_logits_per_image is (num objects in 1 input image) x (num keypoints) x (side length of the keypoint heatmap) x (side length of the keypoint heatmap)
    one_instances.pred_keypoint_logits = pred_kp_logits_per_image

###############################################################################################################################









