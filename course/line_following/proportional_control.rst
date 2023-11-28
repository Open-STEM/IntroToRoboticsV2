Following the Line: Proportional Control
========================================

In the measuring distances module, you used proportional control to make the
robot drive straight along a wall. We can apply proportional control to the line
following problem too!


The perks of proportional control
---------------------------------

Let's think back to the previous exercise - following the line by either
turning slightly left or right depending on whether the robot is situated to the left or
the right of the line. 
The issue with that approach is that the robot oscillates (bounces back and forth) around the line, 
and if the robot strays too far from the line, it loses track of where the line is. 
Since there were only two cases, where the robot turns at a set speed left or right, 
being just slightly from the line result in the robot turning too much, 
and the robot may not be able to recover. 
Instead of only having two cases, it seems like we'd want a whole bunch of
cases, for anywhere from a sharp left turn to going perfectly straight to a
sharp right turn, and everything in between, based on whether the reflectance
sensor is completely on white, grey, black, or somewhere in between.

.. figure:: media/p_control_1.png
    :align: center

    Desired steering actions based on what the sensor sees.

Having a long chain of if-else statements doesn't sound fun. Perhaps we can look
at this with a completely fresh approach?

From the previous module, we looked at proportional control to smoothly control
the robot's distance to the wall using the distance sensor. Can we use the same
concept here?

Calculating error
-----------------

When we were using proportional control to control the robot's distance to the wall,
we calculated the error as the difference between the desired distance and the
actual distance. We can do the same here: the error is the difference between
some threshold value (representing being on the edge of the line) and the actual reflectance value.
In the initial reflectance sensor exercise, you found an approximate threshold value 
for the reflectance sensor to determine whether the robot was on or off the line. 
We're going to start by using that threshold value to calculate the error.

So, the error is the following:

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            # Input your threshold value here:
            threshold = 0.5 
            error = reflectance.get_right() - threshold

    .. tab-item:: Blockly

        .. image:: media/set_error.png
            :width: 300

Above, we subtract the threshold to center the reflectance value, so that the error is
negative when the robot is too far left and needs to turn right, and positive
when the robot is too far right and needs to turn left. 

If you want to test to make sure the error is being calculated correctly, you
can print the error to the console in a loop.

Implementing proportional control
---------------------------------

Based on the computed error, we want that to determine how much the robot turns. 

.. figure:: media/p_control_2.png
    :align: center

    Desired steering actions and proportional control output based on what the
    sensor sees.

This image illustrates how the error impacts how much we want to turn. Remember:
making the robot turn is simply setting the left and right motors to different
efforts. Similarly to how we did wall following, we'll need to apply a base speed
and use the error to adjust it as needed.

.. tab-set::

    .. tab-item:: Hide

        Now it's your turn. Try and implement proportional control for line following using the error.
        If you need a hint or want to view the solution, take a look at the next tabs.

    .. tab-item:: Hint

        .. tab-set::

            .. tab-item:: Python

                .. code-block:: python

                    drivetrain.set_effort(base_effort - KP * error, base_effort + KP * error)

            .. tab-item:: Blockly
                
                .. image:: media/set_effort_error.png
                    :width: 300

        This would be run inside the loop. The base_effort represents the average effort
        of the motors, no matter how much the robot turns. KP scales how much the robot
        should turn based on the error - a higher KP means the robot will react more
        to smaller deviations in error.

        Let's do a quick check to make sure the code makes sense. We assume base_effort
        = 0.5 and KP = 1. If the reflectance reads whitish-grey and yields a value of
        around 0.25, the error would be -0.25, meaning that the left motor's effort is:

        .. math:: 

            0.5 - 1 \cdot -0.25 \\
            \begin{align}
            & = 0.5 + 0.25 \\
            & = 0.75
            \end{align}

        and the right motor's speed is: 

        .. math:: 

            0.5 + 1 \cdot -0.25 \\
            \begin{align}
            & = 0.5 - 0.25 \\
            & = 0.25
            \end{align}

        Motor efforts of 0.75 and 0.25 would indicate a turn to the right, and the code
        does as desired.

    .. tab-item:: Solution

        .. tab-set::

            .. tab-item:: Python

                .. code-block:: python

                    # Input your threshold value here:
                    threshold = 0.5 
                    base_effort = 0.5
                    KP = 1
                    while True:
                        error = reflectance.get_right() - threshold
                        drivetrain.set_effort(base_effort + KP * error, base_effort - KP * error)
                        time.sleep(0.01)

            .. tab-item:: Blockly

                .. image:: media/one_edge_line_follow.png
                    :width: 1000

        Just to review, let's take this code line-by-line and make sure we understand what's going on.

        :code:`threshold = 0.5` sets the threshold value to 0.5. 
        This is the value that the reflectance sensor will use to determine whether the robot is on or off the line.
        This is a tuned value that may differ depending on your line, sensor, and lighting.

        :code:`base_effort = 0.5` sets the base effort to 0.5.
        This is the average effort of the motors, which controls how fast we want the robot to follow the line. 
        A higher base effort means the robot will follow the line faster, but also means the robot will be less able to recover from errors.

        :code:`KP = 1` sets the KP value to 1.
        This is the proportional constant, which controls how much the robot reacts to the error.
        This is our main tuning value, and you'll have to try different values to see what works best for your robot.

        :code:`error = reflectance.get_right() - threshold` calculates the error.
        As we discussed earlier, the error basically is our measurement of how far the robot is from the line.

        :code:`drivetrain.set_effort(base_effort + KP * error, base_effort - KP * error)` sets the motor efforts.
        This is where we actually use the error to determine how much the robot turns. 
        A positive error means we are too far left, and need the left power to be higher than the right power,
        and a negative error means we are too far right, and need the right power to be higher than the left power.

This is a video illustrating line following with one-sensor control. Notice the
smoother tracking compared to on/off control, yet the robot is still unable to
recover perfectly, because even a small amount of strafing from the
line results in the robot completely losing where it is. 
We'll look at how to improve this in the next section. 
Also, the KP value was not equal to 1 here; it's up to you to figure out the best 
KP value for your bot.

.. error::

    Missing one-sensor line following video

