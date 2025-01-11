from grove.grove_ryb_led_button import GroveLedButton
from gpiozero import PWMOutputDevice
import time

pin = 5
obj = GroveLedButton(pin)

BUZZER_PIN = 12
buzzer = PWMOutputDevice(BUZZER_PIN)

def sound(dur):
    buzzer.frequency = 261
    buzzer.value = 0.5
    time.sleep(dur)
    buzzer.value = 0
    time.sleep(0.1)

led_state = False

def cust_on_event(index, event, tm):
    global led_state
    #single click
    if event == 2:
        led_state = True
        obj.led.light(led_state)
        sound(0.5)

        print("state2 - LED turned ON")
    # long press
    elif event == 8:
        led_state = True
        obj.led.light(led_state)
        sound(1.0)
        print("state8 - LED turned ON")
    elif event == 16:
        led_state = False
        obj.led.light(led_state)
        print("state16 - LED turned OFF")
    else:
        print(f"Unhandled event: {event}, time: {tm}")

obj.on_event = cust_on_event

while True:
    time.sleep(1)
