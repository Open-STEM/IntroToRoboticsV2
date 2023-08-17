Obstacle Avoidance 
==================

One useful application of the ultrasonic sensor is obstacle avoidance. 

In this tutorial, we will learn how to use the ultrasonic sensor to first stop at a certain distance from an object, and then to avoid the object by turning a random angle away from an object. 

Step 1: Going forward a certain distance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first step in obstacle avoidance is being able to stop at a certain distance from an object.
To do this, we want to continously read the rangefinder distance and check whether it is less than,
let's say, 10 cm. Once it crosses this threshold, we want to stop the robot.

To accomplish this, we can use a while loop, with a condition that checks whether the
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
~~~~~~~~~~~~~~~

Instead of simply stopping, we'd like to turn around 180 degrees, go forward, and repeat,
turning 180 whenever we detect an object.

To turn 180 degrees, we'd want to replace :code:`drivetrain.stop()` with :code:`drivetrain.turn(180)`.
After this, we'd want to go forward again. But instead of writing :code:`drivetrain.set_speed(10, 10)` again,
notice that we're just trying to run these two steps over and over:
    1. Go forward until an object is detected
    2. Turn 180 degrees

Looks like we can just wrap these two steps in a while loop! Here's what the code looks like:

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

Now What?
~~~~~~~~~

Even though we're turning around after detecting an object, you should notice that your robot is getting stuck in a cycle. 

To fix this, many robots like IRobot's Roomba use a simple algorithm known as "bump and run".

The idea behind bump and run is that if you bump into an object, you should turn away from it at a random angle and continue on your way.

The reason that we specify that the robot must turn at a random angle is because if we turn at the same angle every time, we will get stuck in a cycle again.

Also, we still want to be able to have some control over the range of angles that our robot turns. 

In this case, let's say that after hitting an object, we want our robot to turn between 135 and 225 degrees. Look at the following diagram to see what this looks like:

.. error:: 

    TODO add a graphic to show the range of angles

To accomplish this, we will use the random library which allows python to randomly generate a decimal number from 0.0 to 1.0.

We can then "scale" this number up by 90 which means that we will then get a random number from 0 to 90.

Run this code block a couple of times to see what happens:

.. error:: 

    TODO add code to show random number generation and scaling between 0-90

If we then add this scaled number to 135, we will get a random number from 135 to 225 (which is the range of angles that we want to turn).

The code for this is as follows:

.. error:: 

    TODO add code to complete this


And voi la! We have now successfully created a program where our robot can avoid objects forever!