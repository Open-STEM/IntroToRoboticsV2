Distance Tracking 
=================

Now that we've covered on-off control, let's use that information to track an object from a certain distance. 

The Process
-----------

Essentially, we want our robot to go towards the object if it's too far and away from the object if it's too close. 

We can do this by using the distance sensor to determine how far away the object is and then using that information to determine how the direction in which the robot should be going.

For this activity, let's use a target distance of 30 cm. 

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.rangefinder import Rangefinder

            rangefinder = Rangefinder.get_default_rangefinder()

            while True:
                if rangefinder.distance() < 30:
                    drivetrain.set_speed(-20, -20)
                elif rangefinder.distance() > 30:
                    drivetrain.set_speed(20, 20)


    .. tab-item:: Blockly

        .. image:: media/SimpleStandoff.png
            :width: 300

You'll notice that this code causes the robot to move back and forth, or oscillate, as the sonar distance continuously swaps between being greater than and less than 30 cm.
So what if we add a third case that tells the robot's motors to stop when sonar distance equals 30 cm?

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.rangefinder import Rangefinder

            rangefinder = Rangefinder.get_default_rangefinder()

            while True:
                if rangefinder.distance() < 30:
                    drivetrain.set_speed(-20, -20)
                elif rangefinder.distance() > 30:
                    drivetrain.set_speed(20, 20)
                else:
                    drivetrain.stop()


    .. tab-item:: Blockly

        .. image:: media/SimpleStandoffStop.png
            :width: 300

Unfortunately, even with this code, our robot still doesn't stop! The issue is that the distance sensor is so precise that it
never reads exactly 30 cm. We can combat this by making our robot stop when it's *close* to 30 cm instead of *exactly* 30 cm.
We can do this by creating a range in which our robot stops called a "deadband." Using a range of +- 2.5 cm, our new code would look like this:


.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.rangefinder import Rangefinder

            rangefinder = Rangefinder.get_default_rangefinder()

            while True:
                if rangefinder.distance() < 27.5:
                    drivetrain.set_speed(-20, -20)
                elif rangefinder.distance() > 32.5:
                    drivetrain.set_speed(20, 20)
                else:
                    drivetrain.stop()


    .. tab-item:: Blockly

        .. image:: media/deadband.png
            :width: 300

This code should allow the robot to stop when it senses a sonar distance of ~30 cm. Our issue now is that
there is a potential error of +- 2.5 cm from our desired following distance. Luckily, there is a solution to this called "proportional control."
