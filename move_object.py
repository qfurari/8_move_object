#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-
import math

# <rtc-template block="description">
"""
 @file move_object.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
move_object_spec = ["implementation_id", "move_object", 
         "type_name",         "move_object", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "VenderName", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.speed", "0.01",
         "conf.default.scope", "100",

         "conf.__widget__.speed", "text",
         "conf.__widget__.scope", "slider",

         "conf.__type__.speed", "double",
         "conf.__type__.scope", "double",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class move_object
# @brief ModuleDescription
# 
# 
# </rtc-template>
class move_object(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_inCoordinate = OpenRTM_aist.instantiateDataType(RTC.TimedShortSeq)
        """
        """
        self._inCoordinateIn = OpenRTM_aist.InPort("inCoordinate", self._d_inCoordinate)
        self._d_inPosition = OpenRTM_aist.instantiateDataType(RTC.TimedShortSeq)
        """
        """
        self._inPositionIn = OpenRTM_aist.InPort("inPosition", self._d_inPosition)
        self._d_outCoordinate = OpenRTM_aist.instantiateDataType(RTC.TimedShortSeq)
        """
        """
        self._outCoordinateOut = OpenRTM_aist.OutPort("outCoordinate", self._d_outCoordinate)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        
         - Name:  speed
         - DefaultValue: 0.01
        """
        self._speed = [10]
        """
        
         - Name:  scope
         - DefaultValue: 100
        """
        self._scope = [100]
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
        self.bindParameter("speed", self._speed, "0.01")
        self.bindParameter("scope", self._scope, "100")
		
        # Set InPort buffers
        self.addInPort("inCoordinate",self._inCoordinateIn)
        self.addInPort("inPosition",self._inPositionIn)
		
        # Set OutPort buffers
        self.addOutPort("outCoordinate",self._outCoordinateOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
        return RTC.RTC_OK
	
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
	
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
    
        return RTC.RTC_OK
	
    ##
    #
    # The deactivated action (Active state exit action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):
    
        return RTC.RTC_OK
	
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
        # inPositionポートからデータを読み込む
       
            
        if self._inPositionIn.isNew()  :# and self._inCoordinateIn.isNew()
            if self._inCoordinateIn.isNew():
                #追加座標の読み込み
                #print("座標読み込み開始")
                coordinateIn_data_list = []
                while self._inCoordinateIn.isNew():
                    coordinateIn_data = self._inCoordinateIn.read().data
                    coordinateIn_data_list.append(coordinateIn_data)
                #print("現在の座標配列の長さ："+ str(len(coordinateIn_data_list)))

                #追加座標の読み込み
                #print("人の座標読み込み開始")
                positionIn_data_list = []
                while self._inPositionIn.isNew():
                    positionIn_data = self._inPositionIn.read().data
                    positionIn_data_list.append(positionIn_data)
                #print("現在人の座標配列の長さ："+ str(len(positionIn_data_list)))

            
                #処理
                scope = 50#修正いるかも リストで帰ってくるなら
                speed = 10
                num_circles =len(coordinateIn_data_list)
                num_people = len(positionIn_data_list)
                print("オブジェクトの数",num_circles)
                print("人の数",num_people) 
                
                for j in range(num_people):
                    #print("####TEST1####")
                    for i in range(num_circles):
                       # print("####TEST2####")
                # 目標位置と円の距離を計算
                        target_x = positionIn_data_list[j][0]
                        target_y = positionIn_data_list[j][1]
                        circle_x = coordinateIn_data_list[i][0]
                        circle_y = coordinateIn_data_list[i][1]
                        distance = int(math.sqrt((target_x - circle_x) ** 2 + (target_y - circle_y) ** 2))
                       # print("####TEST3####")

                # 目標位置に向かって移動
                        if distance == 0:
                            coordinateIn_data_list[i] = [int(circle_x + 1), int(circle_y + 1)]

                        elif distance < scope : 
                           # print("check") # あまりに小さい距離のときは動かさない
                            direction_x = (circle_x - target_x) / distance
                           # print("check")
                            direction_y = (circle_y - target_y) / distance
                           # print("check")
                            coordinateIn_data_list[i] = [int(circle_x + direction_x * speed), int(circle_y + direction_y * speed)]
                           # print("check")
                        else:
                            direction_x = (target_x - circle_x) / distance
                           # print("check")
                            direction_y = (target_y - circle_y) / distance
                           # print("check")
                            coordinateIn_data_list[i] = [int(circle_x + direction_x * speed), int(circle_y + direction_y * speed)]





                #dataの挿入
                #print("####TEST4####")
                print("移動済みの座標",coordinateIn_data_list)
                print("人の座標",positionIn_data_list)
                for data in coordinateIn_data_list:
                    OutCoordinate = RTC.TimedShortSeq(RTC.Time(0,0),data)
                    self._outCoordinateOut.write(OutCoordinate)

                del coordinateIn_data_list
                del positionIn_data_list
                del OutCoordinate
                del direction_x
                del direction_y
                del circle_x
                del circle_y
                del distance
                del coordinateIn_data
                del target_x
                del target_y
                del scope
                del speed
        
                
        return RTC.RTC_OK
	
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
	



def move_objectInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=move_object_spec)
    manager.registerFactory(profile,
                            move_object,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    move_objectInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("move_object" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

