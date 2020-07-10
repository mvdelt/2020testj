# 2020.05.20.수욜. 내코랩플젝 어떤 셀 백업. - 코랩이 잠시 이상해져서 세이브가 안돼서 이렇게 백업해둔거임.
# -> 다시 코랩으로 복사 완료. 이제 이파일(colabBackupj.py)은 지워도 됨.

try:

  ## i. Det2의 Visualizer 클래스를 수정.
  ## i. 음.......이상함........ from A.B.C import D 라고 하면, C 가 모듈(.py파일)이라면, C가 다 실행되지않음? 그럼 실행됐으니까 메모리?에 올라갓든지 뭐글케돼서 굳이 임포트를 또 시켜올필요없는거아닌가??? 아닌가... 흠.....
  from detectron2.utils.visualizer import Visualizer, ColorMode
  import matplotlib as mpl
  ## i. 아 자꾸 변수 디파인안됏다고떠서 걍 싹다 (Det2소스코드로부터)복사해서 요기 붙여놓은거임. 지금내플젝에선 안쓰이는것도있을거임.
  _KEYPOINT_THRESHOLD = 0.05
  _SMALL_OBJECT_AREA_THRESH = 1000
  _LARGE_MASK_AREA_THRESH = 120000
  _OFF_WHITE = (1.0, 1.0, 240.0 / 255)
  _BLACK = (0, 0, 0)
  _RED = (1.0, 0, 0)
  class Visualizer_kplogitsj(Visualizer):
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
      self.overlay_instances(
          masks=masks,
          boxes=boxes,
          labels=labels,
          keypoints=keypoints,
          assigned_colors=colors,
          alpha=alpha,
      )
      # i. 내가만든함수사용.
      print('kplogits_per_image:',kplogits_per_image)
      self.show_kp_logitsj(kplogits_per_image)
      return self.output
    
    # i. 걍 이렇게 그냥출력해버리면 굳이 Visualizer클래스를 다시만든 이유가 좀 없어지긴하는데, 일단 이렇게해서 결과 어케나오는지 먼저 체크하자. ->일단 히트맵 출력은 성공!!!
    def show_kp_logitsj(self, kplogits_per_image):
      import matplotlib.pyplot as plt
      # i. kplogits_per_image 는 (N x K x S x S) 형태. N 은 한 이미지 내의 디텍션된 물체들의 갯수. K,S,S는 아래설명대로.
      # i. kplogit_per_object 는 (K x S x S) 형태. K 는 키포인트갯수(내경우 6), S 는 키포인트 로짓의 가로세로 길이.
      for kplogit_per_object in kplogits_per_image:
        for kplogit_per_kp in kplogit_per_object:
          plt.imshow(kplogit_per_kp, cmap='viridis')
          plt.colorbar()
          plt.show()


    # # i. 키포인트랑 키포인트연결하는라인 그려주는 순서만 뒤바꾸려고 내가 수정해줬음. -> 그려지는순서 안바뀌네?? 이 함수의 코드실행순서대로 그려지는게 아닌건가??
    # def draw_and_connect_keypoints(self, keypoints):
    #   """
    #   Draws keypoints of an instance and follows the rules for keypoint connections
    #   to draw lines between appropriate keypoints. This follows color heuristics for
    #   line color.

    #   Args:
    #       keypoints (Tensor): a tensor of shape (K, 3), where K is the number of keypoints
    #           and the last dimension corresponds to (x, y, probability).  # i. 맨마지막값 확률 아닐지도모름. 즉, 0~1사이의값이아닐지도모른다고. 지금 요 코멘트설명들이 죄다 100% 정확한건 아니니까.

    #   Returns:
    #       output (VisImage): image object with visualizations.
    #   """
    #   visible = {}
    #   keypoint_names = self.metadata.get("keypoint_names")
    #   for idx, keypoint in enumerate(keypoints):
    #       # draw keypoint -> # i. 여기선 그려주진않음. 라인보다 키포인트를 더 위에 그려주려고 저 아래에서 그려주도록 햇음 내가. 라인에 덮여서 키포인트들이 잘 안보여서.
    #       x, y, prob = keypoint
    #       if prob > _KEYPOINT_THRESHOLD:
    #           # self.draw_circle((x, y), color=_RED)
    #           if keypoint_names:
    #               keypoint_name = keypoint_names[idx]
    #               visible[keypoint_name] = (x, y)
    #   if self.metadata.get("keypoint_connection_rules"):
    #       for kp0, kp1, color in self.metadata.keypoint_connection_rules:
    #           if kp0 in visible and kp1 in visible:
    #               x0, y0 = visible[kp0]
    #               x1, y1 = visible[kp1]
    #               color = tuple(x / 255.0 for x in color)
    #               self.draw_line([x0, x1], [y0, y1], color=color)
    #   # i. 위에서 라인 그려줬으니, 이제 키포인트 그리자(기존에는 키포인트먼저그리고 그위에 라인그려서, 키포인트가 라인에 가려져서 잘 안보였었음.).
    #   for idx, keypoint in enumerate(keypoints):
    #       # draw keypoint
    #       x, y, prob = keypoint
    #       if prob > _KEYPOINT_THRESHOLD:
    #           self.draw_circle((x, y), color=_OFF_WHITE) # i. _RED 에서 _OFF_WHITE 로 바꿔줘봄. 내의도대로 써클이 라인 위로 안올라가서(그대로 아래에 깔려잇음) 지금 이 함수 실행된거 맞나 보려고.. ->실행 잘 되네.. 근데 z order(수직순서)는 안바뀌는거네..            
    #   return self.output


    def draw_and_connect_keypoints(self, keypoints):
        """
        Draws keypoints of an instance and follows the rules for keypoint connections
        to draw lines between appropriate keypoints. This follows color heuristics for
        line color.

        Args:
            keypoints (Tensor): a tensor of shape (K, 3), where K is the number of keypoints
                and the last dimension corresponds to (x, y, probability).

        Returns:
            output (VisImage): image object with visualizations.
        """
        visible = {}
        keypoint_names = self.metadata.get("keypoint_names")
        for idx, keypoint in enumerate(keypoints):
            # draw keypoint
            x, y, prob = keypoint
            if prob > _KEYPOINT_THRESHOLD:
                self.draw_circle((x, y), color=_RED, radius = 10, fill=False, zorder=20) # i. radius, fill, zorder 넣어줫음.
                if keypoint_names:
                    keypoint_name = keypoint_names[idx]
                    visible[keypoint_name] = (x, y)

        if self.metadata.get("keypoint_connection_rules"):
            for kp0, kp1, color in self.metadata.keypoint_connection_rules:
                if kp0 in visible and kp1 in visible:
                    x0, y0 = visible[kp0]
                    x1, y1 = visible[kp1]
                    color = tuple(x / 255.0 for x in color)
                    self.draw_line([x0, x1], [y0, y1], color=color, linestyle="-", linewidth=None, zorder=5) # i. linestyle, linewidth, zorder 넣어줌. 

        return self.output

    # i. zorder 값 넣어주려고 draw_circle, draw_line 함수 오버라이트 해줌. -> zorder 값 넣어줬더니 키포인트(circle)랑 라인 수직순서 바꾸는거 성공!!
    def draw_circle(self, circle_coord, color, radius=3, fill=True, zorder=20): # i. fill, zorder 넣어줌.
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
            mpl.patches.Circle(circle_coord, radius=radius, fill=fill, color=color, zorder=zorder) # i. fill, zorder 바꿔줫음.
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
      if scores is not None:
          if labels is None:
              labels = ["{:.0f}%".format(s * 100) for s in scores]
          else:
              labels = ["{} {:.0f}%".format(l, s * 100) for l, s in zip(labels, scores)]
      return labels





  test_img_filename_list = os.listdir(test_imgs_pathj)
  for test_img_filename in test_img_filename_list:
    testimg_arr = cv2.imread(os.path.join(test_imgs_pathj, test_img_filename))
    # 요기서 predictions는 {"instances": (Instances클래스의인스턴스)} 의 형태를 가진 딕셔너리일거임. - 내가 vscode로 공부중인 디텍트론2플젝의 DefaultTrainer코드에 코멘트 상세히 적어놨음.
    # 실제로 출력해봐도 그렇고. 죠 아래에서도 predictions["instances"] 로 값을 꺼내오고있고.
    pred_pa_kp_upper = predictor(testimg_arr)
    visualizer = Visualizer_kplogitsj(
                  testimg_arr[:, :, ::-1],                   
                  metadata=MetadataCatalog.get(my_dataset_namej),
                  scale=1, 
                  # i. 일단요거없애고해보자.
                  # instance_mode=ColorMode.IMAGE_BW   # remove the colors of unsegmented pixels
    )
    # i. 에러뜨네. ColorMode.IMAGE_BW 는 세그멘테이션이 필수라고. predictions.has("pred_masks")의 값이 없는걸로 봐서, (요 모델 또는 predictor에서)마스크는 출력을 안하도록 일단은 되어잇는건가??? 마스크도 출력하도록 바꿔보자!!!

    # i. 요기서 코랩벌룬실습에선 .to("cpu")로 해줬었고 나도 쭉 글케 해왔는데, .to("gpu")로 바꿔서도 함 해보자 뭐 다른게 있나 혹시 더 빠른가. -> 에러뜨네. RuntimeError: Expected one of cpu, cuda, mkldnn, opengl, opencl, ideep, hip, msnpu device type at start of device string: gpu
    visImage = visualizer.draw_instance_predictions(pred_pa_kp_upper["instances"].to("cpu"))  
    pred_drawed_testimg_arr = visImage.get_image()
    cv2_imshow(pred_drawed_testimg_arr[:, :, ::-1])

    ## i. keypoint logits ("heatmap") 출력해줘보자.
    ## 그니까 지금, 코드 흐름에서, 중간에 키포인트 로짓이 출력되는데 그게 다른함수의 인풋으로 들어가는거임. 즉, 키포인트 로짓은 최종적으로 밖으로 출력되진 않는다는거임. 내부적으로만 값이 만들어졋다가 사용되어버리는거지.
    ## 이 중간값을 밖으로 출력시키려면 어떻게 해야되느냐 이거지.
    ## 아마도 일반적인 OOP에서는(OOP말고 다른방식도 마찬가지겟지?), 이게 쉽지않은문제인듯..?? 내가원하는 그 값을 출력하는 함수 하나만 달랑 실행시킬수가 없음. 왜냐면 그 함수에 인풋값들을 넣어줘야하는데, 그 인풋값들은 또 다른함수들로부터 오고...그러기때문에.
    ## 그래서, 디텍트론2개발자도 이렇게 말하고잇음:
    ## "The output of the model does not contain *intermediate* heatmap information.(i. "intermediate" 라고 말하고잇음. 내부적으로 중간에 생성되었다가 사용되는 정보란거임.)
    ## If you need, one option is to write your own ROIHeads and overwrite its _forward_keypoint method so it does not contain the line above."
    ## -> 즉, 중간에생성되엇다가사용되는 정보가, 모델의 최종 아웃풋에는 들어잇지 않으니, ROIHeads 클래스를 새로 작성해서(기존 ROIHeads를 상속해서겟지물론) _forward_keypoint 함수를 새로작성(덮어쓰기)하란거지.
    ## (참고: https://github.com/facebookresearch/detectron2/issues/754 , 추가참고: https://github.com/facebookresearch/detectron2/issues/965, https://github.com/facebookresearch/detectron2/issues/319#issuecomment-565773345) 
    ##
    ## 자!!! 이제 그럼 그렇게 함 해보자!!!!!!!!!!
        


except:
  playMusicj(music_ErrorMusic)  
  raise