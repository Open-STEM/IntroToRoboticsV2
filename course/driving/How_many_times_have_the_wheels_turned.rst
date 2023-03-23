How many times have the wheels turned?
======================================

We know that, in order to find out how far we have driven, we can use :math:`numberOfRotations \cdot circumference = distanceTravelled`.

We can find the circumference of the wheel (remember, it is :math:`diameterOfWheel \cdot pi`), but how do we find the number of rotations? 

 

How many times have the wheels turned?
--------------------------------------
 

The robot has sensors that look at how far the wheels have turned. If you don't remember, the sensors on a robot give it information about it's environment and actions --similar to your five senses -- that we can ask about, and use to make decisions. Because the robot senses this information, we can just ask it "how much have the wheels turned?"

 

The Encoders
************

The Encoders are the sensors on the motors.

The Encoders tell you how many times the wheel has turned 1.25 degrees. If you ask "how many times has the wheel turned 1.25 degrees", and the encoder says "100 times", that means you have turned :math:`1.25 \cdot 100 = 125` degrees.

 

What would the encoder say if you had turned one rotation? Remember, there are 360 degrees in one revolution.

There are :math:`\frac{360}{1.25} = 288` divisions in one rotation.

.. image:: media/blog017-image001-disks-resolution.jpg

These are examples of encoders, where the wheel is divided into multiple sections. Each one represents one "click". There are 288 sections in the motor you are using.

 

In the video below, the encoder has 60 clicks in a rotation.

https://youtu.be/u-aMnayYO6c

How many times did it rotate? how did you find this out? can you find how many degrees it has rotated each time it clicks from this?

Asking the robot about rotations
To get the encoder ticks on the left motor, you can use 

.. code-block:: python

    leftEncoderPosition = drivetrain.get_left_encoder_position()

You can print the left encoder position to your computer using 

.. code-block:: python 

    print(leftEncoderPosition)

Challenge 1: Design Thinking
----------------------------

Use the tools you learned about here and the internet to print the distance your robot has driven.

    How would you find the distance?

    What information do you need to find that out?   

    What information do you not have? Where might you be able to find that?

You can test this by moving the robot by hand along a measuring tape.


Challenge 2: Abstraction
------------------------

Create a function that takes in an encoder value and returns the distance travelled by the wheel.

Call it getDistanceFromTicks( numberOfEncoderTicks ) because it gets the distance travelled from the number of encoder ticks. 

once you have created the function, you can use it to find the distance a wheel has driven 

.. code-block:: python

    leftEncoderPosition = drivetrain.get_left_encoder_position()
    rightEncoderPosition = drivetrain.get_right_encoder_position()

    left_Wheel_Total_Distance_Travelled = getDistanceFromTicks(leftEncoderPosition)
    right_Wheel_Total_Distance_Travelled = getDistanceFromTicks(rightEncoderPosition) 
