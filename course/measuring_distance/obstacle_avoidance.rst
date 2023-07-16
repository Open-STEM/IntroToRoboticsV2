Obstacle Avoidance 
==================

One useful application of the ultrasonic sensor is obstacle avoidance. 

In this tutorial, we will learn how to use the ultrasonic sensor to first stop at a certain distance from an object, and then to avoid the object by turning a random angle away from an object. 

The First Step
~~~~~~~~~~~~~~

The first step to avoiding objects is to ensure that we can properly sense and stop in front of them. 

Essentially, we want to be able to stop at a certain distance from an object.

To accomplish this, we will employ a while loop with a conditional statement. 

A conditional statement (often known as an "if" statement) is one that outputs either a "true" or "false". 

In this case, we want the robot to go straight until we get too close to an object. Then, we want the robot to stop.

The code for this is as follows:

.. error:: 

    TODO add code that stops at a certain distance from an object


Now What?
~~~~~~~~~

Now that we can stop at a certain distance from an object, we want to be able to avoid the object and continue on our way.

To do this, many robots like IRobot's Roomba use a simple algorithm known as "bump and run".

The idea behind bump and run is that if you bump into an object, you should turn away from it and continue on your way.

One thing to specify here is that when turning, it is important to turn a random angle. This is because if you turn the same angle every time, you will eventually get stuck in a loop where you keep bumping into the same object.

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