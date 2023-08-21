Using the Web Server as a Dashboard 
===================================

The most useful application of the webserver is as a dashboard. The webserver can display live-updated 
data from the robot, which can be a great debugging tool. Printing values that your robot calculates or 
senses can help you understand why a bug is occuring because these values might not be what you expect, 
and the only way to determine them is to read them as the program runs.

You can send a value to the web server with just one line. 
The :code:`webserver.log_data(label, data)` function will create a label on the webserver with the corresponding data. 
If you call this multiple times, it will update the label on the webserver with the most recent value, which is how it is live-updated.

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.defaults import *

            webserver = Webserver.get_default_webserver()

            rangefinder = Rangefinder.get_default_rangefinder()

            webserver.log_data("Distance", rangefinder.distance())

            # Uses defaults from secrets.json  
            webserver.start_network()  
            webserver.start_server()

    .. tab-item:: Blockly

        .. image:: media/dashboard.png
            :width: 600

Now, after running this code, you may have noticed that it isn't live-updating. This is because the log_data function is only being called once.
Your first instinct may be to put this in a loop, but that won't work because the webserver takes control of the main event loop.
To get your data updating automatically, we can use the MicroPython :code:`Timer` class.

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.defaults import *
            from machine import Timer

            webserver = Webserver.get_default_webserver()

            rangefinder = Rangefinder.get_default_rangefinder()

            def update_distance(timer):
                # We move the log_data call into this function so that it is called every time the timer is triggered
                webserver.log_data("Distance", rangefinder.distance())

            # Timer(-1) creates a timer that is not attached to any hardware, so it is purely a software timer
            timer = Timer(-1)
            # The timer is set to trigger the update_distance function every 1000 milliseconds (1 second)
            timer.init(period=1000, mode=Timer.PERIODIC, callback=update_distance)

            # Uses defaults from secrets.json  
            webserver.start_network()  
            webserver.start_server()

    .. tab-item:: Blockly

        This is not yet supported in Blockly.

This will now update the distance every second. You can change the period to whatever you want. 
One thing to take note of here is that the function that is called by the timer must take one parameter, which is the timer itself.
We don't use this parameter in this example, but it is required to be there.

Now you can use this to debug your robot. You can add as many labels as you want, and in the future there will be more logging options available.