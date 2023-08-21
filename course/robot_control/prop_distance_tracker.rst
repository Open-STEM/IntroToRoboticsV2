Implementing a Proportional Controller
======================================

Now that you've learned about how proportional controllers, let's implement one for our distance tracking activity,
where we want to keep the robot some distance from the object in front of it using the rangefinder!

Defining Terminology
--------------------

Let's identify the terms we'll need to use in our code:

**Set Point** or desired value: In this example, this is some set distance from the rangefinder we want the robot to be at. 
For this example, let's say 20cm.

**Process Variable** or current value: We obtain our measured value from reading the rangerfinder value. This is
:code:`rangefinder.distance()`.

Our goal is for our process variable (the rangefinder distance) to approach the set point (20 cm).

Thus, our **error** is calculated as :code:`error = rangefinder.distance() - 20`. Note that :code:`error = 20 - rangefinder.distance()`
is also "correct". The distinction in sign is simply whichever makes more sense for your application. Here, if we had an error of 30cm,
we would want to drive forward 10cm, so we would want a positive error to make our motors spin forward.

**Control Output**: In this case, this is our motor effort. This is because we want to drive with a speed proportional
to the distance error. As a reminder for P control, this will be calculated as :code:`motor_effort = Kp * error`.

**Kp**: This is our proportional gain. Though we will need to tune this value, we can guess a somewhat reasonable value
by considering the range of values our error can take, and the domain of our control output. In this case, if we're 30cm away
from the object, our error will be 10. We can guess that at this sufficient distance we will want to drive forward at a maximum
effort of 1, as effort is restricted to the domain :math:`[-1, 1]`. Thus, we can guess that :code:`Kp = 1/10 = 0.1`. Of course,
this isn't likely the final value that works best for your robot, but it's a good starting point.

Implementing the Controller
---------------------------

Now that we've defined our terms, let's write the code!

Let's start by defining our proportional gain and our set point:

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            Kp = 0.1
            desired_distance = 20

    .. tab-item:: Blockly

        .. image:: media/variables.png
            :width: 300

Next, we want to enter some sort of loop to continuously read our rangefinder value and update our motor effort from our controller output.

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            Kp = 0.1
            desired_distance = 20
            while True:
                error = rangefinder.distance() - desired_distance
                motor_effort = Kp * error
                drivetrain.set_effort(motor_effort, motor_effort)
                time.sleep(0.05)

    .. tab-item:: Blockly

        .. image:: media/pcode.png
            :width: 500

Each iteration of the loop consists of the following steps:
    #. Read the rangefinder value to get the current distance
    #. Calculate the error
    #. Calculate the control output through Kp * error
    #. Set the drivetrain motor efforts to the control output
    #. Wait for a short period of time

This code should give us a working solution to maintain a set distance from the object in front of the robot!

.. admonition:: Try it out

    Try moving the object in front of the robot and watch the robot attempt to maintain the set distance! What
    happens when you increase Kp? Decrease it? What value of Kp works best for your robot?