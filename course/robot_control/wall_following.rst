Introduction to Wall Following
==============================
Now that you've developed a program to keep a certain distance from an object, let's implement this by having the XRP follow a wall while maintaining a target distance.

Building a control law
----------------------

when you follow a wall, all you need to do is steer the robot so you can keep a certain distance from the wall.
If you are following a wall on your right side, you will turn right if you are too far and left if you are too close.
We can easily do this with a proportional control loop. The steering correction can be proportional to the error,
in this case the difference between the distance to the wall and the target distance to the wall.

 
.. tip::
   Remember that you will want to incorporate a "base effort" to ensure that the robot is moving forward at all times. Let's set this to **0.5**.

   It is also important to note that the side you choose to plate your ultrasonic range finder will affect the implmentation of the control law. 

Now, implement a proportional controller given the steps that you have previously followed and the tips noted above. 

Watch this video to see what a working wall-follower looks like. 

 .. image:: media/wallfollowing.gif


Implementing Wall Following
---------------------------

Today, let's use the information we learned last time to actually implement a wall-follower. 

Here is some code that would allow your XRP to track a wall on the right side of the robot. 

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.differential_drive import DifferentialDrive
            from XRPLib.rangefinder import Rangefinder

            kP = None
            targetDist = None

            differentialDrive = DifferentialDrive.get_default_differential_drive()

            rangefinder = Rangefinder.get_default_rangefinder()


            kP = 0.02
            targetDist = 20
            while True:
                differentialDrive.set_effort((0.4 + kP * ((rangefinder.distance()) - targetDist)), (0.4 + (kP * ((rangefinder.distance()) - targetDist)) * -1))


    .. tab-item:: Blockly

        .. image:: media/wall-follow-blockly.png
            :width: 600
