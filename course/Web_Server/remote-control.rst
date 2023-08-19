Remotely Controlling your XRP
=============================

you've learned how to move the XRP with basic drive commands, but using the web server to remotely control 
the XRP gives you much more freedom.

The XRP Web server has built in buttons to go forward, back, left, right, and stop. 
All you need to do is add whatever command you want into that button, so when pressed, 
the web served will run that command.

here is an example of code that uses these buttons to drive:

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python
            from XRPLib.webserver import Webserver
            from XRPLib.differential_drive import DifferentialDrive

            webserver = Webserver.get_default_webserver()

            differentialDrive = DifferentialDrive.get_default_differential_drive()


            def forward():
            differentialDrive.set_effort(0.5, 0.5)

            webserver.registerForwardButton(forward)

            def back():
            differentialDrive.set_effort((-0.5), (-0.5))

            webserver.registerBackwardButton(back)

            def left():
            differentialDrive.turn(90, 0.5)

            webserver.registerLeftButton(left)

            def right():
            differentialDrive.turn((-90), 0.5)

            webserver.registerRightButton(right)

            def stop():
            differentialDrive.stop()

            webserver.registerStopButton(stop)

            webserver.start_network(ssid="xrp_1", password="")
            webserver.start_server()

    .. tab-item:: Blockly

        .. image:: media/rc-blockly.png
            :width: 600

with this code, you can wirelessly drive your XRP!