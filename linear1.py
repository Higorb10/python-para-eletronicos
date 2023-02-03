import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
servo = GPIO.PWM(12,70)


count = 1
while (count <= 1):
    
    print("Ciclo: ", count)
    servo.start(0)
    time.sleep(1)

    duty = 6
    while duty <= 12:
        servo.ChangeDutyCycle(duty)
        time.sleep(4)
        duty = duty + 6
    
    servo.ChangeDutyCycle(0)
    time.sleep(1)
    servo.ChangeDutyCycle(0)

    count = count + 1
