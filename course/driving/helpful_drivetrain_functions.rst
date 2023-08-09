Helpful Drivetrain Functions
============================

Throughout this module, we've explored different ways to drive forwards
and turn, through setting efforts, speeds, and reading the encoders. However,
XRPLib also provides some handy functions to make it easy for the user.
These functions use more complicated calculations to ensure that the XRP 
drives smoothly and exactly to the right distance every time.

.. code-block:: python

    drivetrain.straight(distance, max_effort = 0.5, timeout = None)

This function will drive the robot straight forward for a distance in
centimeters that you specify. The other two parameters are *optional*. You can 
provide a value for them, but if you don't, the default value will be used.

Calling the function like this: :code:`drivetrain.straight(20)` will make the
robot go straight 20 centimeters, and use the default values for everything
else, meaning a maximum effort applied of 50% and no timeout.

You can also use a negative value for distance to drive backwards.

The :code:`max_effort` parameter specifies how much effort the robot is allowed
to apply while driving. By default it is 50%, which is a good effort for normal
driving on a flat surface.

The :code:`timeout` parameter specifies a time, in seconds, that the robot
should try to drive before giving up. For example, what if your robot runs into
something while driving, and the wheels get stuck? The robot will use the
encoders to measure the wheels and notice that it never arrived at the distance
you set, so it will try forever and none of your code will run afterwards. The
timeout lets you set a maximum time that the XRP should try for before giving
up. Usually, you won't need to use this, but it is there if you need it.

.. code-block:: python

    drivetrain.turn(turn_degrees, max_effort = 0.5, timeout = None)

This function is similar to the :code:`straight` function, except that it
rotates the robot instead of driving it forwards.

The :code:`turn_degrees` parameter lets you tell the robot how many degrees it
should turn. Positive values will turn clockwise, and negative values turn
counterclockwise.

.. admonition:: Try it out

    Write code to drive the robot straight for 20 centimeters and then turn 90
    degrees clockwise. Don't forget to add the 
    :code:`from XRPLib.defaults import *` statement at the top of your program.