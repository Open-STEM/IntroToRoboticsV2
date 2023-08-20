Remotely Controlling your XRP
=============================

With the webserver, you can also control your XRP remotely.
The webserver class has a few methods that allow you to register functions to be called when an arrow button is pressed,
which we can use to control the XRP. 

Below is an example of how to register some basic drive functions to be called when the arrow buttons are pressed:

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.defaults import *

            def forward():
                differentialDrive.set_effort(0.5, 0.5)

            webserver.registerForwardButton(forward)

            def back():
                differentialDrive.set_effort(-0.5, -0.5)

            webserver.registerBackwardButton(back)

            def left():
                differentialDrive.set_effort(-0.5, 0.5)

            webserver.registerLeftButton(left)

            def right():
                differentialDrive.set_effort(0.5, -0.5)

            webserver.registerRightButton(right)

            def stop():
                differentialDrive.stop()

            webserver.registerStopButton(stop)

    .. tab-item:: Blockly

        .. image:: media/rc-blockly.png
            :width: 600

These functions are then registered to the webserver, and when the arrow buttons are pressed, the corresponding function is called.
The arrows will appear if any of these functions are registered, and will be disabled if they are not.

.. note::
    You can also use lambda functions to register functions to the webserver, 
    which can be useful for simple functions, but are out of scope for this lesson.
