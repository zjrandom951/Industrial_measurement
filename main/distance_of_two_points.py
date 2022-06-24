import sys
from PyQt5.QtGui import QImage, QPixmap  
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


from distance import Ui_Distance

import cv2
import socket
from connect import ping
import calculate
import pyrealsense2 as rs
from measure import Measure
from main_bcnet import BCNet
from realsense_camera import RealsenseCamera
from draw import draw

class MyMainForm(QMainWindow, Ui_Distance):
    def __init__(self, parent=None):
        super(MyMainForm,self).__init__(parent)

        #初始化界面
        self.setupUi(self) #完整界面

        #初始化按键
        
        self.get_frame.clicked.connect(self.Capture)
        self.start_measure.clicked.connect(self.Start)
        
        #初始化相机
        self.rs = RealsenseCamera()

        


    def Start(self):
        point1 = list(map(int, self.point1.text().split()))
        point2 = list(map(int, self.point2.text().split()))
        points_3d = self.calculator.get_coordinate_Group_3d([point1, point2])
        distance = calculate.cal_dis(points_3d[0], points_3d[1])
        print(points_3d)
        print(distance)

            

    def Capture(self):

        ret, self.bgr_frame, self.depth_frame, _, _, self.depth_intrinsics  = RealsenseCamera.get_frame_stream(self.rs)
        self.depth_scale =self.rs.depth_scale


        image_height, image_width, image_depth = self.bgr_frame.shape  # 获取图像的高，宽以及深度。
        #print("type is", type(self.bgr_frame))
        QIm = cv2.cvtColor(self.bgr_frame, cv2.COLOR_BGR2RGB)  # opencv读图片是BGR，qt显示要RGB，所以需要转换一下
        QIm = QImage(QIm.data, image_width, image_height,  # 创建QImage格式的图像，并读入图像信息
                        image_width * image_depth,
                        QImage.Format_RGB888)
        self.color_frame.setPixmap(QPixmap.fromImage(QIm))  # 将QImage显示在之前创建的QLabel控件中
        self.rs.release()
        self.Camera_on = False

        self.calculator = calculate.calculator(self.depth_frame, self.depth_intrinsics, self.depth_scale)
        self.Show_result()
        

    def Show_result(self):
        Draw = draw(self.bgr_frame)
        cv2.imshow('bgr_frame',Draw.bgr_frame)
        

if __name__ =="__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
