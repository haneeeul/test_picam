#-*- coding: utf-8 -*-
import picamera, sys
camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
camera.start_preview()

def main():
    print("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    camera.stop_preview()

if __name__=="__main__":
    main()
