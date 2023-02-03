import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
servo = GPIO.PWM(12,50)


count = 1
while (count <= 5):
    
    print("Ciclo: ", count)
    servo.start(0)
    time.sleep(0.5)

    duty = 5
    while duty <= 20:
        servo.ChangeDutyCycle(duty)
        time.sleep(0.5)
        duty = duty + 5
    
    servo.ChangeDutyCycle(0)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

    count = count + 1