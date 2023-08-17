Proportional Control With The IMU
=================================

Introduction:
-------------

The XRP's circuit board contains a very useful sensor called an inertial measurement unit (IMU). 
This sensor uses several internal senors to determine what direction the robot is pointing in, as well as 
the acceleration in its primary directions.

.. image ::
    media/6dof.jpg

.. note:: 
    The imu measures the acceleration in centimeters per second squared in the 3 main directions: 
    forward and backward (z), side to side (x), and up and down (y).
    It also measures the ange in degrees with yaw (turning side to side), pitch (pointing up or down),
    and roll (tilting to a side)

Getting these values is easy. The functions for getting acceleration in any axis are below:


.. tab-set:: 

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.imu import IMU

            imu = IMU.get_default_imu()
            imu.calibrate(1)


            imu.get_acc_x()

            imu.get_acc_y()

            imu.get_acc_z()

    .. tab-item:: Blockly

        .. image:: media/acceleration-blockly.png
            :width: 600

Getting the angles in each axis is just as easy, the functions for doing so are below:

.. tab-set:: 

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.imu import IMU

            imu = IMU.get_default_imu()
            imu.calibrate(1)


            imu.get_yaw()

            imu.get_roll()

            imu.get_pitch()

    .. tab-item:: Blockly

        .. image:: media/gyro-blockly.png
            :width: 500

You can use these values to determine the direction your robot is pointed in, the steepness of a surface 
it is driving up, or even the sideways tilt if it is driving on an uneven surface.

Turning With The IMU
--------------------

Turning to an angle is the most common use of the IMU. If you know what heading you want your 
robot to turn to, you can set up a proportional control loop to move your measured heading to your desired heading.

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            import math
            from XRPLib.imu import IMU
            from XRPLib.encoded_motor import EncodedMotor
            from XRPLib.differential_drive import DifferentialDrive

            targetAngle = None
            kP = None

            imu = IMU.get_default_imu()
            imu.calibrate(1)

            motor1 = EncodedMotor.get_default_encoded_motor(1)

            differentialDrive = DifferentialDrive.get_default_differential_drive()

            def turn(targetAngle):
                global kP
                kP = 0.015
                while not (math.fabs(targetAngle - (imu.get_yaw())) < 3 and (motor1.get_speed()) < 5):
                    differentialDrive.set_effort((((targetAngle - (imu.get_yaw())) * kP) * -1), ((targetAngle - (imu.get_yaw())) * kP))
                differentialDrive.stop()


            turn(90)

    .. tab-item:: Blockly
        
        .. image:: media/gyroturn-blockly.png
            :width: 600


