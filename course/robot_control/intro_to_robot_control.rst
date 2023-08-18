Controlling Behavior: Introduction
==================================

Now that robot has information about it's environment (through the use of sensors), let's go over how we can use this information to control our robot's behavior.


Open Loop Control
-----------------

Before incorporating sensor information, let's go over a simple, open-loop controller. 

All this means is that we are going to tell the robot to do something without checking to see if it actually did it.

For example, an oven is an open-loop controller. If you set the cook time to 30 minutes, the oven will cook for 30 minutes regardless of whether or not the food is actually done.

This is a useful controller for simpler processes like ovens that don't need to adapt to their environment. However, for more complex processes like autonomous cars, we would want to incorporate sensor information to make sure that the car is actually doing what we want it to do.

Closed Loop Control
-------------------

Closed loop control is when we use sensor information to control our robot's behavior.

For example, a self-driving car is a closed-loop controller. It uses sensor information to determine if it is in the correct lane, if it is too close to other cars, etc. and adjusts its behavior accordingly.

In this lesson, we will be using closed-loop control to control our robot's behavior, specifically, we will cover discrete control. 

Python Programming Note: Conditionals
-------------------------------------

A conditional is a statement in code where the program will only execute a certain block of code if a certain condition is met.

In the context of on-off controllers, "if statements" are an important type of conditional and are shown in this example:

.. tab-set::

	.. tab-item:: Python

		.. code-block:: python

			if True:
				print("Hello World!")

	.. tab-item:: Blockly

		.. image:: media/if_true.png
			:width: 300

The if statement above will print "Hello World!" because its condition is true.

.. tab-set::

	.. tab-item:: Python

		.. code-block:: python

			if False:
				print("Hello World!")

	.. tab-item:: Blockly

		.. image:: media/if_false.png
			:width: 300

The if statement above will not print "Hello World!" because its condition is always false.

.. tab-set::

	.. tab-item:: Python

		.. code-block:: python

			int i = 3
			if i < 5:
				print("Hello World!")

	.. tab-item:: Blockly

		.. image:: media/condition.png
			:width: 300

The if statement above will print "Hello World!" because the variable "i" is less than 5, satisfying the condition. 

In simpler controllers, if statements can be used to define our "control law". A control law is a set of rules that determines how our robot should behave.

On-off Control
--------------

On-off control is a simple closed-loop controller that uses a binary signal (on or off) to control a process.

For example, a thermostat is an on-off controller. If the temperature is below the target temperature, the thermostat turns on the heater. If the temperature is above the target temperature, the thermostat turns off the heater.

In this lesson, we will be using on-off control to control our robot's behavior. Specifically, we will use an on-off controller to "standoff" our robot from an object.