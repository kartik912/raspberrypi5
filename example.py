from grove.grove_mini_pir_motion_sensor import GroveMiniPIRMotionSensor
import time

def main():
    sensor = GroveMiniPIRMotionSensor(5)
    
    while True:
        if sensor.on_detect:
            print("Motion detected!")
        else:
            print("No motion.")
        time.sleep(1)

if __name__ == '__main__':
    main()