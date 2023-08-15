Introduction to Wall Following
==============================
Now that you've developed a program to keep a certain distance from an object, let's implement this by having the XRP follow a wall while maintaining a target distance.

Building a control law
----------------------
What do we want to do when we are too close to the wall? How do we start to move closer to the wall?

Here is a sketch of the setup:

.. image:: media/wallFollow.png
 
.. tip::
   Remember that you will want to incorporate a "base effort" to ensure that the robot is moving forward at all times. Let's set this to **0.5**.

   It is also important to note that the side you choose to plate your ultrasonic range finder will affect the implmentation of the control law. 

Now, implement a proportional controller given the steps that you have previously followed and the tips noted above. 

Watch this video to see what a working wall-follower looks like. 

 .. image:: wallfollowing.gif


Implementing Wall Following
===========================

Today, let's use the information we learned last time to actually implement a wall-follower. 

Here is some code that would allow your XRP to track a wall on the right side of the robot. 

.. error:: 

    TODO add a visual and complete code to complete this
