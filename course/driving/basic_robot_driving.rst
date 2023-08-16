Getting the Robot Moving
========================

Basic driving
-------------

In the last lesson we learned how to set the effort of each of your robot's 
motors individually. Since both of the motors make up the robot's drivetrain,
there's an easier way to write code to move the robot.

.. note:: 

    For this lesson, put your XRP on a flat surface like a table or the floor.

Getting your XRP robot to move is simple! Here is some code you can use to drive both the left and right motors at 50% 
effort:

.. tab-set:: 

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.defaults import *

            drivetrain.set_effort(0.5, 0.5)

    .. tab-item:: Blockly

        .. image:: media/seteffortexample.png
            :width: 300

:code:`0.5` and :code:`0.5` are the parameters of the function.
The functions you used before only had one parameter, but functions can have as
few or as many parameters as you want, or even none at all.

.. hint:: 

    Parameters are inputs to a function that can dictate attributes like distance or angle to vary its behavior.


.. admonition:: Try it out
    
    Add the code to your program to see your robot drive.

    Try using different values to make the robot move at different speeds. What 
    happens if you use different values for the left and right wheels?

    Afterward, place the robot on a ramp and run it again. Take notice of how
    the robot moves slower when on the ramp. Why does this happen?

You may notice that your XRP does not drive perfectly straight even though you 
used the same effort value for both motors. This is because the motors on the 
XRP aren't perfect. Every motor is a little bit different. Some of them have 
more friction inside them than others. In the next module we'll learn some ways 
to solve this problem so your robot goes straight every time.

