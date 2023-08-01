Staying in the Circle
=====================

Your robot is now capable of stopping when it sees a line. You can use this 
functionality to keep your robot trapped inside a circle! You'll find out why 
you'd want to do this in the next module, which is a challenge activity!

Let's break this problem down into a series of steps:

#. Drive forward until a line is seen (the edge of the circle)
#. Stop driving so that the robot doesn't leave the circle
#. Turn around
#. Repeat

You already have code which does steps 1 and 2 (``drive_until_line()``), and you
learned back in the robot driving module how to do step 3
(``drivetrain.turn()``, see :doc:`/course/driving/calling_drive_functions` for a
refresher)

.. admonition:: Try it out

    Write an infinite loop which keeps the robot in a circle. Try out different 
    angles when turning around. You may want to try not turning a full 180 
    degrees.