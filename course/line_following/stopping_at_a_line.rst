Stopping at a Line
==================

In the last module, you wrote and tested a function which could accurately 
determine if the reflectance sensor was able to see a line. In this activity, 
you'll use that function to make the robot stop when it sees a line.

.. figure:: media/stop_at_line.gif
    :align: center

    The XRP stopping when it sees a line.

Let's consider a previous exercise - using a while loop to drive a
certain distance:

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.defaults import *

            while drivetrain.get_left_encoder_position() < 20:
                drivetrain.set_speed(10, 10)
            drivetrain.stop()

        In this code, the condition being checked is
        ``drivetrain.get_left_encoder_position() < 20`` meaning that the robot will
        drive forward at 10 cm/s until the left encoder reads a distance of 20 cm. This 
        code can be easily modified to replace the current condition with a condition 
        that uses the function you wrote.
    
    .. tab-item:: Blockly

        .. image:: media/stop_at_distance.png
            :width: 300

        .. |ico1| image:: media/left_encoder_condition.png
            :height: 3ex

        In this code, the condition being checked is |ico1| meaning that the robot will
        drive forward at 10 cm/s until the left encoder reads a distance of 20 cm. This 
        code can be easily modified to replace the current condition with a condition 
        that uses the function you wrote.

.. admonition:: Try it out

    Modify the example code to use your function (``is_over_line()``) as the 
    condition for the loop.

    If you need to "invert" the value of your function (convert ``False`` to
    ``True`` and ``True`` to ``False``), you can use the ``not`` *operator*
    before calling your function like this: ``not is_over_line()``. This code
    does exactly what it sounds like: returns ``True`` when the robot is ``not``
    over the line.

Once you've tested your code and proved it to meet the challenge, make a new 
function called ``drive_until_line()`` and put your code in it. Don't delete 
this function, as you'll need it later!

Challenge activity - Counting Lines
-----------------------------------

For an added challenge, try to write code which makes the robot capable of 
driving over and stopping at several lines. The robot should drive over a line,
stop for some amount of time, say two seconds, and then start driving again 
until it sees another line. Then, modify your code to stop after having seen 5 lines.

.. tip:: 

    You'll need to write some logic which handles the robot driving *off* of the
    line too! Your code from the main activity might not be enough to handle
    this! Think about what your code would do if it started out *already on* a
    line.

Challenge Activity - Staying in the Circle
------------------------------------------

Your robot is now capable of stopping when it sees a line. You can use this 
functionality to keep your robot trapped inside a circle! This is meant to be a
challenge activity, so you'll need to figure out how to do it on your own. 
Start by breaking down the problem into smaller steps

.. tab-set::

    .. tab-item:: Hide

        Press the other tab to see a hint.

    .. tab-item:: Hint

        #. Drive forward until a line is seen (the edge of the circle)
        #. Stop driving so that the robot doesn't leave the circle
        #. Turn around
        #. Repeat

You already have code which does steps 1 and 2 (``drive_until_line()``), and you
learned back in the robot driving module how to do step 3
(``drivetrain.turn()``, see :doc:`Calling Drive Functions </course/driving/calling_drive_functions>` for a
refresher)

.. admonition:: Tip

    Try out different angles when turning around. 
    You may want to try not turning a full 180 degrees.

.. admonition:: Extension

    If you want to give yourself an extra challenge, turn this into a sumo competition!
    Put two robots in the center of the same circle facing opposide directions, 
    and modify your code to try to push the other robot out of the circle while staying in yourself.
    You can use the distance sensor to detect the other robot. 
    There's many way to optimize a sumo robot program, so try to be creative!