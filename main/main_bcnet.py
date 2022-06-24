from detectron2.config import get_cfg
from detectron2.data.detection_utils import read_image
from detectron2.utils.logger import setup_logger

import argparse
import torch

from detectron2.engine.defaults import DefaultPredictor

import numpy as np
def setup_cfg(args):
    # load config from file and command-line arguments
    cfg = get_cfg()
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    # Set score_threshold for builtin models
    cfg.MODEL.RETINANET.SCORE_THRESH_TEST = args.confidence_threshold
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = args.confidence_threshold
    cfg.MODEL.FCOS.INFERENCE_TH = args.confidence_threshold
    cfg.MODEL.PANOPTIC_FPN.COMBINE.INSTANCES_CONFIDENCE_THRESH = args.confidence_threshold
    cfg.freeze()
    return cfg


def get_parser():
    parser = argparse.ArgumentParser(description="Detectron2 demo for builtin models")
    parser.add_argument(
        "--config-file",
        default="configs/fcos/fcos_imprv_R_101_FPN.yaml",
        metavar="FILE",
        help="path to config file",
    )
    parser.add_argument("--webcam", action="store_true", help="Take inputs from webcam.")
    parser.add_argument("--video-input", help="Path to video file.")
    parser.add_argument("--input", nargs="+", help="A list of space separated input images")
    parser.add_argument(
        "--output",
        help="A file or directory to save output visualizations. "
        "If not given, will show output in an OpenCV window.",
    )

    parser.add_argument(
        "--confidence-threshold",
        type=float,
        default=0.4,
        help="Minimum score for instance predictions to be shown",
    )
    parser.add_argument(
        "--opts",
        help="Modify config options using the command-line 'KEY VALUE' pairs",
        default=["MODEL.WEIGHTS", "./models/model_0001999.pth"],
        nargs=argparse.REMAINDER,
    )
    return parser

class BCNet:
    def __init__(self) -> None:
        self.args = get_parser().parse_args()
        self.cfg = setup_cfg(self.args)
        self.cpu_device = torch.device("cpu")
        self.predictor = DefaultPredictor(self.cfg)
        
        #初始化检测原始输出信息
        self.obj_boxes = []
        self.obj_classes = []
        self.obj_scores = []
        self.obj_centers = []
        self.obj_masks_points = []
        self.obj_contours = []

        #初始化目标输出
        self.obj_dis_external = []#外径、长度
        self.obj_dis_internal = []#内径、宽度

        #边缘点坐标定义
        self.co_ext_2d = []
        self.co_int_2d = []
        self.co_ext_3d = []
        self.co_int_3d = []
        
    def detect(self, bgr_frame):
        """
        检测图片中的目标物

        Parameters:
        -----------
        bgr_frame 	   : 
                        三通道彩色图片 类型为numpy.ndarray shape为 (480, 640, 3)

        Return:
        -----------
        obj_classes 	   : 
                        检测到的物品类别  类型为numpy.ndarray 取值0或1 shape为(检测到的物体数量,)
        masks 	   : 
                        检测到的物品掩膜 类型为numpy.ndarray 取值True或False shape为(检测到的物体数量, 480, 640)
        centers 	   : 
                        检测到的物品边框中心 类型为torch.Tensor shape为(检测到的物体数量,2)
        obj_boxes 	   : 
                        检测到的物品边框 类型为numpy.ndarray shape为(检测到的物体数量,2,2)
        obj_scores	   : 
                        检测到的物品得分 类型为list shape为(检测到的物体数量,)
        """

        predictions = self.predictor(bgr_frame)
        self.instances = predictions["instances"].to(self.cpu_device)
        self.obj_classes = self.instances.pred_classes.numpy()
        self.obj_scores = self.instances.scores.numpy().tolist()
        self.masks = self.instances.pred_masks.numpy()
        boxes = self.instances.pred_boxes.__getitem__(slice(None))
        self.centers = self.instances.pred_boxes.get_centers()
        self.obj_boxes = []

        for box in boxes:
            points=[]
            box = box.numpy()
            points.append([int(box[0]) , int(box[1])])
            points.append([int(box[2]) , int(box[3])])
            self.obj_boxes.append(points)
        
        self.obj_boxes = np.asanyarray(self.obj_boxes)

        return self.obj_classes, self.masks, self.centers, self.obj_boxes, self.obj_scores
