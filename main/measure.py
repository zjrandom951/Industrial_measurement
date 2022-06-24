import process
import calculate
class Measure():
    def __init__(self,classes, depth_frame,depth_intrn,depth_scale, masks, boxes, centers) -> None:
        #some tools initialization
        self.Processor = process.processor(classes, masks, boxes, centers)
        self.Calculator = calculate.calculator(depth_frame, depth_intrn, depth_scale)
        self.Goal_Shim = []
        self.Goal_Bolt = []

    ###############################Measure Shim####################################################
    def measure_shim(self):
        """
        测量垫片尺寸

        Parameters:
        -----------
        masks_Shim 	   : 
                        垫片掩膜 类型为numpy.ndarray 取值为 True或False shape为 (垫片数量, 480, 640)
        centers_Shim 	   : 
                        垫片中心 

        Return:
        -----------
        Goal_Shim 	   : 
                        垫片的尺寸 类型为list
        """

        if len(self.Processor.masks_Shim) != 0:
            self.Goal_Shim = self.Calculator.cal_Shim_Goal(self.Processor)
            # ##Distinguish between outer and inner edges of shim
            # contours_Shim_outside = self.Processor.contours_Shim[0] 
            # contours_Shim_inside = self.Processor.contours_Shim[1]
            
            # ##Get 3d coordinate 
            # self.coordinate_3d_contours_Shim_inside = self.Calculator.get_coor_Groups_3d(contours_Shim_inside)
            # self.coordinate_3d_contours_Shim_outside = self.Calculator.get_coor_Groups_3d(contours_Shim_outside)

            # ##Calculate 3d centers of shim(Point center)
            # self.coordinate_3d_centers_Shim_inside = calculate.cal_coor_Groups_mean(self.coordinate_3d_contours_Shim_inside)
            # self.coordinate_3d_centers_Shim_outside = calculate.cal_coor_Groups_mean(self.coordinate_3d_contours_Shim_outside)           

            # ##Calculate 3d distance between centers and contours of shim
            # distance_Shim_outside = calculate.cal_dis_p2ps_Groups(self.coordinate_3d_centers_Shim_outside,self.coordinate_3d_contours_Shim_outside)
            # distance_Shim_inside = calculate.cal_dis_p2ps_Groups(self.coordinate_3d_centers_Shim_inside,self.coordinate_3d_contours_Shim_inside)
            
            # #Calculate Goal
            # self.Goal_Shim = self.Calculator.cal_Shim_Goal(distance_Shim_outside,distance_Shim_inside)
            
        return self.Goal_Shim


#################################Measure Bolt#######################################################

    def measure_bolt(self):
        """
        测量螺栓尺寸

        Parameters:
        -----------
        masks_Bolt 	   : 
                        螺栓掩膜 类型为numpy.ndarray 取值为 True或False shape为 (螺栓数量, 480, 640)

        Return:
        -----------
        Goal_Bolt 	   : 
                        螺栓的尺寸 类型为list
        """       
        if len(self.Processor.masks_Bolt) != 0:
            self.Goal_Bolt = self.Calculator.cal_Bolt_Goal(self.Processor)
        return self.Goal_Bolt