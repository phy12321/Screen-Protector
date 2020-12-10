# Screen-Protector
如果自己的工位正靠近走廊，可以后台运行该脚本保护屏幕隐私.

People whose work station close to the corridor  can run the script as a background process to protect screen privacy.

------

This demo is mainly based on [JackKoLing](https://github.com/JackKoLing)'s work, check [here](https://github.com/JackKoLing/opencv_deeplearning_practice/tree/master/practice1_face_detection).

## How It Works

The code is based on a light Face detection algorithm, and it works quite **simple**: Counting the number of faces in real time, if number is not 1, the screen brightness will be reduced.

**Test Platform:** **win10**(Lenovo xiaoxin pro13,,  i7 10710U + MX250, 16G(2666MHz) + 512G SSD)

CPU occupancy is in 20--40%, GPU 0%.  

The fan of laptop is still at 18 ℃, which means **it is lightweight and won't occupy too much computing resources.**

## Install

**The exe package , which shuold not be a big problem, is not relaeased for now . So it requries a conda envrionment to execute in.**

1. create a virtual envrionment and  install following dependicies: 
   * python3.x(tested on python3.8) 
   * opencv-python
   * time
   * wmi
   * pywin32
   * numpy
2. Download the code.
3. run "python ./main.py" 



