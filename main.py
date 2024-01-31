import sys
import cv2 
import imutils
from yoloDet import YoloTRT
from playsound import playsound
import time
# use path for library and engine file
model = YoloTRT(library="yolov5/build/libmyplugins.so", engine="yolov5/build/cmodel.engine", conf=0.5, yolo_ver="v5")

cap = cv2.VideoCapture('videos/2.mp4')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) 
frame_count = 0
while True:
    ret, frame = cap.read()
    frame_count += 1

    if not ret:
        break

    # Process every other frame
    if frame_count % 3 != 0:
        continue
    Green = False
    Cross = False
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_thickness = 3
    text = "NONE"
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = int((frame.shape[1] - text_size[0]) / 2)
    text_y = int((frame.shape[0] + text_size[1]) / 2)
    #frame = imutils.resize(frame, width=600)

    #changed line
    
    detections, t = model.Inference(frame)
    for obj in detections:
        print(obj['class'], obj['conf'], obj['box'])
        if obj['class'] == 'Green' :
            Green = True
        elif obj['class'] == 'Cross' :
            Cross = True

    print("FPS: {} sec".format(1/t))
    if Green and Cross :
        text = "Can across"
        playsound("Nar.mp3")
    else :
        text = "NONE"


    cv2.putText(frame, text, (text_x, text_y), font, font_scale, (0, 255, 0), font_thickness, cv2.LINE_AA)
    cv2.imshow("Output", frame)


    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
