import argparse
import cv2
import torch
from detectron2.config import get_cfg
#from detectron2.engine.defaults import DefaultPredictor
from detectron2.engine.defaults import DefaultPredictor
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



args = get_parser().parse_args()
cfg = setup_cfg(args)

predictor = DefaultPredictor(cfg)
model = predictor.model

original_image = cv2.imread('test_img/0051.jpg')
height, width = original_image.shape[:2]

image = predictor.transform_gen.get_transform(original_image).apply_image(original_image)
image = torch.as_tensor(image.astype("float32").transpose(2, 0, 1))

inputs = {"image": image, "height": height, "width": width}
fake_iter = 10 
x = ([inputs], fake_iter, fake_iter*10)
batch_size = 2  #批处理大小

export_onnx_file = "bcnet.onnx"			# 目的ONNX文件名
torch.onnx.export(model,
                    x,
                    export_onnx_file,
                    input_names=["input"],
                    output_names=["output"])

