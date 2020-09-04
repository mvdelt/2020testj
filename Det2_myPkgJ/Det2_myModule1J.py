# i. 2020.09.03.목욜저녁.첫작성.) 
# 설명: 내 디텍트론2 코랩플젝(치과의료영상 딥러닝. 현재 임플 x-ray bone level 탐지 하는중이지)
#       에서 줄줄이 죄다 코딩해논것들 깔끔히 리팩토링하기위해 이 모듈 만듦.
#       일단 지금 PA_kp_paper.ipynb 코랩플젝을 리팩토링중이어서(엔드유저용으로, cfg랑 체크포인트는 다 다운받아서 인퍼런스만 하게끔), 
#       PA_kp_paper.ipynb 의 코드들(중 인퍼런스에만 관계된것들만) 여기에 복사해옴.


# 여기서(맨위에서) 임포트할거 싹다해주면 되겠지? 함해보자.
import os, cv2
import numpy as np
from google.colab.patches import cv2_imshow # i. 이게 되나...??? 함해보자;;




################################ i. 키포인트 로짓(히트맵) 넣어주는 코드. ###############################################################################################################
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

#####################################################################################################################################################################################







################################# i. Visualizer_kplogitsj 클래스. Visualizer 클래스 상속해서 내가 수정해준거임. ##############################################################################################

## i. Det2의 Visualizer 클래스를 수정.
## i. 음.......이상함........ from A.B.C import D 라고 하면, C 가 모듈(.py파일)이라면, C가 다 실행되지않음? 그럼 실행됐으니까 메모리?에 올라갓든지 뭐글케돼서 굳이 임포트를 또 시켜올필요없는거아닌가??? 아닌가... 흠.....
from detectron2.utils.visualizer import Visualizer, ColorMode
from detectron2.utils.colormap import random_color
from matplotlib import colors as mplc
import matplotlib as mpl
# import matplotlib.pyplot as plt   ## i. ->필요없을것같아서 일단 코멘트아웃.


## i. 아 자꾸 변수 디파인안됏다고떠서 걍 싹다 (Det2소스코드로부터)복사해서 요기 붙여놓은거임. 지금내플젝에선 안쓰이는것도있을거임.
_KEYPOINT_THRESHOLD = 0.05
_SMALL_OBJECT_AREA_THRESH = 1000
_LARGE_MASK_AREA_THRESH = 120000
_OFF_WHITE = (1.0, 1.0, 240.0 / 255)
_BLACK = (0, 0, 0)
_RED = (1.0, 0, 0)

