import sys
from robot import Robot
import jetson.inference
from jetson.utils import videoSource
import jetson.utils
import numpy as np
import cv2
import time


robot = Robot()
#robot = Robot(left_multiplier=0.95)
input = videoSource("0")

timeStamp = time.time()

fpsFilt=0

dispW=640
dispH=640
flip=1  # Right side up wai


net = jetson.inference.detectNet(argv=['--model=ssd-mobilenet.onnx','--labels=labels.txt','--input-blob=input_0','--output-cvg=scores', '--output-bbox=boxes'])


max_speed = 1


output = jetson.utils.videoOutput("rtp://10.197.49.128:1234")



while True:
    
    img = input.Capture()
       
    cv_frame = jetson.utils.cudaToNumpy(img)
    flip_img = cv2.flip(cv_frame, -1)
    cuda_img = jetson.utils.cudaFromNumpy(flip_img)
    
    if img is None:
        print("No image input")
    
    detections = net.Detect(cuda_img)
    if len(detections) > 0:
        print("detected {:d} objects in image".format(len(detections)))
        class_id = detections[0].ClassID
        
        if class_id == 0:
            print("BACKGROUND")
            print("GO STRAIGHT")
            robot.set_motors(0.30 * max_speed, 0.30 * max_speed)
            time.sleep(0.5)
        
        elif class_id == 1:
            print("LEFT")
            robot.set_motors(0.10 * max_speed, 0.30 * max_speed)
            #robot.left(.30)
            time.sleep(1)
            robot.stop()

        elif class_id == 2:
            print("RIGHT")
            robot.set_motors(0.30 * max_speed, 0.10 * max_speed)
            #robot.right(.30)
            time.sleep(1)
            robot.stop()
                    
        elif class_id == 3:
            print("STOP")
            robot.stop()
            time.sleep(.5)
            robot.set_motors(0.25 * max_speed, 0.25 * max_speed)
            time.sleep(1)
    else:
        robot.set_motors(0.25 * max_speed, 0.25 * max_speed)
        time.sleep(1)
        
    output.Render(cuda_img)
    output.SetStatus("Network {:.0f} FPS".format(net.GetNetworkFPS()))    

                        
        
        
