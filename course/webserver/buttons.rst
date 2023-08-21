Creating Custom Webserver Buttons
==========================================

Last lesson, you learned how to bind simple drive commands to the arrow buttons.
But, what if you want to perform more complicated code tasks? or what if you have more than 5 commands you want to run from the webserver?

Well, XRPLib provides the tools to do that! 
With the :code:`webserver.add_button(label, func)` method, you can add any function you want to the webserver,
along with a helpful label that describes what your function does!

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.defaults import *

            def raiseArm():
                servo_one.set_angle(100)

            def lowerArm():
                servo_one.set_angle(0)

            def led_blink():
                board.led_blink(5)

            def led_stop():
                board.led_off()
            
            def square():
                # Drives in a square with 20cm sides
                for side in range(4):
                    drivetrain.straight(20)
                    drivetrain.turn(90)

            webserver.add_button("Raise Arm", raiseArm)
            webserver.add_button("Lower Arm", lowerArm)
            webserver.add_button("Blink LED", led_blink)
            webserver.add_button("Stop LED", led_stop)
            webserver.add_button("20cm Square", square)

            webserver.start_network()
            webserver.start_server()

    .. tab-item:: Blockly

        .. image:: 
            media/custom-buttons.png


After running this code, you should see your new button(s) appear under the Custom Buttons section of the web page!
Note: We recommend leaving your robot plugged in the first time you run a new function on the webserver, 
just to make sure that it doesn't have any errors.

And there you go! That's all the basics of how to use the webserver!