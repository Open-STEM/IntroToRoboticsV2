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
            from XRPLib.differential_drive import DifferentialDrive

            rangefinder = Rangefinder.get_default_rangefinder()

            differentialDrive = DifferentialDrive.get_default_differential_drive()

            while True:
                if (rangefinder.distance()) < 27.5:
                    differentialDrive.set_effort((-0.3), (-0.3))
                elif (rangefinder.distance()) > 32.5:
                    differentialDrive.set_effort(0.3, 0.3)


    .. tab-item:: Blockly

        .. image:: media/SimpleStandoff.png
            :width: 300



