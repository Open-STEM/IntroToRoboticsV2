Using the reflectance sensor
============================

In this lesson we will write simple code to make the XRP follow a line on the
floor. The line we will follow will be made of black tape placed on a white
surface. In this lesson, you'll learn how a *reflectance* sensor works and why
we use these colors for the line.

The XRP robot is not only able to measure distances with its rangefinder, but
can use its two analog reflectance sensors on the front underside of the robot
to measure how reflective the ground surface is. This is particularly useful for
a specific use case - detecting and following lines!

This sensor consists of an infrared transmitter and a receiver. The transmitter
emits infrared light which gets reflected from colored obstacles (for our
curriculum, the colored obstacle is the black line which the robot would
follow). The receiver absorbs and senses how much infrared light is reflected
from the nearby obstacles. Based on the intensity of the absorbed light, logical
decisions could be made by the robot to complete certain tasks, for example,
following a line.

By using a black line and a white background, we ensure that the line stands out
from the background as much as possible, making it easy for the sensor to
distinguish between them.

The XRP has two reflectance sensors, a left and right sensor. **XRPLib**
provides a function to read from each reflectance sensor:

.. code-block:: python

   from XRPLib.defaults import *

   left = reflectance.get_left()
   right = reflectance.get_right()

Both of these functions return a value that ranges from 0 (white) to 1 (black).
However, these sensors are separated only by around a centimeter - why do we
need two sensors instead of one? Later through this module, we will discuss how
integrating the data from both sensors onto our code can yield more accurate
results.

Let's consider a previous exercise - using a while loop to drive a certain
distance:

.. code-block:: python

    from XRPLib.defaults import *

    while drivetrain.get_left_encoder_position() < 20:
        drivetrain.set_speed(5, 5)
    drivetrain.stop()

Here, we command the robot to start going forwards, and keep driving while our 
distance driven by the left encoder is less than 20 cm.

Consider a similar use case for the reflectance sensor: driving forward until a
dark line is detected.

.. image:: stopatline.gif

How could we go about programming this? Well, let's consider what values the
reflectance sensor would read throughout this program:

.. image:: reflectsensoutputgraph.png

This plots the readings of the left reflectance sensor on the y axis over time
on the x axis, where the robot starts on a white surface and then crosses over a
black line.

As shown in the plot, our reflectance sensor gives readings close to 0 while
initially in the light surface, but then jumps close to 1 when it sees the dark
line before going back down. Could we somehow adopt a similar code structure
with a while loop as above to achieve this?

The key lies in the condition of the while loop - what causes the while loop to
terminate. In this case, we want to check whether the sensor's reading has
dipped below a certain value, which would indicate detection of the dark line.
Note that we don't get values that are exactly 0 or 1.

We want to write a condition for our while loop that is :code:`False` once the
sensor crosses a *threshold* value. Based on the graph, **0.7** would be a good
starting point for the threshold. In general, we want to pick something around 
75% of our highest expected value, so that we stay well away from the low values
but still ensure a range of high values will work.

.. admonition:: Try it out

    Try to write code that uses the left reflectance sensor to drive the robot
    forwards at 5 centimeters per second until it sees a line.
