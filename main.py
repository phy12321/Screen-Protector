'''
使用摄像头实现人脸检测
'''
import cv2
import time
import wmi
import numpy as np

modelPath = "deploy.prototxt.txt"
weightPath = "res10_300x300_ssd_iter_140000.caffemodel"
confidence = 0.5  # 置信度参数，高于此数才认为是人脸，可调
vs = cv2.VideoCapture(0)  # 用笔记本自带摄像头，请选0
c = wmi.WMI(namespace='root\WMI')
a = c.WmiMonitorBrightnessMethods()[0]
screen_low = False

net = cv2.dnn.readNetFromCaffe(modelPath, weightPath)

while True:
    ret, frame = vs.read()
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()  # 预测结果
    pred_confidence = detections[0,0,:,2]
    num_face = np.sum(np.where(pred_confidence > confidence, 1, 0))

    time.sleep(0.1)
    # print(num_face)
    if num_face != 1:
        if not screen_low:
            screen_low = True
            a.WmiSetBrightness(Brightness=10, Timeout=100)
            time.sleep(.1)
        elif screen_low:
            time.sleep(.1)
    elif screen_low:
        screen_low = False
        a.WmiSetBrightness(Brightness=70)

vs.release()
cv2.destroyAllWindows()
