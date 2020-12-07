# DO_NOT_Look_At_My_Screen
如果自己的工位正靠近走廊，可以后台运行该脚本保护屏幕隐私.

People whose work station close to the corridor  can run the script as a background process to protect screen privacy.

------

This demo is mainly based on [JackKoLing](https://github.com/JackKoLing)'s work, check [here](https://github.com/JackKoLing/opencv_deeplearning_practice/tree/master/practice1_face_detection).

## How It Works

The code is based on a light Face detection algorithm, and it works quite **simple**: Counting the number of faces in real time, if number is not 1, the screen brightness will be reduced.

**Test Platform:** Lenovo xiaoxin pro13, **i7 10710U + MX250**, 16G(2666MHz) + 512G SSD

CPU occupancy is in 20--40%, GPU 0%.  

The fan of laptop is still at 18 ℃, which means **it is lightweight and won't occupy too much computing resources.**

## Install

**For Script running:**

1. Install dependicies: 
   * python3.x(tested on python3.8) 
   * opencv-python
   * time
   * wmi
   * numpy
2. run "python main.py" 

**For .exe running:**

​	Double click the .exe file


