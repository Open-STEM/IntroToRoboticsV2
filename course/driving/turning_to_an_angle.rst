Turning To an angle
===================

If you want to turn your XRP to a certain angle, there are two ways to do this.

Turning With The IMU
--------------------

Turning with the IMU is the simpler method. The IMU, or Inertial Measurement Unit, is a device that can 
measure, among other things, the heading of your XRP in degrees. If you know what heading you want your 
robot to turn to, you can set up a proportional control loop to move your measured heading to your desired heading.

.. tab-set::
    .. tab-item:: Python
        .. code-block:: python
            

    .. tab-item:: Blockly
        .. image:: 
            :width: 300


Turing With Encoders
--------------------

Turning with encoders is a bit more complicated, and it involves a bit of math. To turn with encoders, you 
need to know how many encoder counts the wheel has to rotate to turn a certain number of degrees. 
