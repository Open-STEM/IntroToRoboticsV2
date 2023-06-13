Calling Drive Functions
=======================

Here are functions that are built to make the robot go straight and turn

.. tab-set::

    .. tab-item:: Python
        :sync: key1

        .. code-block:: python

            drivetrain.straight(distance: float, speed: float = 0.5, timeout: float = None) -> bool
            drivetrain.turn(turn_degrees: float, speed: float = 0.5, timeout: float = None) -> bool

    .. tab-item:: Blockly
        :sync: key2

        .. code-block:: cpp

            std::out << "hello world";

These versions of the drive functions have a few extra features we didn't cover in the last section, such as the use of an optional timeout for if you anticipate the robot being unable to reach its target position for any reason.

Calling the Drive Functions:
----------------------------

Similar to most of the code you've written so far in this section, we call these methods from
inside of def main():, located within code.py:

.. code-block:: python

    def main():
        # Drive forwards 20 cm and then turn 90 degrees clockwise
        drivetrain.straight(20, 1)
        drivetrain.turn(90, 0.8)

So now that we have the fundamentals of driving down, what else can we do?

Mini-Challenge: An A-Maze-ing Path
----------------------------------
[Picture of 1001 maze (with dimensions)]

If we wanted our robot to navigate this maze, what would we do? Try breaking down the path into simple "drive straight __ cm" and "turn __ degrees" segments. This will allow us to easily convert real world instructions into code for the robot.

Once you have your path written out informally, try converting that into instructions for the robot using the go_straight and go_turn functions. Place your robot into the maze and run your code. If your robot touches the tape at any point, try to adjust the distances and turns so that it doesn't.

A Shapely Surprise
------------------
Let's take the ideas we just exercised for the maze and do something a little simpler. Let's try to get the robot to drive in the shape of a square. You can choose how big you want the square to be; for this exercise it doesn't really matter. Follow the same steps as before, and write down the segments in pseudocode (words describing what the code will do informally) before translating that into actual code.
 
.. raw:: html
    <iframe width="560" height="315" src="https://youtu.be/ERl_785Iss8" frameborder="0" allowfullscreen></iframe>


XRP tracing a square

You may notice that this code is pretty repetitive, consisting of the same two instructions 4 times. There's got to be a cleaner way of doing that, right?

Python Programming Note: For Loops
----------------------------------

Similar to the While loops we covered earlier, for loops are a special type of loop that are usually used to run a section of code a specified number of times. The syntax for a for loop is as follows:

.. code-block:: python

    for counter_name in range(number_of_loops):
        # Loop content goes here
As a for loop cycles, "counter_name" becomes a variable equal to the number loop that is currently occurring, starting at zero. This means that on the third time running the loop content, counter_name = 2.

Mini-Challenge: An Application
------------------------------

Now that we know about for loops, we can try a new approach to driving. Take your square driving code and adapt it to have the robot outline a triangle instead of a square. Then, rewrite it using a for loop.
