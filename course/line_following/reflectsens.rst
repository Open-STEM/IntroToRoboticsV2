Using the Reflectance sensor
============================
Detecting the line
------------------

The XRP robot is not only able to measure distances with its rangefinder, but can use its two analog reflectance sensors on the front underside of the robot to measure how reflective the ground surface is. This is particularly useful for a specific use case - detecting and following lines!

Navigation:
-----------


The goal of navigation is to find the best route from the starting point to the destination within an environment. Navigation is especially helpful for avoiding obstacles and staying on the path.

The reflectance sensor:
-----------------------


This sensor consists of an infrared transmitter and a receiver. The transmitter emits infrared light which gets reflected from colored obstacles (for our curriculum, the colored obstacle is the black line which the robot would follow). The receiver absorbs and senses how much infrared light is reflected from the nearby obstacles. Based on the intensity of the absorbed light, logical decisions could be made by the robot to complete certain tasks, for example, following a line. 

The API provides two library functions to read information from the reflectance sensors:

.. code-block:: python

   left = reflectance.get_left()
   right = reflectance.get_right()

Both of these functions return a value that ranges from 0 (white) to 1 (black). However, these sensors are separated only by around a centimeter - why do we need two sensors instead of one? Later through this module, we will discuss how integrating the data from both sensors onto our code can yield more accurate results.

 
Let's consider a previous exercise - using the rangefinder to drive until some certain distance to the wall. The code looks something like this: ::
   
   drivetrain.set_effort(1,1)
   while sonar.get_distance() > 10:
   time.sleep(0.1)
   drivetrain.stop()

Here, we command the robot to start going forwards, keep polling our rangefinder at quick regular intervals, and when we dip under the 10 cm distance, we break out the robot and stop the drive motors.

 
Consider a similar use case for the reflectance sensor: driving forward until a dark line is detected.


Insert Video Here


How could we go about programming this? Well, let's consider what values the reflectance sensor would read throughout this program:

.. image:: reflectsensoutputgraph.png

This plots the readings of the left reflectance sensor on the y axis over time on the x axis, where the robot starts on a white surface and then crosses over a black line.

As shown in the plot, our reflectance sensor gives readings close to 0 while initially in the light surface, but then jumps close to 1 when it sees the dark line before going back down. Could we somehow adopt a similar code structure with a while loop as above to achieve this?

The key lies in the condition of the while loop - what causes the while loop to terminate. In this case, we want to check whether the sensor's reading has dipped below a certain value, which would indicate detection of the dark line. Note that we don't get values that are exactly 0 or 1 - surfaces never fully reflect or absorb heat - so we can't have a while loop condition like: while reflectance ``reflectance.get_left() != 1:``

A condition like this means that we would continue going forward until we detected a surface that was perfectly black, which is quite unlikely to happen. Instead, by considering any value over 0.7, for example, as "black", this gives us considerable margin of error for different variations of darkish surfaces. So, the code should consist of starting the motors, waiting until the reflectance sensor's value jumps above a value (i.e. 0.7), and then stop the motors.

Mini Challenge: Line Detection
------------------------------

* Write a program to go forward until a black line is detected. It should look like the video above.
