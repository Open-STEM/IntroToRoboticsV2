Calling Drive Functions
=======================

Driving straight and turning in place are two things you'll be doing a lot with 
your XRP. Since these are such common tasks, **XRPLib** has built in functions
to do them for you accurately. These functions use more complicated calculations
than you did in your :code:`drive_distance` function to ensure that the XRP 
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

So now that we have the fundamentals of driving down, what else can we do?

Mini-Challenge: An A-Maze-ing Path
----------------------------------

.. error:: 

    TODO add picture of 1001 maze (with dimensions)

If we wanted our robot to navigate this maze, what would we do? Try breaking
down the path into simple "drive straight __ cm" and "turn __ degrees" segments.
This will allow us to easily convert real world instructions into code for the
robot.

Once you have your path written out informally, try converting that into
instructions for the robot using the :code:`straight` and :code:`turn`
functions. Place your robot into the maze and run your code. If your robot
touches the tape at any point, try to adjust the distances and turns so that it
doesn't.

A Shapely Surprise
------------------

Let's take the ideas we just exercised for the maze and do something a little
simpler. Let's try to get the robot to drive in the shape of a square. You can
choose how big you want the square to be; for this exercise it doesn't really
matter. Follow the same steps as before, and write down the segments in
pseudocode (words describing what the code will do informally) before
translating that into actual code.
 
.. youtube:: ERl_785Iss8

You may notice that this code is pretty repetitive, consisting of the same two
instructions 4 times. There's got to be a cleaner way of doing that, right?

Python Programming Note: For Loops
----------------------------------

Similar to the While loops we covered earlier, for loops are a special type of
loop that are usually used to run a section of code a specified number of times.
The syntax for a for loop is as follows:

.. code-block:: python

    for counter_name in range(number_of_loops):
        # Loop content goes here

As a for loop cycles, :code:`counter_name` becomes a variable equal to the
number loop that is currently occurring, starting at zero. This means that on
the third time running the loop content, :code:`counter_name` = 2.

Mini-Challenge: An Application
------------------------------

Now that we know about for loops, we can try a new approach to driving. Take
your square driving code and adapt it to have the robot outline a triangle
instead of a square. Then, rewrite it using a for loop.
