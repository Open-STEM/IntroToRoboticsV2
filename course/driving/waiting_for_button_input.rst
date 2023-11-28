Waiting for Button Input
========================

You may have noticed that your code runs immediately after uploading it. This is
nice sometimes, but sometimes you aren't coding in the same place you will be
running your code, and the robot suddenly driving itself off the table isn't an
ideal result. In order to have the code run on command, we can use the on board
buttons to tell the code when to run.

The XRP has a button which you can read from code. To make it easy, **XRPLib**
has a built in function which will wait for the button to be pressed for you.

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python
            
            from XRPLib.defaults import *
            from time import sleep

            board.wait_for_button()
            sleep(1)
            drivetrain.straight(20)

    .. tab-item:: Blockly

        .. image:: media/waitForButton.png
            :width: 300

This function is part of :code:`board` since the button is on the XRP's main 
controller board.

This code will wait until the button is pressed, and then wait an additional 
1 second (for you to get your finger out of the way) and then start driving.

There is also a function which lets you read the current state of the button
without waiting for it:

.. code-block:: python

    board.is_button_pressed()

You could use this function as the *condition* for a :code:`while` loop if you
wanted to do something more complicated with the button than just waiting for
it.