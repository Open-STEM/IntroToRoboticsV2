Effort vs. Speed
================


Getting the Robot to move
-------------------------

Getting your XRP robot to move is pretty easy. On a basic level, all movement
commands boil down to this one method:

.. code-block::
    
    drivetrain.set_effort(left_effort: float, right_effort: float);

A *method* is a grouping of code for a common purpose. For example, the
drivetrain.set_effort function sets the drivetrain to move at the effort
values you as the programmer specify. These input values into the method
are called *parameters*, and are essential for giving methods context that
may change at various points.

So what is an effort value?
---------------------------

An effort value is a measure of how much voltage is sent to the motors.
Sending more voltage to the motors results in it running at a higher
speed or it producing more torque or both. 

In our case, effort values are bound between -1.0 (full power in reverse)
and +1.0 (full power forwards), with 0 being off.  Any thoughts on
what 1/2 effort would be?

Let's test this so we can get a better idea of what effort values
actually mean:
In code.py, inside of def main():, add the following line of code
to run the motors at full power. This is where you will be putting most
of your code moving forward.

Python Programing Notes:
------------------------

Note1:
    The while loop will continue to loop through the statements that
    are indented underneath it until the while condition is no longer true.
    The while True: will continue to execute forever, also known as an infinite
    loop.

Note2:
    time.sleep(0.1) tells the program to do nothing for 0.1 seconds. 

Note3:
    It is good practice to put the robot up on something like a roll
    of tape where the wheels can run free without hitting the table. This
    keeps the robot from running off the end of the table. When a program in
    an infinite loop like this is started, it will keep spinning the wheels
    until the program is changed. To stop the wheels from turning, you will need
    to delete or comment out the drivetrain.set_effort(1.0, 1.0) line and save
    the program again.

.. code:: Python

    def main():
        while True:
            drivetrain.set_effort(1.0, 1.0)
            time.sleep(0.1)

Notice that the effort values used above are 1.0 which represents half effort
forward. What would you use for half effort forward and what would use for
half effort backward?

Then, upload your code to the robot and let the robot drive on a flat
surface. Take note of how fast it goes. Try measuring how fast it travels
in a few seconds!

Afterward, place the robot on a ramp and run it again. Take notice of how
the robot moves slower when on the ramp. Why does this happen?

.. video:: RampAscend.mp4

Ramp ascend

.. video:: RampDescend.mp4

Ramp descend

Mini-Challenge: Climbing Slopes
-------------------------------
So if a robot drives slower up a ramp, then the natural question would
be: how steep of a slope can the robot climb?

Have your robot drive on a ramp and then raise the ramp until the robot
is no longer able to move forwards. Is that angle what you expected? If your
robot started sliding back down the ramp, think about why that happened.
