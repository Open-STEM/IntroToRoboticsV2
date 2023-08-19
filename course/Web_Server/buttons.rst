Creating Custom Buttons for the Web Server
==========================================

In the last section, you learned how to remotely control your XRP using the built-in directional buttons. 
in addition to those, you can also create custom buttons that can run any code you want!

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.webserver import Webserver
            from XRPLib.servo import Servo

            webserver = Webserver.get_default_webserver()

            servo1 = Servo.get_default_servo()

            def func1():
            servo1.set_angle(90)

            webserver.add_button("raiseArm", func1)

    .. tab-item:: Blockly

        .. image:: 
            media/raise-servo.png


you can make a button run any function you can write, so get creative!