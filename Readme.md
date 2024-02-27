# YOLO Crosswalk detection with Jetson Nano 2GB
<img src="https://github.com/minvamos/Jetson_Detection_System/assets/122091776/660220dc-464b-416f-8e09-2e3b5e1e3ebf" alt="demo" width="480" height="360">


The repository provides the NVIDIA Jetson Nano with Yolov5 and openCV, recognizing crosswalks and pedestrian traffic lights to determine if they can traverse.

It is expected that visually impaired people will wear this equipment and help when using crosswalks.

For model learning for object detection, [**Yolov5**](https://github.com/ultralytics/yolov5) was used. In order to use Jetson Nano's GPU, the learned model was converted into a TensorRT engine using [**Tensorrtx**](https://github.com/wang-xinyu/tensorrtx/tree/master/yolov5).

The repository provides two inferences. One detects a crosswalk with a Real time camera and outputs a voice message saying it is possible to traverse when it is in a traversable state. For the rest, enter an mp4 file, and save the result as mp4.
## NVIDIA Jetson AI Specialist
![Jetson_AI_Specialist_Certification](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/fbc52ba3-5dba-4848-bcef-ee36bd3fdd29)

Through this project, I received Jetson AI Specialist certification from NVIDIA.

## Requirement

### Hardware

[**Jetson Nano 2GB developer kit**](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit)

[**ELP 8mp USB Camera**](https://a.co/d/hiW5Qi0)

-------------
The equipment below is required only for main.py playing sound.

[**USB sound card**](https://eleshop.jp/shop/g/gMAR121/?srsltid=AfmBOooG1S5eVXwVad2FVfjOR3HIlRD5SNnTIJkZ13JA1yQ3rukahjr83eg)

[**Stereo single earphone**](https://amzn.asia/d/9Vk3nyw)

### Software

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
Part of [**PTL_Dataset_876x657.zip**](https://dl.orangedox.com/p6T3Fs) and the images taken by myself were used for training.

Training is based on YOLOv5n in the GoogleColab environment using YOLOv5 ver6.0.
|   |   |   |
|---|---|---|
| ![1](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/931747b9-b8c6-4de6-8733-57b9cf07efa7) | ![2](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/fa8af2a3-eb1d-4a31-8f77-5c91a7512774) | ![3](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/4d86b1ea-52c1-4a0f-bcf0-64c065b6e44c) |
| ![d1](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/af87920e-92ea-438d-a21a-98ef48e71483) | ![d2](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/d7008e9a-77cb-4bc6-ab07-95c0e011a032) | ![d3](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/33410afa-4bfe-4731-b70d-f1b89c070ae2) |

|           | Training | Validation |  Total |
|-----------|----------|------------|--------|
| Images    | 2642      | 659       | 3201    |

## Object Classification
In this model, four classes of object recognition are possible.

### 0 (Green): Green pedestrian traffic light
### 1 (Cross): Crosswalks in a crossable state

### 2 (D_Cross): Crosswalk in a non-crossable state (Vehicles are driving on a crosswalk)

### 3 (Red): Red pedestrian traffic light
## Inference
You can check the output videos in [**Video Link**](https://youtu.be/FFOofk3XE1s?si=jHIGIHz5xtgDS1eW) here.

Clone this project from the GitHub repository and go to the repository.
```
$ git clone https://github.com/minvamos/Jetson_Detection_System.git
```
```
$ cd Jetson_Detection_System
```
To proceed with real-time detection that can be checked by GUI using a USB camera, run 
```main.py``` .

In this code, when a traversable state is detected, a voice (Japanese) is also output.

```
$ python3 main.py
```
If you want to obtain a detection completed video file using mp4 file, run ```main_output.py```.
```
$ python3 main_output.py
```
Change path of mp4 files if you have to. 

## How this application works
Here's how this application works.
![al1](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/2af27b02-4bf8-469e-b583-6575859be7fb)
![al2](https://github.com/minvamos/Jetson_Detection_System/assets/122091776/fb82778c-ddee-472a-aa86-2588b51a076e)

It operates in an infinite loop by default, and reads the frame of the image every cycle. In the frame, class 0 (Green light), class 1 (Safety crosswalk) is detected, indicating the traversable state.