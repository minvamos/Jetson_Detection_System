# YOLO Crosswalk detection with Jetson Nano 2GB
<img src="https://github.com/minvamos/Jetson_Detection_System/assets/122091776/660220dc-464b-416f-8e09-2e3b5e1e3ebf" alt="demo" width="480" height="360">


The repository provides the NVIDIA Jetson Nano with Yolov5 and openCV, recognizing crosswalks and pedestrian traffic lights to determine if they can traverse.

For model learning for object detection, [**Yolov5**](https://github.com/ultralytics/yolov5) was used. In order to use Jetson Nano's GPU, the learned model was converted into a TensorRT engine using [**Tensorrtx**](https://github.com/wang-xinyu/tensorrtx/tree/master/yolov5).

## Requirement
Operating system : JetPack 4.6

Python : version 3.6.9

CUDA : 10.2.300

CuDNN : 8.2.1.32

Memory swap : 5GB

## Libraries

torch : 1.8.0

torchvision : 0.9.0

OpenCV : 4.5.5 with CUDA

pyCUDA : 2020.1

numpy  : 1.19.0

pandas : 1.1.5

Pillow : 8.4.0

scipy : 1.5.4

seaborn : 0.11.2

pyYAML : 6.0.1

tqdm : 4.64.1

psutil : 5.9.8

imutils : 0.5.4


## Training
Part of [**PTL_Dataset_876x657.zip**](https://dl.orangedox.com/p6T3Fs) and the images taken by myself were used for learning.
|   |   |   |
|---|---|---|
| ![1](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/931747b9-b8c6-4de6-8733-57b9cf07efa7) | ![2](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/fa8af2a3-eb1d-4a31-8f77-5c91a7512774) | ![3](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/4d86b1ea-52c1-4a0f-bcf0-64c065b6e44c) |
| ![d1](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/af87920e-92ea-438d-a21a-98ef48e71483) | ![d2](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/d7008e9a-77cb-4bc6-ab07-95c0e011a032) | ![d3](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/33410afa-4bfe-4731-b70d-f1b89c070ae2) |

|           | Training | Validation |  Total |
|-----------|----------|------------|--------|
| Images    | 2642      | 659       | 3201    |


## Inference
To proceed with real-time detection that can be checked by GUI using a USB camera, run ```main.py``` .

```
$ python3 main.py
```
If you want to obtain a detection completed video file using mp4 file, run ```main_output.py```.
```
$ python3 main_output.py
```
you have to change the path of mp4 files. 
