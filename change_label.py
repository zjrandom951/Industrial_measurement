import cv2
import os
import glob
import json
import collections
import numpy as np
from labelme import utils

def RotateClockWise90(img):
    new_img = np.rot90(img)
    return new_img

if __name__ == "__main__":
    src_dir = '/home/zjrandom/Dataset/dataset-final'
    dst_dir = '/home/zjrandom/Projects/BCNet/datasets/coco_yi'
    
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    # 先收集一下文件夹中图片的格式列表，例如 ['.jpg', '.JPG']
    exts = dict()
    filesnames = os.listdir(src_dir)

    #i = 771 #开始的编号

    i = 977 #开始的编号
    
    for filename in filesnames:
        name, ext = filename.split('.')
        if ext != 'json':
            if exts.__contains__(ext):
                exts[ext] += 1
            else:
                exts[ext] = 1

    anno = collections.OrderedDict()  # 这个可以保证保存的字典顺序和读取出来的是一样的，直接使用dict()的话顺序会很乱（小细节哦）
    for key in exts.keys():
        for img_file in glob.glob(os.path.join(src_dir, '*.' + key)):
            length = len(str(i))

            new_filename = "0" * (4-length) + str(i) + ".jpg"

            file_name = os.path.basename(img_file)
            print(f"Processing {file_name}")
            img = cv2.imread(img_file)

            (h, w, c) = img.shape   # 统计了一下，所有图片的宽度里面，1344是占比较多的宽度中最小的那个，因此
                                    # 都等比例地将宽resize为1344(这里可以自己修改)

            w_new = 640
            h_new = 480
            

            if h > w :

                w_ratio = w_new / h  # 标注文件里的坐标乘以这个比例便可以得到新的坐标值
                h_ratio = h_new / w

                img_rorate = RotateClockWise90(img)
                print(img_rorate.shape)
                img_resize = cv2.resize(img_rorate, (w_new, h_new))  # resize中的目标尺寸参数为(width, height)
            else :
                w_ratio = w_new / w  # 标注文件里的坐标乘以这个比例便可以得到新的坐标值
                h_ratio = h_new / h

                img_resize = cv2.resize(img, (w_new, h_new))  # resize中的目标尺寸参数为(width, height)

            cv2.imwrite(os.path.join(dst_dir, new_filename), img_resize)

            # 接下来处理标注文件json中的标注点的resize
            json_file = os.path.join(src_dir, file_name.split('.')[0] + '.json')

            #save_to = open(os.path.join(dst_dir, file_name.split('.')[0] + '.json'), 'w')
            save_to = open(os.path.join(dst_dir, new_filename.split('.')[0] + '.json'), 'w')
            with open(json_file, 'rb') as f:
                anno = json.load(f)

                anno["imagePath"] = new_filename #修改文件名
                anno["imageHeight"] = 480 #修改图片尺寸
                anno["imageWidth"] = 640


                for shape in anno["shapes"]:
                    points = shape["points"]
                    #points = np.rot90(points)
                    new_points = []
                    if h > w:
                        for point in points:
                            new_point_w = point[1] * w_ratio
                            new_point_h = point[0] * h_ratio
                            new_points.append([new_point_w, 480 - new_point_h])
                    else :
                        for point in points:
                            new_point_w = point[0] * w_ratio
                            new_point_h = point[1] * h_ratio
                            new_points.append([new_point_w, new_point_h])

                    shape["points"] = new_points
                    
                # 注意下面的img_resize编码加密之前要记得将通道顺序由BGR变回RGB
                anno['imageData']=str(utils.img_arr_to_b64(img_resize[..., (2, 1, 0)]), encoding='utf-8')
                json.dump(anno, save_to, indent=4)
                i += 1 #编号递增

    print("Done")
