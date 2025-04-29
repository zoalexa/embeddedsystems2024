from machine import Pin,PWM
import time
import utime

# Motor definitions
M1A=PWM(Pin(8))
M1B=PWM(Pin(9))
M2A=PWM(Pin(10))
M2B=PWM(Pin(11))

# Frequency initialization
M1A.freq(100)
M1B.freq(100)
M2A.freq(100)
M2B.freq(100)

#Set Pins for IR Sensors as INPUTS
right_ir = Pin(28, Pin.IN)
left_ir = Pin(26, Pin.IN)
center_ir = Pin(27, Pin.IN)

speed = 20000

# Move Forward
def move_forward():
    M1A.duty_u16(0)
    M1B.duty_u16(speed)
    M2B.duty_u16(speed)
    M2A.duty_u16(0)
    
# Move Backward
def move_backward():
    M1A.duty_u16(speed)
    M1B.duty_u16(0)
    M2B.duty_u16(0)
    M2A.duty_u16(speed)
    
# Turn Right
def turn_right():
    M1A.duty_u16(0)
    M1B.duty_u16(speed)
    M2B.duty_u16(0)
    M2A.duty_u16(speed)
    
# Turn Left
def turn_left():
    M1A.duty_u16(speed)
    M1B.duty_u16(0)
    M2B.duty_u16(speed)
    M2A.duty_u16(0)
   
# Stop
def stop():
    M1A.duty_u16(0)
    M1B.duty_u16(0)
    M2B.duty_u16(0)
    M2A.duty_u16(0)
    
while True:
    
    right_val=right_ir.value() # Read Sensor 1 Value
    left_val=left_ir.value() # Read Sensor 2 Value
    center_val=center_ir.value() # Read Sensor 3 Value
    
    # Debug statement
    # print(str(right_val)+"-"+str(left_val)+"-"+str(center_val))
    
    # Set Conditions for Obstacle Avoidance
    if right_val==0 and left_val==0 and center_val==1:
        move_forward()
    elif right_val==1 and left_val==0:
        turn_right()
    elif right_val==0 and left_val==1:
        turn_left()
    elif right_val==0 and left_val==0 and center_val==0:
        stop()
    elif right_val==1 and left_val==1 and center_val==1:
        stop()
    
    time.sleep(0.025)
