import wiringpi
from time import sleep
servo_pin = 32 # Using GPIO pin number
# Initialize WiringPi and SoftServo
wiringpi.wiringPiSetupGpio()
wiringpi.softServoSetup(servo_pin, -1, -1, -1, -1, -1, -1, -1) #I also tried  softPwmCreate

while(True):
    # Move the servo to 0 degrees
    print("Moving to 0 degrees")
    wiringpi.softServoWrite(servo_pin, 0)
    sleep(1)
    # Move the servo to 90 degrees
    print("Moving to 90 degrees")
    wiringpi.softServoWrite(servo_pin, 90)
    sleep(1)
    # Move the servo to 180 degrees
    print("Moving to 180 degrees")
    wiringpi.softServoWrite(servo_pin, 180)
    sleep(1)

    wiringpi.softServoWrite(servo_pin, 0)
    wiringpi.delay(1000) # Give time for the servo to reach 0 degrees
    wiringpi.softServoWrite(servo_pin, -1) # Release the servo