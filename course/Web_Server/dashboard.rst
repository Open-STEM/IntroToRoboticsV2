Using the Web Server as a Dashboard 
===================================

The most useful application of the seb server is as a dashboard. The web server can display live-updated 
data from the robot, which can be a great debugging tool. Printing values that your robot calculates or 
senses can help you understand why a bug is occuring because these values might not be what you expect, 
and the only way to determine them is to read them as the program runs.

You can send a value to the web server with just one line. The example code for printing the distance
found by the ultrasonic sensor is below. You can use this one command to print any data you want with any
label you want 

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.webserver import Webserver
            from XRPLib.rangefinder import Rangefinder

            webserver = Webserver.get_default_webserver()

            rangefinder = Rangefinder.get_default_rangefinder()


            webserver.log_data("distance", (rangefinder.distance()))

    .. tab-item:: Blockly

        .. image:: media/dashboard.png
            :width: 600

