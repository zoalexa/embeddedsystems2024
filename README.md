# Line Follower Robot Project  
*Embedded Systems Class - Computer Science (DUTh)*

---

## Materials Needed

To recreate this project, you will need:

1. **1x Cytron Technologies Maker Pi RP2040**  
2. **2x DC Motors** (ours are 120RPM, but you can use motors with higher RPM)  
3. **3x TCRT5000 IR Sensors** or any equivalent  
4. **2x 18650 Batteries**  
5. **1x 2-slot 18650 Battery Holder**  
6. **1x Step-Down Voltage Regulator** (buck converter)  
7. **2x Rubber Wheels**  
8. **2x Ball Caster Wheels**  
9. **Time and Patience!**

---

## Assembly Instructions
### Step 0: Solder the components
To start, find some wires and solder the following:
  -  The step-down voltage regulator inputs with the battery pack.
  -  The step-down voltage regulator outputs with excess wires, so we can power the board.
  -  Both pins of the motors.
Soldering ensures that the connections are secure and there is not going to be any unexpected disconnection of the cables.

### Step 1: Prepare the Chassis  
Find a **20cm x 10cm** piece of plastic or hard cardboard for your chassis (a shorter length, e.g. 15cm, will also work).

---

### Step 2: Attach the Motors  
Glue the motors on the sides of the long edge of the chassis to ensure the best traction.

![Step 2 - Motors](photos/attach_motors.png)

---

### Step 3: Mount the IR Sensors  
Build a small base to hold the IR sensors side-by-side, preferably with at least a **1cm gap** between each sensor to cover more ground (the example is not 1cm). Example mount is shown in Step 4.

---

### Step 4: Attach IR Sensors Under Chassis  
Attach the IR sensor base under the chassis, preferably close to the center.

![Step 4 - Sensors Under Chassis](photos/attach_sensors.png)

---

### Step 5: Add Ball Caster Wheels  
Attach 2 ball caster wheels, one on each side. You might need standoffs for the sensors to have enough clearance from the ground.

![Step 5 - Ball Casters](photos/attach_ball_caster.png)

---

### Step 6: Place Battery Pack, Board, and Regulator  
Arrange the 18650 battery pack, Maker Pi RP2040 board, and step-down voltage regulator on top of the chassis as you see fit.

![Step 6 - Electronics Placement](photos/top_view.jpg)

---

### Step 7: Connect IR Sensors to Board  
Use the Grove cables provided with the Maker Pi RP2040 (or separate cables if preferred) to connect the IR sensors to the board digital pins.

![Step 7a - IR Sensor Wiring](photos/connect_sensors_1.png)

![Step 7b - IR Sensor Wiring](photos/connect_sensors_2.png)

---

### Step 8: Connect Motors to Motor Driver  
Connect each motor to its corresponding motor driver clamp.  
- Check that **M1B** and **M2B** LEDs light up when you turn the motors counter-clockwise  
- **M1A** and **M2A** LEDs light up when turning clockwise  
- If LEDs are reversed, swap M1A and M1B (same for M2), so you don't have to change your code..

![Step 8a - Motor Connection](photos/connect_motors_1.png)

![Step 8b - Motor Connection](photos/connect_motors_2.png)
---

### Step 9: Install MicroPython and Upload Code  
- Connect your board to the PC via USB while holding the **BOOTSEL** button  
- Flip the power switch to ON  
- Open **Thonny IDE** and install MicroPython on your board  
- Copy the provided code (`main.py`) from the repository
- Save it on the board as `main.py`

![Step 9 - BOOTSEL and Switch](photos/bootsel_and_switch.png)
---

### Step 10: Power and Test Your Robot  
- Flip the power switch to OFF  
- Disconnect USB and connect the batteries to the battery holder  
- Place your robot on the track and switch power ON to start the program

**Congratulations! You’ve created a **line follower robot**!**

This project was created by:
  - Nick Chaitas
  - Zois Alexandridis
  - Pavlos Amanatidis
  - Alkiviadis Ballas

---

### Step 10 (Optional): Modify the Code
- The algorithm that this code uses is the PID algorithm.  
- In order to modify the code, reconnect the board using your USB cable to your computer. **REMOVE THE BATTERIES FIRST!**
- Open Thonny and load `main.py`
- Here, you can tweak the variables Kp, Ki, Kd, base_speed, max_offset and the motor frequency to your liking. You can probably create something better by modifying the code!
- Save and disconnect the robot from your computer.
- Place the batteries in the battery holder.
- Place the robot on the track and flip the switch to the ON setting.
- Test as much as you wish!