class Visualizer_kplogitsj(Visualizer):

    # i. 키포인트 히트맵을 PA상에 또는 잘라낸bbox상에 superimpose해서 그려주기위해 내가만든함수.
    def draw_kplogitsj(self, predictions):

      # print('predictions.pred_keypoint_logits.requires_grad:',predictions.pred_keypoint_logits.requires_grad) # i. False 겠지? 그래야지. -> ㅇㅇ.False출력됨.
      # print('predictions.pred_boxes.tensor.requires_grad:',predictions.pred_boxes.tensor.requires_grad) # i. 얘도 마찬가지로 False 출력되고.

      kplogits_per_image = predictions.pred_keypoint_logits
      boxes = predictions.pred_boxes # i. if predictions.has("pred_boxes") else None 이거 왜 안붙여줬냐면, 만약에 특정 인풋이미지(PA이미지)에서 디텍션된 물체(임플픽스쳐)가 없다고 해도, predictions.pred_boxes 등에는 비어있는 텐서가 들어갈거기때문에 predictions.has("pred_boxes") 의 값은 어차피 True 일 거거든(일단 내가 코드 훑어보기론 그러함). 일단 걍 그래서 if~ 는 빼줘봄.
      # i. 비주얼라이저객체.요함수(프레딕션) 이렇게 콜해줘서, 
      # 또다른 VisImage객체(아니면 기존VisImage객체를 수정한것)를 리턴시킬 예정.
      # 여기에는 히트맵 그려져잇음. 
      # 기존 영상에서 히트맵그릴 box부분만의 값을 좀 약하게해주면 더 굿. 이것도 함 시도해보자.


      # i. 각 box 의 좌표정보를 저장해두기위한 변수를 VisImage객체(self.output) 내부에 만듦. 나중에 (키포인트로짓 오버레이된)box만 크롭하여 보여줄때 사용하려고.
      self.output.boxCoordsTuple_listj = []
      for kplogits_per_obj, box in zip(kplogits_per_image, boxes):
        # i. box 좌표 저장. 나중에 box 크롭시 사용.
        self.output.boxCoordsTuple_listj.append( ( int(round(box[0].item())) , int(round(box[1].item())) , int(round(box[2].item())) , int(round(box[3].item())) ) )


        # i. 키포인트가 6개니까 키포인트로짓(히트맵)도 6개인데 하나의 box에 그려줘야하니까 걍 다 더해서 한 box에 6개의 로짓분포들이 다 보이도록 해줘보자.
        kplogits_per_obj_summed = torch.sum(kplogits_per_obj, 0) # i. torch tensor.
        kplogits_per_obj_summed_arr = kplogits_per_obj_summed.numpy() # i. numpy array.        


        # i. 리사이징 코드. 일단 코멘트아웃해줘봄. 여기서 cv2.resize로 리사이징 안해줘도 요 아래 ax.imshow 에서 해주는듯해서.
        # -> 내생각대로긴한데, ax.imshow 의 인터폴레이션은 (기본값인 'antialiased'는 심하게 그렇고, 대조도 높아보이는 'sinc'로 해주니 훨 낫긴하네.) 네모네모하게 나오네 부드럽게 안나오고. 필요하면 요코드 다시 살려서 cv2.resize 사용해주자.
            # (예제코드)
            # imgArr = cv2.imread('your_image.jpg')
            # resized_imgArr = cv2.resize(imgArr, dsize=(가로길이 정수, 세로길이 정수), interpolation=cv2.INTER_CUBIC)
        boxSize=(int(round(box[2].item()-box[0].item())), int(round(box[3].item()-box[1].item())))
        # i. 일단 토치텐서로 해줘보는데, 안되면 넘파이어레이로 바꾸자. one_kplogits.numpy() 이런식으로해주면되나봄. -> 에러떠서 .numpy() 해줬더니 잘 됨.
        # i. interpolation 설정값 바꿔줘보자.
        # i. 요 아래 self.output.ax.imshow 에서 extent 설정해주고 interpolation 설정해주면, 지금 이 opencv 의 resize 는 굳이 사용 안해도 될것같긴 함. ->ㅇㅇ.맞음.근데 걍 사용해줘봄.
        kplogits_per_obj_summed_arr = cv2.resize(kplogits_per_obj_summed_arr, dsize=boxSize , interpolation=cv2.INTER_CUBIC)


        # self.output.ax.add_image(plt.imshow(kplogits_per_obj_summed_arr)) # i. ->이렇게하니까 뭐 하나를 여러개에 할수없다는식으로 에러뜸;; 아래처럼 self.output.ax.imshow 이렇게하니까 잘 됨.
        kplogitsPerObj_AxesImage = self.output.ax.imshow(kplogits_per_obj_summed_arr, alpha=0.4, extent=(box[0].item(), box[2].item(), box[3].item(), box[1].item()), interpolation='sinc') # i. 오! extent 설정해주니 이미지 좌표 설정 되네!! interpolation 옵션값 골라주는대로 인터폴레이션 되고(이미지 확대/축소시에).
        # i. ->위의 변수 kplogitsPerObj_AxesImage 는 이제 이용 안함. - 아래에 patch 이용해서 clip 하는거 해보려고, imshow 의 리턴값인 AxesImage객체를 할당하고자 만들었던 변수였음. 
        

        # # i. (생각해보니 의미없어서, 해보고싶은것만 구현해보고 코멘트아웃함.)        
        # # i. 요기서부턴 box 대로 clip 해서 보여주는 코드. -> 이상하게잘림. 그도그럴것이, 현재 axes 의 정보가 없자나?? -> transform=self.output.ax.transData 넣어줘보자!!!->더이상하네. ax.transAxes해보자. -> 그래도안되네. transAxes같은경우는 (0,0)~(1,1)단위라서 그런듯? 암튼 이거중요한거아니니 패스.
        # # -> 패스하려고했는데 기준원점 바꿔서 transData로 실행시켜논거 출력 제대로 됏네!! transform 지정안해줫을땐 원점을 좌하단으로 해줫엇는데, 혹시나해서 좌상단을 원점으로 해주고 transform을 ax.transData 로 해주니까 원하는대로 되네!!!
        # # 암튼 이제 해보고싶은건 했고, 근데 다시생각해보니 내가원하는건 이걸로 안되는거라 일단 코멘트아웃.  
        # rectPatch_forClip = mpl.patches.Rectangle((box[0].item(), box[1].item()), (box[2].item()-box[0].item())*0.75, (box[3].item()-box[1].item())*0.75, transform=self.output.ax.transData)
        # kplogitsPerObj_AxesImage.set_clip_path(rectPatch_forClip)        

      return self.output



    def draw_instance_predictions(self, predictions):
      """
      Draw instance-level prediction results on an image.

      Args:
          predictions (Instances): the output of an instance detection/segmentation
              model. Following fields will be used to draw:
              "pred_boxes", "pred_classes", "scores", "pred_masks" (or "pred_masks_rle").

      Returns:
          output (VisImage): image object with visualizations.
      """
      boxes = predictions.pred_boxes if predictions.has("pred_boxes") else None
      scores = predictions.scores if predictions.has("scores") else None
      classes = predictions.pred_classes if predictions.has("pred_classes") else None
      labels = self._create_text_labelsj(classes, scores, self.metadata.get("thing_classes", None))
      keypoints = predictions.pred_keypoints if predictions.has("pred_keypoints") else None
      # i. keypoint logits 도 추가. 내가수정해준 keypoint heads 클래스의 내가만든함수에서 "pred_keypoint_logits" 라는 이름으로 Instances객체에 키포인트 로짓 넣어줘놨지.
      kplogits_per_image = predictions.pred_keypoint_logits

      if predictions.has("pred_masks"):
          masks = np.asarray(predictions.pred_masks)
          masks = [GenericMask(x, self.output.height, self.output.width) for x in masks]
      else:
          masks = None

      if self._instance_mode == ColorMode.SEGMENTATION and self.metadata.get("thing_colors"):
          colors = [
              self._jitter([x / 255 for x in self.metadata.thing_colors[c]]) for c in classes
          ]
          alpha = 0.8
      else:
          colors = None
          alpha = 0.5

      if self._instance_mode == ColorMode.IMAGE_BW:
          self.output.img = self._create_grayscale_image(
              (predictions.pred_masks.any(dim=0) > 0).numpy()
          )
          alpha = 0.3

      # i. 요함수에서 키포인트도 그려줌.(draw_and_connect_keypoints메서드 호출해서.)
      self.overlay_instancesj(
          masks=masks,
          boxes=boxes,
          labels=labels,
          keypoints=keypoints,
          kplogits_per_image = kplogits_per_image, # i. 요거 추가해줌. 시각화결과 그려줄때 키포인트 로짓 정보를 활용해보려고(예를들어 키포인트마다 로짓 값 보여준다든지).
          assigned_colors=colors,
          alpha=alpha,
      )
      # i. 내가만든함수(show_kplogitsj)호출. ->여기서 호출 안하기로.
      # print('kplogits_per_image:',kplogits_per_image)
      # self.show_kplogitsj(kplogits_per_image) # i. 너무 출력 이미지들이 많아서그런가 자꾸 코랩이 다운(?)돼서 일단 코멘트아웃.
      return self.output
    
    # i. 걍 이렇게 그냥출력해버리면 굳이 Visualizer클래스를 다시만든 이유가 좀 없어지긴하는데, 일단 이렇게해서 결과 어케나오는지 먼저 체크하자. ->일단 히트맵 출력은 성공!!!
    ## i. ->수정했음. matplotlib 써서, 히트맵들 깔끔하게 플롯팅하고, 그 플롯이미지 자체를 통째로 넘파이어레이로 만들도록.
    def show_kplogitsj(self, kplogits_per_image):
      from matplotlib.gridspec import GridSpec
      from matplotlib.backends.backend_agg import FigureCanvasAgg
      # i. 이 메서드 호출 전에 VisImage객체(self.output)에 히트맵더해서크롭시킨 이미지어레이들 리스트 넣어줬나 체크.
      assert hasattr(self.output, 'heatmapaddedCroppedArr_listj'), "j) this method(show_kplogitsj) should be called AFTER set 'heatmapaddedCroppedArr_listj' in the VisImage object!!"
      croppedArr_list = self.output.heatmapaddedCroppedArr_listj # i. VisImage 객체에 내가 저장해놨던 box크롭된 이미지어레이들 리스트를 사용.
      # i. kplogits_per_image 는 (N x K x S x S) 형태. N 은 한 이미지 내의 디텍션된 물체들의 갯수. K,S,S는 아래설명대로.
      # i. kplogit_per_object 는 (K x S x S) 형태. K 는 키포인트갯수(내경우 6), S 는 키포인트 로짓의 가로세로 길이.
      num_objs_per_img = kplogits_per_image.size()[0]
      kpIdx2kpName = {0:"Lt b. level", 1:"Rt b. level", 2:"Lt apex", 3:"Rt apex", 4:"Lt top", 5:"Rt top"} # i. 일단 교수님도 봐야해서 내 어노테이션방식이랑 좌우 다르게 했음.(키포인트인덱스->키포인트명칭 맵핑용 딕셔너리임.)
      kpPlotRGBA_arr_list = []
      for objIdx, (kplogit_per_object, croppedArr) in enumerate(zip(kplogits_per_image, croppedArr_list)):
        ## i. 각 임플마다, 키포인트로짓들 보여줄 플롯 만들고,
        ## 이걸 self.output(VisImage객체)에 저장. ->걍 VisImage객체에 저장 안하는걸로. 일단.
        kp_fig = mpl.figure.Figure(constrained_layout=True, figsize=(6.4, 4.8), dpi=100)
        kp_gs = GridSpec(3, 4, figure=kp_fig) # i. 행3 열4 grid.
        kp_ax0 = kp_fig.add_subplot(kp_gs[:,:2])
        kp_ax1 = kp_fig.add_subplot(kp_gs[0,2])
        kp_ax2 = kp_fig.add_subplot(kp_gs[0,3])
        kp_ax3 = kp_fig.add_subplot(kp_gs[1,2])
        kp_ax4 = kp_fig.add_subplot(kp_gs[1,3])
        kp_ax5 = kp_fig.add_subplot(kp_gs[2,2])
        kp_ax6 = kp_fig.add_subplot(kp_gs[2,3])
        kp_ax_list = [kp_ax4, kp_ax3, kp_ax2, kp_ax1, kp_ax6, kp_ax5] # i. 프레딕션된 키포인트로짓 순서가 COCO형식으로 어노테이션해준 그 어노테이션 순서대로였었지 아마. 지금내경우엔 bone right, bone left, apex right, apex left, top right, top left 순서.(좌우는 내방식.)

        kp_fig.suptitle("Fixture{}/{} heatmaps".format(objIdx+1, num_objs_per_img), fontsize=14)

        kp_ax0.imshow(croppedArr, aspect='auto')
        kp_ax0.axis('off')
        kp_ax0.set_title('All points, Superimposed', fontsize=10)
                
        # i. 이런식으로 VisImage객체에 저장해줄까했는데, 일단 안하는걸로.
        # self.output.kp_fig = kp_fig
        # self.output.kp_ax0 = kp_ax0
        # self.output.kp_ax1 = kp_ax1
        # ...

        for kpIdx, (kplogit_per_kp, kp_ax) in enumerate(zip(kplogit_per_object, kp_ax_list)):
          kp_ax.axis('off')
          kp_ax.imshow(kplogit_per_kp, interpolation='sinc')
          kp_ax.set_title('{}'.format(kpIdx2kpName[kpIdx]), fontdict={'fontsize': 10, 'fontweight': 'medium', 'color':'black'})

          # 이전에 쓰던 코드. 이제 plt 사용 안함. plt 는 간편하게쓸때의 용도인듯.
          # plt.imshow(kplogit_per_kp, cmap='viridis')
          # plt.colorbar()
          # plt.title('Obj{}/{}) {} heatmap'.format(objIdx+1, num_objs_per_img, kpIdx2kpName[kpIdx]), fontsize = 14)
          # plt.show()

        # i. colorbar 추가. 되나몰겟네. 일단해보자.
        kp_fig.colorbar(mpl.cm.ScalarMappable(norm=None, cmap=None), cax=None, ax=kp_ax_list, use_gridspec=True)
        kp_canvas = FigureCanvasAgg(kp_fig)
        kp_canvas.draw()
        buf = kp_canvas.buffer_rgba() # i. canvas.buffer_rgba() 가 결국 canvas.renderer.buffer_rgba() 를 호출해서 리턴하는거임. 결국 같은것.
        kpPlotRGBA_arr = np.array(buf)
        kpPlotRGBA_arr_list.append(kpPlotRGBA_arr)

      # i. 이 리스트를 VisImage객체에 저장해주자. 뭐 꼭 이렇게 안해도되지만 걍.
      self.output.kpPlotRGBA_arr_listj = kpPlotRGBA_arr_list


    def overlay_instancesj(
        self,
        *,
        boxes=None,
        labels=None,
        masks=None,
        keypoints=None,
        kplogits_per_image, # i. 요거 추가함.
        assigned_colors=None,
        alpha=0.5
    ):
        """
        Args:
            boxes (Boxes, RotatedBoxes or ndarray): either a :class:`Boxes`,
                or an Nx4 numpy array of XYXY_ABS format for the N objects in a single image,
                or a :class:`RotatedBoxes`,
                or an Nx5 numpy array of (x_center, y_center, width, height, angle_degrees) format
                for the N objects in a single image,
            labels (list[str]): the text to be displayed for each instance.
            masks (masks-like object): Supported types are:

                * :class:`detectron2.structures.PolygonMasks`,
                  :class:`detectron2.structures.BitMasks`.
                * list[list[ndarray]]: contains the segmentation masks for all objects in one image.
                  The first level of the list corresponds to individual instances. The second
                  level to all the polygon that compose the instance, and the third level
                  to the polygon coordinates. The third level should have the format of
                  [x0, y0, x1, y1, ..., xn, yn] (n >= 3).
                * list[ndarray]: each ndarray is a binary mask of shape (H, W).
                * list[dict]: each dict is a COCO-style RLE.
            keypoints (Keypoint or array like): an array-like object of shape (N, K, 3),
                where the N is the number of instances and K is the number of keypoints.
                The last dimension corresponds to (x, y, visibility or score).
            assigned_colors (list[matplotlib.colors]): a list of colors, where each color
                corresponds to each mask or box in the image. Refer to 'matplotlib.colors'
                for full list of formats that the colors are accepted in.

        Returns:
            output (VisImage): image object with visualizations.
        """
        num_instances = None
        if boxes is not None:
            boxes = self._convert_boxes(boxes)
            num_instances = len(boxes)
        if masks is not None:
            masks = self._convert_masks(masks)
            if num_instances:
                assert len(masks) == num_instances
            else:
                num_instances = len(masks)
        if keypoints is not None:
            if num_instances:
                assert len(keypoints) == num_instances
            else:
                num_instances = len(keypoints)
            keypoints = self._convert_keypoints(keypoints)
        if labels is not None:
            assert len(labels) == num_instances
        if assigned_colors is None:
            assigned_colors = [random_color(rgb=True, maximum=1) for _ in range(num_instances)]
        if num_instances == 0:
            return self.output
        if boxes is not None and boxes.shape[1] == 5:
            return self.overlay_rotated_instances(
                boxes=boxes, labels=labels, assigned_colors=assigned_colors
            )

        # Display in largest to smallest order to reduce occlusion.
        areas = None
        if boxes is not None:
            areas = np.prod(boxes[:, 2:] - boxes[:, :2], axis=1)
        elif masks is not None:
            areas = np.asarray([x.area() for x in masks])

        if areas is not None:
            sorted_idxs = np.argsort(-areas).tolist()
            # Re-order overlapped instances in descending order.
            boxes = boxes[sorted_idxs] if boxes is not None else None
            labels = [labels[k] for k in sorted_idxs] if labels is not None else None
            masks = [masks[idx] for idx in sorted_idxs] if masks is not None else None
            assigned_colors = [assigned_colors[idx] for idx in sorted_idxs]
            keypoints = keypoints[sorted_idxs] if keypoints is not None else None

        for i in range(num_instances):
            color = assigned_colors[i]
            if boxes is not None:
                self.draw_box(boxes[i], edge_color=color)

            if masks is not None:
                for segment in masks[i].polygons:
                    self.draw_polygon(segment.reshape(-1, 2), color, alpha=alpha)

            if labels is not None:
                # first get a box
                if boxes is not None:
                    x0, y0, x1, y1 = boxes[i]
                    text_pos = (x0, y0)  # if drawing boxes, put text on the box corner.
                    horiz_align = "left"
                elif masks is not None:
                    x0, y0, x1, y1 = masks[i].bbox()

                    # draw text in the center (defined by median) when box is not drawn
                    # median is less sensitive to outliers.
                    text_pos = np.median(masks[i].mask.nonzero(), axis=1)[::-1]
                    horiz_align = "center"
                else:
                    continue  # drawing the box confidence for keypoints isn't very useful.
                # for small objects, draw text at the side to avoid occlusion
                instance_area = (y1 - y0) * (x1 - x0)
                if (
                    instance_area < _SMALL_OBJECT_AREA_THRESH * self.output.scale
                    or y1 - y0 < 40 * self.output.scale
                ):
                    if y1 >= self.output.height - 5:
                        text_pos = (x1, y0)
                    else:
                        text_pos = (x0, y1)

                height_ratio = (y1 - y0) / np.sqrt(self.output.height * self.output.width)
                lighter_color = self._change_color_brightness(color, brightness_factor=0.7)
                font_size = (
                    np.clip((height_ratio - 0.02) / 0.08 + 1, 1.2, 2)
                    * 0.5
                    * self._default_font_size
                )
                self.draw_text( ## i. 위에서 정해준 값들 넣어줌. bbox 상단 라벨 텍스트 그려줌.
                    labels[i],
                    text_pos,
                    color=lighter_color,
                    horizontal_alignment=horiz_align,
                    face_alphaj = 0.8,
                    font_size = font_size * 2, ## i. 상수좀 곱해서 크게해줌.

                    fontweight = 'semibold'
                )

        # draw keypoints   # i. 키포인트 로짓 정보도 같이 넘겨줌.
        if keypoints is not None:
            for keypoints_per_instance, kplogits_per_instance in zip(keypoints, kplogits_per_image):
                self.draw_and_connect_keypointsj(keypoints_per_instance, kplogits_per_instance)

        return self.output

    def draw_and_connect_keypointsj(self, keypoints, kplogits_per_instance): # i. 인풋인자에 내가 키포인트 로짓 추가함.
        """
        Draws keypoints of an instance and follows the rules for keypoint connections
        to draw lines between appropriate keypoints. This follows color heuristics for
        line color.

        Args:
            keypoints (Tensor): a tensor of shape (K, 3), where K is the number of keypoints
                and the last dimension corresponds to (x, y, probability).  # i. 맨마지막값 확률 아닐지도모름. 즉, 0~1사이의값이아닐지도모른다고. 지금 요 코멘트설명들이 죄다 100% 정확한건 아니니까.

        Returns:
            output (VisImage): image object with visualizations.
        """
        visible = {}
        keypoint_names = self.metadata.get("keypoint_names")
        # for idx, keypoint in enumerate(keypoints): # i. ->요 한줄 대신 아래 한줄처럼 변경.
        for idx, (keypoint, kplogits_for_onekp) in enumerate(zip(keypoints, kplogits_per_instance)):
            # draw keypoint
            x, y, prob = keypoint
            if prob > _KEYPOINT_THRESHOLD:
                if idx == 0 or idx ==1: # i. 키포인트가 bone right, bone left 인 경우.
                    self.draw_circle((x, y), color=_RED, radius = 14, linewidthj=4.5, fill=False, zorder=20) # i. draw_circle 메서드에 radius, fill, zorder 넣어줫음. 라인두께도 설정가능하게 빼줬음.
                else: # i. 그 외의 키포인트들.
                    self.draw_circle((x, y), color=(255/255, 0/255, 0/255, 1), radius = 10.5, fill=True, zorder=15)
                if keypoint_names:
                    keypoint_name = keypoint_names[idx]
                    visible[keypoint_name] = (x, y)
                # i. 이쯤에 키포인트 로짓 값을 출력해줘보자.
                self.draw_text(
                    # round(float(kplogits_for_onekp.max()),2), # 출력할 텍스트 내용. - 일단 해당 키포인트(하나)의 로짓값들중 최대값을 출력해줘봄.
                    '{}/{}'.format(round(float(kplogits_for_onekp.max()),1), round(float(prob),2)), # 출력할 텍스트 내용. - 일단 해당 키포인트(하나)의 로짓값들중 최대값을 출력해줘봄. ## i. 2020.06.21.추가) prob 값도 출력해봄. 뭔지 좀 보게.
                    (x+10,y-9), # 포지션. 일단출력먼저하고 나중에 수정.
                    font_size= self._default_font_size * 1.4, # 일단걍해보고 나중에 수정.
                    color= (150/255, 250/255, 50/255, 0.8), # 일단 "g"(green일거임) 넣어보고 나중에 수정.->RGBA값으로해줘봄.튜플.
                    facecolorj=(0/255, 0/255, 0/255), # RGBA, 0~1사이의값들로구성. -> 아.근데 알파값은 어차피 요바로아래서정해주는걸로 적용되나봄. 걍 RGB(3가지값)튜플로 해줘봄.
                    face_alphaj=0,
                    horizontal_alignment="left", # see 'matplotlib.text.Text'
                    rotation=0,

                    fontweight = 'semibold'                
                )

        ## i. 2020.06.21.추가) 전체 fixture 길이 대비 bone loss 되지 않은 픽스쳐부분의 비율 시각화출력.
        ## 1) apex, bone level, top 세군데에 대해 좌우 포인트를 평균내서 중간포인트를 구함(총 3개 중간포인트).
        apex_x, apex_y        =  (keypoints[3][:2]+keypoints[2][:2])/2
        bonelvl_x, bonelvl_y  =  (keypoints[1][:2]+keypoints[0][:2])/2
        top_x, top_y          =  (keypoints[5][:2]+keypoints[4][:2])/2
        ## 2) 중간포인트들을 이용해서 다음을 구함: 전체픽스쳐길이, 본컨택된픽스쳐길이, (전체픽스쳐길이 대비)본컨택된픽스쳐부위의 비율. 
        import math        
        tot_fixture_len = math.sqrt((apex_x-top_x)**2 + (apex_y-top_y)**2)
        osseo_fixture_len = math.sqrt((apex_x-bonelvl_x)**2 + (apex_y-bonelvl_y)**2)
        osseo_fixture_pct = round((osseo_fixture_len/tot_fixture_len)*100, 1) ## 본컨택된픽스쳐부위의 비율.
        boneLossCls = 'Normal' if osseo_fixture_pct>=90 else 'Early' if osseo_fixture_pct>=75 else 'Moderate' if osseo_fixture_pct>=50 else 'Severe' ## 본컨택된픽스쳐부위의 비율을 이용해서 클래스 분류.
        ## 3) 본컨택된픽스쳐부위의 비율, 분류결과 시각화 출력.
        self.draw_text( ## 비율 출력(예: 73.55% 이런식).
            'MBL {}%'.format(round(100-osseo_fixture_pct, 1)), # 출력할 텍스트 내용.
            ((apex_x+top_x)/2, (apex_y+top_y)/2 +15), # 포지션. 일단 픽스쳐의 한가운데로 잡아봄. 일단출력먼저하고 나중에 수정.
            font_size= self._default_font_size * 2.5, # 기본값에 3곱해줘봄. 일단걍해보고 나중에 수정.
            color= (127/255, 0/255, 255/255, 1.0), # 일단 "g"(green일거임) 넣어보고 나중에 수정.->RGBA값으로해줘봄.튜플.
            facecolorj=(0/255, 0/255, 0/255), # RGBA, 0~1사이의값들로구성. -> 아.근데 알파값은 어차피 요바로아래서정해주는걸로 적용되나봄. 걍 RGB(3가지값)튜플로 해줘봄.
            face_alphaj=0,
            horizontal_alignment="center", # see 'matplotlib.text.Text'
            rotation=0,
            zorderj=50,

            alpha = 1.0,
            fontfamily = 'cursive',
            fontweight = 'semibold'
        )
        self.draw_text( ## 분류결과 출력(예: Early 이런식).
            '{}'.format(boneLossCls), # 출력할 텍스트 내용.
            ((apex_x+top_x)/2, (apex_y+top_y)/2 -50), # 포지션. 일단 픽스쳐의 한가운데로 잡아봄. 일단출력먼저하고 나중에 수정.
            font_size= self._default_font_size * 3, # 기본값에 3곱해줘봄. 일단걍해보고 나중에 수정.
            color= (0/255, 0/255, 204/255, 1.0), # 일단 "g"(green일거임) 넣어보고 나중에 수정.->RGBA값으로해줘봄.튜플.
            facecolorj=(0/255, 0/255, 0/255), # RGBA, 0~1사이의값들로구성. -> 아.근데 알파값은 어차피 요바로아래서정해주는걸로 적용되나봄. 걍 RGB(3가지값)튜플로 해줘봄.
            face_alphaj=0,
            horizontal_alignment="center", # see 'matplotlib.text.Text'
            rotation=0,
            zorderj=50,

            alpha = 1.0,
            fontfamily = 'Helvetica',
            fontweight = 'bold'                
        )

        if self.metadata.get("keypoint_connection_rules"):
            for kp0, kp1, color in self.metadata.keypoint_connection_rules:
                if kp0 in visible and kp1 in visible:
                    x0, y0 = visible[kp0]
                    x1, y1 = visible[kp1]
                    color = tuple(x / 255.0 for x in color)
                    self.draw_line([x0, x1], [y0, y1], color=color, linestyle="-", linewidth=7, zorder=5) # i. linestyle, linewidth, zorder 넣어줌. linewidth=None 이엇는데 2로 바꿔줘봄.
        return self.output

    ## i. 2020.06.24.수욜.저녁늦게.) bbox 테두리 선 두께 더굵게해주려고 요 draw_box 함수도 붙여넣어서 overwrite 해줘봄.
    def draw_box(self, box_coord, alpha=0.7, edge_color="g", line_style="-"): 
        """
        Args:
            box_coord (tuple): a tuple containing x0, y0, x1, y1 coordinates, where x0 and y0
                are the coordinates of the image's top left corner. x1 and y1 are the
                coordinates of the image's bottom right corner.
            alpha (float): blending efficient. Smaller values lead to more transparent masks.
            edge_color: color of the outline of the box. Refer to `matplotlib.colors`
                for full list of formats that are accepted.
            line_style (string): the string to use to create the outline of the boxes.

        Returns:
            output (VisImage): image object with box drawn.
        """
        x0, y0, x1, y1 = box_coord
        width = x1 - x0
        height = y1 - y0

        # linewidth = max(self._default_font_size / 4, 1)
        linewidth = max(self._default_font_size / 4, 6) ## i. 더 두껍게해주려고.

        self.output.ax.add_patch(
            mpl.patches.Rectangle(
                (x0, y0),
                width,                
                height,
                fill=False,
                edgecolor=edge_color,
                linewidth=linewidth * self.output.scale,
                alpha=alpha,
                linestyle=line_style,
            )
        )
        return self.output


    def draw_text(
        self,
        text,
        position,
        *,
        font_size=None,
        color="g",
        facecolorj="black",
        face_alphaj=0.8,
        horizontal_alignment="center",
        rotation=0,
        zorderj=10,
        **kwargsj
    ):
        """
        Args:
            text (str): class label
            position (tuple): a tuple of the x and y coordinates to place text on image.
            font_size (int, optional): font of the text. If not provided, a font size
                proportional to the image width is calculated and used.
            color: color of the text. Refer to `matplotlib.colors` for full list
                of formats that are accepted.
            horizontal_alignment (str): see `matplotlib.text.Text`
            rotation: rotation angle in degrees CCW

        Returns:
            output (VisImage): image object with text drawn.
        """
        if not font_size:
            font_size = self._default_font_size

        # since the text background is dark, we don't want the text to be dark
        color = np.maximum(list(mplc.to_rgb(color)), 0.2)
        color[np.argmax(color)] = max(0.8, np.max(color))

        x, y = position
        self.output.ax.text(
            x,
            y,
            text,
            size=font_size * self.output.scale,
            family="sans-serif",
            bbox={"facecolor": facecolorj, "alpha": face_alphaj, "pad": 0.7, "edgecolor": "none"},
            verticalalignment="top",
            horizontalalignment=horizontal_alignment,
            color=color,
            zorder=zorderj,
            rotation=rotation,
            **kwargsj
        )
        return self.output

    # i. zorder 값 넣어주려고 draw_circle, draw_line 함수 오버라이트 해줌. -> zorder 값 넣어줬더니 키포인트(circle)랑 라인 수직순서 바꾸는거 성공!!
    def draw_circle(self, circle_coord, color, radius=3, linewidthj=None, fill=True, zorder=20): # i. fill, zorder 넣어줌.
        """
        Args:
            circle_coord (list(int) or tuple(int)): contains the x and y coordinates
                of the center of the circle.
            color: color of the polygon. Refer to `matplotlib.colors` for a full list of
                formats that are accepted.
            radius (int): radius of the circle.

        Returns:
            output (VisImage): image object with box drawn.
        """
        x, y = circle_coord
        self.output.ax.add_patch(
            mpl.patches.Circle(circle_coord, radius=radius, linewidth=linewidthj, fill=fill, color=color, zorder=zorder) # i. fill, zorder 바꿔줫음.
        )
        return self.output

    def draw_line(self, x_data, y_data, color, linestyle="-", linewidth=None, zorder=5): # i. zorder 넣어줫음.
        """
        Args:
            x_data (list[int]): a list containing x values of all the points being drawn.
                Length of list should match the length of y_data.
            y_data (list[int]): a list containing y values of all the points being drawn.
                Length of list should match the length of x_data.
            color: color of the line. Refer to `matplotlib.colors` for a full list of
                formats that are accepted.
            linestyle: style of the line. Refer to `matplotlib.lines.Line2D`
                for a full list of formats that are accepted.
            linewidth (float or None): width of the line. When it's None,
                a default value will be computed and used.

        Returns:
            output (VisImage): image object with line drawn.
        """
        if linewidth is None:
            linewidth = self._default_font_size / 3
        linewidth = max(linewidth, 1)
        self.output.ax.add_line(
            mpl.lines.Line2D(
                x_data,
                y_data,
                linewidth=linewidth * self.output.scale,
                color=color,
                linestyle=linestyle,
                zorder=zorder # i. zorder 값 넣어줌.
            )
        )
        return self.output

    # i. 카테고리(클래스)가 1개더라도 시각화결과에 카테고리명 표기해주려고 내가 아주살짝 수정해줌(>1 을 >=1 로만 바꿔줌). 잘 작동함. - Det2 의 원래코드에선 카테고리갯수가 2개이상이어야 카테고리명 표기하고, 1개면 그냥 확률값(몇%인지)만 표기하도록 되어있었음.
    # 원래 Det2 소스코드에선 Visualizer 클래스의 외부에 정의된 함수였는데, 내가 걍 Visualizer_kplogitsj 안에다가 넣어줘봤음.
    def _create_text_labelsj(self, classes, scores, class_names):
      """
      Args:
          classes (list[int] or None):
          scores (list[float] or None):
          class_names (list[str] or None):

      Returns:
          list[str] or None
      """
      ######
      # i. 걍 어노테이션json파일에 내가 적어줬던 카테고리명(impj라고 해논상태지) 무시하고 새로 카테고리명 넣어줄거면 요기다가 이런식으로 적어주면 시각화결과에 요대로 출력되겠지. 잘 작동함.
      class_names = ["fixture_upper"]
      ######
      labels = None
      if classes is not None and class_names is not None and len(class_names) >= 1:
          labels = [class_names[i] for i in classes]
          #####
          # i. 내가 아래 코드 추가해서 조금 변형해줌. 예를들어 한 이미지에 물체가 5개 있고 그중 3번째 물체라 치면, Obj3/5) fixture_upper 99% 이런식으로 bbox 에 표시되도록.
          num_objs_per_img = len(labels)
          labels = [ "{}/{}) {}".format(idx+1, num_objs_per_img, label) for idx, label in enumerate(labels)] # i. 요정도 형변환(숫자->스트링)정도는 파이썬에선 자동으로 해줌.
          #####
      if scores is not None:
          if labels is None:
              labels = ["{:.0f}%".format(s * 100) for s in scores]
          else:
              labels = ["{} {:.0f}%".format(l, s * 100) for l, s in zip(labels, scores)]
      return labels

