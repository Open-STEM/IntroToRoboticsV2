Picking up a Basket
===================

Now that we've covered how to move the XRP arm to specific angles, we can start to think about how to use the arm 
to pick up objects. In this section, we'll cover how to use the arm to pick up a basket which is one of the challenges for your final project described in detail in the next module.

The Process 
-----------

Let's first think about what the process of picking up a basket would look like. Imagine the a small paper
cup with a bail attached over the top to that you can hook with the servo arm. An example of a basket is
shown in the video below.

An example of the steps required to aquire the basket are:


#. Lower the arm to a height where it will be inside the bail.
#. Back up the robot so that the arm goes inside the bail.
#. Raise the arm to lift the bucket off the ground.
#. Drive away carying the bucket.

Now the robot can drive away while carrying the basket. 

Try placing your robot in front of a basket and then writing a program to pick it up as shown in the
following video.


.. image:: 
    RobotGrab.gif
    

Integrating Locating and Pickup 
-------------------------------

Now that we've covered how to pick up a basket, we can start to think about how to integrate this with code that we have previously written to locate a nearby object. 

To do this, you will re-use the code that you have written to how execute the pickup process when the robot is in front of the basket.