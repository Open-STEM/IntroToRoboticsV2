Driving a Distance
==================

Controlling your speed
----------------------

In addition to setting the effort of the drivetrain's motors, we can also set 
their *speed*. Remember, effort is not the same as speed. We can also ask the 
XRP's motors to go a certain speed. When using this function, the XRP will
actively measure the speed of the wheels using the motor's *encoder*. If the 
speed falls too low, the motor will automatically increase the effort it applies
to speed back up.

.. tip:: 

    Don't worry if you've never heard of an *encoder*. We'll talk more about 
    them later in the lesson.

To set the speed of the drivetrain motors, we use a new function:

.. tab-set:: 

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.defaults import *

            drivetrain.set_speed(5, 5)

    .. tab-item:: Blockly

        .. image:: media/setspeedexample.png
            :width: 300

This tells the drivetrain to set the speed of each drivetrain wheel to travel at
5 centimeters per second. This means if you put the robot down and let both motors
drive at this speed, the robot would move 5 centimeters forwards each second.

.. admonition:: Try it out

    Add the code to your program and run it. Try the same exercise of pushing 
    something up against the wheels of your XRP. Notice how as you add 
    resistance, the motor will increase its effort to keep the speed constant.
    When you remove the resistance, the effort will go back down.

Since both wheels are now going the same speed, your robot should now also drive
straight, unlike when using the :code:`set_effort` function.

.. tip:: 
    
    If you want the robot to go backwards, use a negative speed value just like
    you did with the effort value.

Driving a distance
------------------

We know that we can ask the wheels to spin at a certain speed using a function, 
but what if we want to make the robot drive a certain distance?

We could ask the robot to move at some speed, and if we know how far it will 
move each second (for this example we are using a speed of 5 cm/s), we can calculate
how many seconds we should drive for to reach that distance.

Let's use :math:`d` to represent the distance we want to drive in cm. But, we want
a number in seconds, so we need to convert by the means of *dimensional analysis*.

To do this, write an expression for the known value with units included:

.. math::
    (d  \text{ cm})

Dimensional analysis involves multiplying this expression by special representations
of "1" to convert units. In this case, our speed is 5 cm per second, so we can equate
:math:`5 \text{ cm} = 1 \text{ second}`. Rearranging, we have our special representation of 1:

.. math:: 

    \frac{1 \text{ second}}{5 \text{ cm}} = 1

We can now multiply our expression with this special representation of 1:

.. math::
    (d \text{ cm}) \cdot \frac{1 \text{ second}}{5 \text{ cm}}

Cancelling out units and simplifying, we obtain:

.. math::
    (d  \cancel{\text{ cm}}) \cdot \frac{1 \text{ second}}{5 \cancel{\text{ cm}}} = \frac{d}{5} \text{ seconds}


This resultant expression makes sense! If we want to go 5 cm, we plug in d = 5, and :math:`\frac{5}{5} = 1`,
so we drive for one second. If we want to go 2.5 cm, we plug in d = 2.5, and :math:`\frac{2.5}{5} = 0.5`,
so we drive for half a second.

Keep in mind that this equation is only valid if the robot is moving at 5 cm per
second. If you change that speed to be faster or slower, you'll need to change
the denominator of the fraction to that speed to fix the equation.

.. admonition:: Try it out

    Calculate how many seconds you need to drive for to go one meter if your 
    robot is moving at 5 cm per second. Remember, there are 100 cm in a meter.

To put the above theory into practice, we need to learn about a new function in Python: 
:code:`sleep`, which makes the XRP wait for some number of seconds before 
continuing to the next instruction in the code.

.. tab-set:: 

    .. tab-item:: Python

        .. code-block:: python

            from XRPLib.defaults import *
            from time import sleep # We need to import the speed function to use it.

            drivetrain.set_speed(5, 5)
            sleep(x) # replace x with the time you calculated to go one meter.
            drivetrain.stop() # This is another function which makes it easy to stop the robot


    .. tab-item:: Blockly

        .. image:: media/setspeedandsleep.png
            :width: 300

.. tip:: 
    
    The :code:`#` symbol in Python creates a *comment*. If you add one to a line
    of code, anything that comes after it on that line will be ignored by the 
    robot. You can use it to leave notes for yourself, or to quickly disable a 
    line of code while debugging problems.

    We use comments in our examples to give you hints about how to write your
    code. You don't need to copy our comments into your code, but you should
    write your own so that you can easily remember what your code does.

.. admonition:: Try it out

    Add the code to your program and try it out. Remember to replace :code:`x` 
    with the value you calculated. Try running your robot next to a meter stick
    to see how accurately your robot drives!

This code you wrote is pretty useful, but what if you wanted to drive other 
distances?

Let's say that we want to drive three distances in a row: 25, 50, and 75 cm.
How could we program the robot to do this? The easy solution is to copy and 
paste the code you wrote before three times, and modify it each time:

.. add blockly tab once math can be inputted into "sleep" block
.. code-block:: python

    from XRPLib.defaults import *
    from time import sleep

    # Drive 25 cm
    drivetrain.set_speed(5, 5)
    sleep(25 / 5) # Notice how we can write math directly in our program!
    drivetrain.stop()

    # Drive 50 cm
    drivetrain.set_speed(5, 5)
    sleep(50 / 5)
    drivetrain.stop()

    # Drive 75 cm
    drivetrain.set_speed(5, 5)
    sleep(75 / 5)
    drivetrain.stop()

This looks pretty repetitive. Most of this code is exactly the same. In fact,
the only change between each block is the parameter we are passing to the
:code:`sleep` function. This is a perfect example of why we have functions.
Let's write our own function to drive the robot a certain distance.

.. tab-set:: 

    .. tab-item:: Python

        Python uses the keyword :code:`def` to let you, the programmer, tell it that you
        would like to *define* a new function. A full function definition looks like 
        this:

        .. code-block:: python

            def function_name(parameter1, parameter2, parameter3):
                # put your code here
                # code in your function can use the parameters by name like this:
                print(parameter1 / 5)

        In this example function, there are three parameters. Functions can have as 
        many or as few parameters as you want, or even have no parameters at all.

    .. tab-item:: Blockly

        In Blockly, you create functions by dragging a block that looks like the picture
        below. The interface allows you to specify the function name, and pass *parameters*
        to the function body. Here, we have a function called some_task (which you should rename
        based on what your function does) that takes in a parameter called :code:`text`, and uses
        prints the :code:`text` value. Functions can have as  many or as few parameters as you want,
        or even have no parameters at all.

        .. image:: media/blocklyfunctiondefinition.png
            :width: 300

        The below blocks *calls* the function we defined above to run it. The value "Hello" is passed
        to the :code:`text` parameter, which results in "Hello" being printed to the console.

        .. image:: media/blocklyfunctioncall.png
            :width: 300


.. admonition:: Try it out

    Define a function called :code:`drive_distance` that takes in one parameter: 
    :code:`distance_to_drive`. Use the parameter in your function as the 
    numerator of your fraction.

    Use your function to make the robot drive 3 distances in a row.

.. tip:: 

    Define your functions towards the top of your file, underneath the 
    :code:`import` statements. This way, code later in the file will be able to 
    use them.
