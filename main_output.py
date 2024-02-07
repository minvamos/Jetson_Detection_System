import sys
import cv2 
import imutils
from yoloDet import YoloTRT
from playsound import playsound
import time

# use path for library and engine file
model = YoloTRT(library="yolov5/build/libmyplugins.so", engine="yolov5/build/cmodel.engine", conf=0.5, yolo_ver="v5")

cap = cv2.VideoCapture('videos/6.mp4')
# put video's directory you want to detect.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) 

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (640, 480))

#frame_count = 0

while True:
    ret, frame = cap.read()


    Green = False
    Cross = False
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_thickness = 3
    text = "NONE"
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = int((frame.shape[1] - text_size[0]) / 2)
    text_y = int((frame.shape[0] + text_size[1]) / 2)

    # changed line
    detections, t = model.Inference(frame)
    for obj in detections:
        print(obj['class'], obj['conf'], obj['box'])
        if obj['class'] == 'Green':
            Green = True
        elif obj['class'] == 'Cross':
            Cross = True

    print("FPS: {} sec".format(1/t))
    if Green and Cross:
        text = "Can across"
        #playsound("Nar.mp3")
    else:
        text = "NONE"

    cv2.putText(frame, text, (text_x, text_y), font, font_scale, (0, 255, 0), font_thickness, cv2.LINE_AA)

    # Write the frame to the output video
    out.write(frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release the VideoWriter and VideoCapture objects
out.release()
cap.release()
cv2.destroyAllWindows()
