import cv2

vc = cv2.VideoCapture('/Users/zhangyan/Desktop/fog.mp4')

c = 1

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

timeF = 375  # 视频帧计数间隔频率

while rval:
    rval, frame = vc.read()
    if (c%timeF == 0):
        cv2.imwrite('/Users/zhangyan/Desktop/dataset/' + str(c) + '.bmp', frame)
    c = c+1
    cv2.waitKey(1)
vc.release()