#################################################################################################################################################################################################









######################################### i. 시각화결과 보여주는 코드(Visualizer_kplogitsj 클래스 이용해서)를 함수화했음. 외부에서 요놈을 임포트하기좋게. ###################################################################################

def visualizeCodeFct_j(val_imgs_pathj, predictor, Visualizer_kplogitsj, MetadataCatalog, my_val_dataset_namej): 
    #@ i. ->일단 딱 val_imgs_pathj만 인풋인자로 해서 함수화해봄. predictor, Visualizer_kplogitsj 등도 인풋인자로 받아야하나? 일단 요렇게만 해서 해보자.
    #@ i. ->역시 안되네 ㅋㅋ. predictor, Visualizer_kplogitsj 도 인풋인자로 해주자.

    ## i. 드뎌 내가 수정해준 Visualizer_kplogitsj 클래스 사용!!
    # %cd /content
    val_img_filename_list = os.listdir(val_imgs_pathj)
    val_img_filename_list = [fname for fname in val_img_filename_list if '.json' not in fname] ## i. 폴더에 어노테이션json파일 있어서, 그놈은 제외하려고 넣어준 코드.
    print('j) for {} test images...'.format(len(val_img_filename_list)))
    ### i. 자꾸 코랩 다운돼서 일단 5개만 해줘봄.
    ####  ->이유는몰겟는데 이제 36개val데이타셋 다돌려도 다운안됨. 근데 시간오래걸려서 걍 5개만해놨음.
    for test_img_filename in val_img_filename_list[:20]: 
        testimg_arr = cv2.imread(os.path.join(val_imgs_pathj, test_img_filename))
        # 요기서 predictions는 {"instances": (Instances클래스의인스턴스)} 의 형태를 가진 딕셔너리일거임. - 내가 vscode로 공부중인 디텍트론2플젝의 DefaultTrainer코드에 코멘트 상세히 적어놨음.
        # 실제로 출력해봐도 그렇고. 죠 아래에서도 predictions["instances"] 로 값을 꺼내오고있고.
        pred_pa_kp_upper = predictor(testimg_arr)
        # print('j) pred_pa_kp_upper:', pred_pa_kp_upper) # i. 2020.06.21.) 키포인트에대한 스코어값이 들어있었나 체크해보려고 출력해봣는데, 역시 없음. 옵젝디텍션 스코어만 있을 뿐임.
        visualizer = Visualizer_kplogitsj(
                    testimg_arr[:, :, ::-1],                   
                    metadata=MetadataCatalog.get(my_val_dataset_namej),
                    scale=1.0,
                    # i. 일단요거없애고해보자.
                    # instance_mode=ColorMode.IMAGE_BW   # remove the colors of unsegmented pixels
        )
        # i. 에러뜨네. ColorMode.IMAGE_BW 는 세그멘테이션이 필수라고. predictions.has("pred_masks")의 값이 없는걸로 봐서, (요 모델 또는 predictor에서)마스크는 출력을 안하도록 일단은 되어잇는건가??? 마스크도 출력하도록 바꿔보자!!!

        # i. 요기서 코랩벌룬실습에선 .to("cpu")로 해줬었고 나도 쭉 글케 해왔는데, .to("gpu")로 바꿔서도 함 해보자 뭐 다른게 있나 혹시 더 빠른가. -> 에러뜨네. RuntimeError: Expected one of cpu, cuda, mkldnn, opengl, opencl, ideep, hip, msnpu device type at start of device string: gpu
        visImage = visualizer.draw_instance_predictions(pred_pa_kp_upper["instances"].to("cpu"))  
        pred_drawed_testimg_arr = visImage.get_image()
        pred_drawed_testimg_arr_resized = cv2.resize(pred_drawed_testimg_arr, tuple(int(round(0.5*i)) for i in pred_drawed_testimg_arr.shape[:2][::-1]), interpolation=cv2.INTER_AREA) # i. 이미지 넘 커서 리사이즈. Visualizer객체 이니셜라이즈할때 scale 정해주면 되는데, 지금 scale값 1인상태로 히트맵추가등 다 해줘버려서, 걍 이렇게 리사이즈해줌 일단.
        #@ i. 원래 이 코드들 구글코랩에서 작성한거라, 코랩에서 제공하는 cv2_imshow 를 사용했었음(from google.colab.patches import cv2_imshow).
        #@    근데, 지금이걸(visualizeCodeFct_j 함수) 코랩에서 임포트해서 쓸라니까 코랩상에서 임포트해준것들은 작동이 안되어서(cv2_imshow 뿐만아니라 os, np, cv2 등 죄다 작동안됨. 지금 이 모듈에서 임포트해줘야함.),
        #@    그래서 cv2_imshow 대신 cv2.imshow 를 사용해줘봄.
        #@  -> 안되네. DisabledFunctionError: cv2.imshow() is disabled in Colab, because it causes Jupyter sessions to crash; As a substitution, consider using 'from google.colab.patches import cv2_imshow' 라고 뜸.
        #@     걍 이모듈의 저위에다가 from google.colab.patches import cv2_imshow 해줘보자.. 될라나..
        cv2_imshow(pred_drawed_testimg_arr_resized[:, :, ::-1]) # i. 디텍션한 bbox, keypoints 그려준 이미지어레이 보여줌.@@@@@@@@@@@@@@@@@@(출력1)
        # cv2.imwrite("./drive/My Drive/PA_kp_paper_resultImages/{}_predDrawed.png".format(test_img_filename), pred_drawed_testimg_arr[:, :, ::-1]) # i. 이미지 저장.
        # print("j) {}_predDrawed.png saved!".format(test_img_filename))

        ### i. (드디어...) 인풋이미지(여기선PA이미지)상에 히트맵 그려준거 출력해보자 (matplotlib 관련 공부 다 했고... 지금 2020.05.27.수욜저녁임.)
        visualizer.draw_kplogitsj(pred_pa_kp_upper["instances"].to("cpu"))
        pred_drawed_testimg_heatmapadded_arr = visImage.get_image()
        pred_drawed_testimg_heatmapadded_arr_resized = cv2.resize(pred_drawed_testimg_heatmapadded_arr, tuple(int(round(0.5*i)) for i in pred_drawed_testimg_heatmapadded_arr.shape[:2][::-1]), interpolation=cv2.INTER_AREA) # i. 이미지 넘 커서 리사이즈. Visualizer객체 이니셜라이즈할때 scale 정해주면 되는데, 지금 scale값 1인상태로 히트맵추가등 다 해줘버려서, 걍 이렇게 리사이즈해줌 일단.
        cv2_imshow(pred_drawed_testimg_heatmapadded_arr_resized[:, :, ::-1]) # i. 위의결과에 추가로 히트맵까지 더해준 이미지어레이 보여줌.@@@@@@@@@@@@@@@@@@(출력2)
        # cv2.imwrite("./drive/My Drive/PA_kp_paper_resultImages/{}_predDrawed-Heatmapadded.png".format(test_img_filename), pred_drawed_testimg_heatmapadded_arr[:, :, ::-1]) # i. 이미지 저장.
        # print("j) {}_predDrawed-Heatmapadded.png saved!".format(test_img_filename))

        ### i. 히트맵까지 더해진걸 box 크롭해서 보여주는것도 추가. ->보여주는건 취소, box크롭한 어레이들을 리스트에 담아서 visImage객체에 넣어줌.
        visImage.heatmapaddedCroppedArr_listj = [] # i. box 크롭된 이미지어레이를 담을 리스트 만듦.
        for i in visImage.boxCoordsTuple_listj: # i. 위에서 호출한 draw_kplogitsj 메서드에서 visImage 객체에 boxCoordsTuple_listj 를 만들어놨음.
            croppedArrj = pred_drawed_testimg_heatmapadded_arr[i[1]:i[3], i[0]:i[2]]
            visImage.heatmapaddedCroppedArr_listj.append(croppedArrj)
            # cv2_imshow(croppedArrj[:, :, ::-1]) # i. box 크롭된거 보여줌.(히트맵까지 더해준 이미지어레이를 box대로 크롭한거) -> 일단 코멘트아웃. matplotlib 이용해서 플롯으로 한꺼번에 정리해서 보여주려고.
        ### i. 히트맵들 플롯팅해서 정리한거 보여줌.
        visualizer.show_kplogitsj(pred_pa_kp_upper["instances"].to("cpu").pred_keypoint_logits)
        num_detectedObjs = len(visImage.kpPlotRGBA_arr_listj)
        for idx, i in enumerate(visImage.kpPlotRGBA_arr_listj): # i. 위에서 호출한 show_kplogitsj 메서드에서 visImage 객체에 kpPlotRGBA_arr_listj 를 만들어놨음.
            cv2_imshow(i[:,:,[2,1,0,3]]) # i. 히트맵들 플롯팅해서 정리한거 보여줌.@@@@@@@@@@@@@@@@@@(출력3)
            # cv2.imwrite("./drive/My Drive/PA_kp_paper_resultImages/{}_predHeatmapPlot{}over{}.png".format(test_img_filename, idx+1, num_detectedObjs), i[:,:,[2,1,0,3]]) # i. 이미지 저장.
            # print("j) {}_predHeatmapPlot{}over{}.png saved!".format(test_img_filename, idx+1, num_detectedObjs))
            # i. 위에서 [2,1,0,3]이 뭐냐면, RGBA 를 BGRA 로 바꿔준거임. - 위의 for문의 각 i 가 RGBA로 된 이미지(넘파이어레이)인데, opencv 의 imshow 는 BGR 또는 BGRA 를 받기때문에.
        
        print('------------------------------------------------------------')

######################################################################################################################################################################################################
