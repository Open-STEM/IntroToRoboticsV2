Following the Line: Proportional Control with Both Sensors
==========================================================

Line following with proportional control using one sensor is quite an
improvement to on/off control. Yet, it's not perfect - if the reflectance sensor
crosses over the center of the line, it's game over.

.. figure:: media/p_control_2_sensors_actions.png
    :align: center

    Desired steering actions based on what the sensor sees.

The issue is - the robot has no way of knowing which side of the line it is
following at all! If it sees the right edge of the line, it will assume it still
is detecting the left edge, and thus keep turning right past the point of no
return!

It would be neat if we could actually follow the center of the line, and can
recognize both cases in which the robot drifts to the left or the right of the
center of the line, and makes a correction. This would largely increase the
"controllable" range of what the reflectance sensor sees and can correctly react
to. Conveniently, it seems like we haven't yet made use of the second
reflectance sensor on the right...

If we recorded the reflectance of both sensors as we moved the robot around the
line, there are a few major "categories" of behaviors the robot would perform.
For a minute, assume the rectangle is a black line and the two red squares are
the location of the reflectance sensors.

.. figure:: media/p_control_2_sensors_left.png
    :align: center

    Simplified view of both reflectance sensors completely off of the line.

Sensors read ~0 and ~0. Robot does not know if it is on either the left or right
side of the line.

.. figure:: media/p_control_2_sensors_half.png
    :align: center

    Simplified view of both reflectance sensors half on the line.

Sensors read ~0 and ~1. Robot knows it is on the left side and turns right.

.. figure:: media/p_control_2_sensors_centered.png
    :align: center

    Simplified view of both reflectance sensors centered on the line.

Sensors read ~0.5 and ~0.5. Robot knows it is on the center and goes straight.

The other two major categories you can extrapolate for yourself.

So, how can we effectively combine the readings of the left and right
reflectance sensors using proportional control to have the robot follow the
line? There's quite an elegant solution that I encourage for you to try to
figure out yourselves before the answer is revealed.

Implementation
--------------
.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            error = reflectance.get_left() - reflectance.get_right()

    .. tab-item:: Blockly

        .. image:: media/error.png
            :width: 300

At the beginning this line of code may not make a lot of sense - but let's
dissect it. Remember our previous convention of positive error meaning the robot
is too far left and needs to turn right, and vice versa.

In this case, if the robot is following the left edge of the line, then the left
sensor detects close to white while the right sensor detects close to black, and
so:

.. math:: 

    \begin{align}
    \text{error} & = 0 - 1 \\
    & = -1
    \end{align}


Which causes the robot to turn right. On the other hand, if the
robot is following the right edge of the line:

.. math:: 

    \begin{align}
    \text{error} & = 1 - 0 \\
    & = 1
    \end{align}

Which causes the robot to turn left. When the robot is right at the center, both
sensor values are the same and so the error is 0, and as the robot starts
drifting towards either direction, the magnitude of the error increases and thus
the robot compensates accordingly.

The most interesting case is when the robot is completely off the line - in this
case, both sensors read white, leaving an error of 0, and so the robot just goes
straight. Given that the robot wouldn't know which direction to compensate if it
was completely off the line, this seems like a reasonable result.

And so, our final code is as follows:

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.defaults import *

            # Try different values for KP and base_effort to get things working smoothly
            KP = 1
            base_effort = 0.5

            while True:
                error = reflectance.get_left() - reflectance.get_right()
                drivetrain.set_effort(base_effort - KP * error, base_effort + KP * error)
    
    .. tab-item:: Blockly
        
        .. image:: media/set_effort_program.png
            :width: 550

Here's what that looks like. Note that KP used in this video was not equal to 1:

.. error:: 
    
    TODO add video


.. admonition:: Try it out

    * Combine what you've learned with encoders to create a function that 
      follows the line using two sensors for some given distance, and, then stop
      the motors.
    * What KP value is best? 
    * Compare one sensor to two sensor line following. What bends in the black
      line is two sensor line following able to handle that one sensor line
      following cannot?
