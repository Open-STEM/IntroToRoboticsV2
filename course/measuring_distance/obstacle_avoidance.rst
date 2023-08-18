Obstacle Avoidance 
==================

One useful application of the ultrasonic sensor is obstacle avoidance. 

In this tutorial, we will learn how to use the ultrasonic sensor to first stop at a certain distance from an object, and then to avoid the object by turning a random angle away from an object. 

Step 1: Going forward a certain distance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first step in obstacle avoidance is stopping at a certain distance from an object.
To do this, we want to continuously read the rangefinder distance and check whether it is less than,
let's say, 10 cm. Once it crosses this threshold, we want to stop the robot.

To accomplish this, we can use a while loop with a condition that checks whether the
rangefinder distance is less than 10 cm.

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            drivetrain.set_speed(10, 10)
            while rangefinder.distance() > 10:
                time.sleep(0.1)
            drivetrain.stop()


    .. tab-item:: Blockly

        .. image:: media/forwarduntildistance.png
            :width: 300

Step 2: Turing 180 degrees once an object is detected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of simply stopping, we'd like to turn around 180 degrees, go forward, and repeat,
turning 180 whenever we detect an object.

To turn 180 degrees, we'd want to replace :code:`drivetrain.stop()` with :code:`drivetrain.turn(180)`.
After this, we'd want to go forward again. But instead of writing :code:`drivetrain.set_speed(10, 10)` again,
notice that we're just trying to run these two steps over and over:
    1. Go forward until an object is detected
    2. Turn 180 degrees

It looks like we can wrap these two steps in a while loop! Here's what the code looks like:

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            # Repeat these two steps over and over again
            while True:

                # Go forward until an object is detected
                drivetrain.set_speed(10, 10)
                while rangefinder.distance() > 10:
                    time.sleep(0.1)

                # Turn 180 degrees
                drivetrain.turn(180)


    .. tab-item:: Blockly

        .. image:: media/forwardturnrepeat.png
            :width: 300

Step 3: Turing a random angle once an object is detected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Even though we're turning around after detecting an object, you should notice that your robot is getting stuck in a cycle.
Because the robot is turning 180 degrees, it often turns back into the object it just detected. To fix this, many
robots like iRobot's Roomba use a simple algorithm known as "bump and run." If you bump into an object, instead of turning 180
degrees, the robot should turn away from it at a random angle to increase the chance it'll explore a new area.

However, if the robot were to turn to a completely random angle, there would be a chance the robot barely turns at all if the random
number is small. So, we'd want to give the robot a reasonable random range of angles to pick from.

.. tab-set::

    .. tab-item:: Python

        We can use :code:`random.randint(135, 225)` to generate a random number between 135 and 225, which we can turn that many degrees.
        Though, note that we need to :code:`import random` at the top of our program to import the library that contains this function.

        .. code-block:: python

            # the library that contains random.randint
            import random

            # Repeat these two steps over and over again
            while True:

                # Go forward until an object is detected
                drivetrain.set_speed(10, 10)
                while rangefinder.distance() > 10:
                    time.sleep(0.1)

                # Turn random amount between 135 and 225 degrees
                turnDegrees = random.randint(135, 225)
                drivetrain.turn(turnDegrees)


    .. tab-item:: Blockly

        Blockly provides a handy block for generating a random number between lower and upper bounds, inclusive.

        .. image:: media/forwardturnrepeatrandom.png
            :width: 400


And voi la! We have successfully created a program where our robot can avoid objects forever!
