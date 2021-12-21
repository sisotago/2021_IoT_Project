# picamera_test.py
import picamera
import time

path = '/home/pi/06_multimedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3)   # 카메라 준비시간
    #camera.capture('%s/photo.jpg' % path)
    camera.start_recording('%s/video.h264' % path)
    input(('press enter to stop')
    #time.sleep(10)
    camera.stop_recording()
finally:
    camera.stop_preview()