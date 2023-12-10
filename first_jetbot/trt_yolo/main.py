import cv2
import time
import ctypes
import sys
from detection import Detector

# dispW=480
# dispH=480
dispW = 640
dispH = 640
flip=0 # Right side up 
pipeline = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=640, height=640, format=NV12, framerate=30/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink  '

def detect(video_path, engine_file_path):
    detector = Detector(engine_file_path)
    capture = cv2.VideoCapture(pipeline)
    fps = 0.0
    while True:
        ret, img = capture.read()
        if img is None:
            print('No image input!')
            break

        output_image_frame,bboxes = detector.detect(img)

        # cv2.imshow('frame', img)
        cv2.imshow('frame', output_image_frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
                break
    capture.release()
    cv2.destroyAllWindows()
    detector.destroy()

if __name__ == "__main__":
    # load custom plugin and engine
#    PLUGIN_LIBRARY = "./libmyplugins_yolov8.so"
#    engine_file_path = "./yolov8.engine"
    PLUGIN_LIBRARY = "./libmyplugins_yolov7tiny.so"
    engine_file_path = "./yolov7-tiny.engine"
    video_path = 0
    if len(sys.argv) > 1:
        engine_file_path = sys.argv[1]
    if len(sys.argv) > 2:
        PLUGIN_LIBRARY = sys.argv[2]

    ctypes.CDLL(PLUGIN_LIBRARY)
    detect(video_path, engine_file_path)
