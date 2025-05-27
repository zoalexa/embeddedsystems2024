This was a project handout about the class of "Embedded Systems" in Computer Science (DUTh).

To recreate this project, you will need:
  1) Cytron Technologies Maker Pi RP2040
  2) 2 DC Motors (ours are 120RPM, you can use more RPM if you want)
  3) 3 TCRT5000 IR Sensors or any equivalent
  4) 2 18650 Batteries
  5) 1x 2-slot 18650 Battery Holder
  6) A step-down voltage regulator (also known as a buck converter)
  7) 2 Rubber Wheels
  8) 2 Ball Caster Wheels
  9) Time!

How to create for yourself:

-  Find a 20cm x 10cm piece of plastic or hard cardboard to use as your chassis (shorter length will work as well)
-  We recommend using glue to attach the motors to the side of the long side, to ensure the best traction.
-  Build a small base for the IR sensors and attach them to the center, side by side, with a gap of at least 1cm, to ensure you cover as much ground as possible.
-  Attach the base of the IR sensors under the chassis, preferably close to the center.
-  Attach 2 ball caster wheels, one on each side (you might need some standoffs to ensure clearance from the ground).
-  On the top side of the chassis, place the 18650 battery pack, the board and the step-down voltage regulator as you see fit.
-  Connect your IR sensors with the board by using the grove cables provided by the Maker Pi RP2040, as shown in the picture, using the digital pins of the sensors (or use separate pin cables if you want to do some cable management).
-  Connect the motors on the motor driver clamps (each motor has its own clamp).
-  Make sure the M1B and M2B LEDs are lighting up when you physically turn the motor counter-clockwise and M1A and M2A LEDs are lighting up when you physically turn the motor clockwise.
-  Alternatively, you can change the pins in the code to the opposite of what they are now (M1A's pin goes to M1B etc.). You will however have to change the way the motor output is handled in the code, if you choose to do it this way.
-  
-  Connect the board with a USB cable on your computer while holding down the BOOTSEL button, flip the switch on the ON setting and open Thonny to install MicroPython on your board.
-  After installing MicroPython on your board, copy the code provided in the code section of the repository.
-  Save the code in the board and rename the file to main.py
-  Flip the switch to the OFF setting, disconnect the board from the computer and plug the batteries on the battery holder.
-  Place your robot on your track and flip the ON switch to initiate the program.

Congratulations, you have created a line follower robot!
