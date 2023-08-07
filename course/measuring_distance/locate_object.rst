Locating a Nearby Object
===========================

Another way to utilize the ultrasonic rangefinder is to use it to locate a nearby object. 

.. admonition:: Try it out

    Before reading more, brainstorm different ways to use the ultrasonic rangefinder to locate a nearby object. 

How?
~~~~

The easiest way to explain the intuition behind this process is sonar. 

The robot will essentially spin in a circle and take a distance reading while it spins.

Then, when an object is detected to be within a certain distance, the robot will stop spinning and go towards the object. 

This is a very simple way to locate an object, but it is also very effective (and will be especially helpful during your final project). 

The First Step
~~~~~~~~~~~~~~

The first step is to spin the robot in a circle and stop when an object is detected.

To do this, utilize a while loop which instucts the robot to spin in a circle while the distance reading is greater than a certain value.

In the following example code, our "distance threshold" is 20 cm.

.. error:: 

    TODO insert a video and code of a working example

The Second Step
~~~~~~~~~~~~~~~

The second step is to go towards the object and stop when the object is within a certain distance.

To do this, integrate the code from the previous example and add a while loop which instructs the robot to move forward while the distance reading is greater than a certain value.

In the following example code, our "distance threshold" is 5 cm.

.. error:: 

    TODO insert a video and code of a working example

The Problem with this Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The problem with this method is that it is not very accurate.

The reason for this is that our robot is currently acting on the "edge" of the object that it sees. 

This means that the robot will not be able to accurately locate the center of the object.

The Solution
~~~~~~~~~~~~

The solution to this problem is to use "flags" to keep track of the edges of an object. 

In this case, we can use a "first edge" flag and a "second edge" flag.

The first edge flag will be set to true when the robot first detects a sudden decrease in distance measurements (i.e. the robot detects the first edge of an object)

When the first edge is set to be true, the robot will take note of that angle, let's call it "firstAngle"

The second edge flag will be set to true when the robot detects a sudden increase in distance measurements (i.e. the robot detects the second edge of an object)

Now that the second edge is also set to be true, the robot can then take note of that angle, let's call it "secondAngle".

We then know that the center of the object is at the angle halfway between firstAngle and secondAngle.

To find that angle, we can take the average of firstAngle and secondAngle; and then save that angle as "centerAngle".

This method will allow the robot to accurately locate the center of an object.

.. error:: 

    TODO insert a video and code of a working example