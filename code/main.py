from machine import Pin,PWM #importing required PIN and PWM from modules
import time #importing time module

#Define and map Motors
M1A=PWM(Pin(8))
M1B=PWM(Pin(9))
M2A=PWM(Pin(10))
M2B=PWM(Pin(11))

M1A.freq(100)
M1B.freq(100)
M2A.freq(100)
M2B.freq(100)

#Set Pins for IR Sensors as INPUTS
right_ir = Pin(28, Pin.IN)
left_ir = Pin(26, Pin.IN)
center_ir = Pin(27, Pin.IN)

#PID variables
Kp = 0.4 # Proportional gain #0.26
Ki = 0.0 # Integral gain
Kd = 0.12 # Derivative gain #0.2

last_movement = ''

last_error = 0
integral = 0
stop_flag = False
all_black = False

def calculate_error(right_val, center_val, left_val): # Returns the result to the error variable
     # Stop condition 1: All sensors see line (1,1,1)
    global stop_flag, all_black, last_movement
     
    if right_val == 1 and center_val == 1 and left_val == 1:
        all_black = True # Signal to stop
        return 0
    
    # Stop condition 2: No sensors see line (0,0,0)
    if right_val == 0 and center_val == 0 and left_val == 0:
        if last_movement == 'RIGHT':
            return 1
        elif last_movement == 'HARD_RIGHT':
            return 2
        elif last_movement == 'LEFT':
            return -1
        elif last_movement == 'HARD_LEFT':
            return -2

    # Normal line-following logic
    if center_val == 1:
        if right_val == 1:
            last_movement = 'RIGHT'
            return 0.5 # Right edge detected → turn right
        elif left_val == 1:
            last_movement = 'LEFT'
            return -0.5 # Left edge detected → turn left
        else: return 0  # Perfectly centered
    else:
        if right_val == 1:
            last_movement = 'HARD_RIGHT'
            return 2 # Far right → hard right
        elif left_val == 1:
            last_movement = 'HARD_LEFT'
            return -2  # Far left → hard left
        else: return 0  # Shouldn't happen (handled above)
        
def pid_control(error):
    global last_error, integral
    
    # PID term calculation
    proportional = error
    integral += error
    derivative = error - last_error
    
    # Error update
    last_error = error
    
    output = Kp * proportional + Ki * integral + Kd * derivative
    
    output = max(-1.0, min(1.0, output))
    
    return output

def set_motors(output):
    base_speed = 50000 # Starting motor speed
    max_offset = 35000 # Maximum difference for steering
    
    # Calculate motor speed
    left_speed = base_speed + int(output * max_offset)
    right_speed = base_speed - int(output * max_offset)
    
    left_speed = max(0, min(50000, left_speed)) # Ensuring speeds are within PWM limits
    right_speed = max(0, min(50000, right_speed)) # Ensuring speeds are within PWM limits       
    if output > 0: # Need to turn right
        M1A.duty_u16(0)
        M1B.duty_u16(left_speed)
        M2B.duty_u16(0)
        M2A.duty_u16(right_speed)
    elif output < 0:  # Need to turn left
        M1A.duty_u16(left_speed)
        M1B.duty_u16(0)
        M2B.duty_u16(right_speed)
        M2A.duty_u16(0)
    else:  # Go straight
        M1A.duty_u16(0)
        M1B.duty_u16(base_speed)
        M2B.duty_u16(base_speed)
        M2A.duty_u16(0)

#Stop
def stop():
    M1A.duty_u16(0)
    M1B.duty_u16(0)
    M2B.duty_u16(0)
    M2A.duty_u16(0)

while not all_black:
    right_val=right_ir.value() #Read Sensor 1 Value
    left_val=left_ir.value() #Read Sensor 2 Value
    center_val=center_ir.value() #Read Sensor 3 Value
    
    error = calculate_error(right_val, center_val, left_val)
    
    if all_black == True:
        stop()
        time.sleep(0.1)
        continue
    else:
        output = pid_control(error)
        set_motors(output)
