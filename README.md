# Jetbot 

## Overview
This project is Jetbot which drives autonomously. It does that based on collision avoidance and traffic sign recognition model. 
But there are few things to keep in mind the model which were not used are variants of Yolo which couldn't get compatible with Jetpack 4.4. But the model performance was far better than SSD mobilnet. Those models are also included on "not_used_model" directory.


## Structure
- [Collision-Avoidance](#Collision-Avoidance)
- [SSD-Mobilenet-Training](#SSD-Mobile-Training)
- [Road-Sign](#RoadSign)


## Collsion-Avoidance
This is done to make Jetbot stay inside the track. It aims is to classidy between "Free Area"and "Blocked Area". Further documenation is provided in collision_avoidance. 

## SSD-Mobile-Training
 SSD-MobileNet, a light-weight CNN model that is designed for edge devices. This model is much faster than YOLOv8, making around 5 inferences per second. Regarding the training, it is available in ssd_model_training.

## Roadsign
The frame is sent to the TSR model, the model will attempt to identify one of three traffic signs. The type of sign determines the Pulse Width Module (PWM) signal strength to both of the motors. When a stop sign is detected, both motors are set to 0% throttle for half a second. Left-turn signs set the right motor to low throttle, and the left motor to high throttle. Right-turn signs do the opposite; the right motor is set to high throttle, and the left motor to low throttle. The turns complete in one second.
