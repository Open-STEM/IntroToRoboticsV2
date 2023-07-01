Controlling Behavior: Introduction
==================================

Now that we know how to gain information about our environment through sensors, let's go over how we can use this information to control our robot's behavior.


Open Loop Control
----------------------

Before incorporating sensor information, let's go over a simple, open-loop controller. 

All this means is that we are going to tell the robot to do something without checking to see if it actually did it.

For example, a washing machine is an open-loop controller. You tell it to wash your clothes for 30 minutes, but it doesn't actually check to see if your clothes are clean after 30 minutes. It just stops after 30 minutes.

This is a useful controller for simpler processes like washing machines that don't need to adapt to their environment. However, for more complex processes like driving a car, we would want sensor information to acheive desired behavior. 

Closed Loop Control
----------------------

Closed loop control is when we use sensor information to control our robot's behavior.

For example, a self-driving car is a closed-loop controller. It uses sensor information to determine if it is in the correct lane, if it is too close to other cars, etc. and adjusts its behavior accordingly.

In this lesson, we will be using closed-loop control to control our robot's behavior, specifically, we will cover bang-bang control. 


Python Programming Note: If Statement
-------------------------------------

Before covering bang-bang control, let's go over a Python programming concept that we will be using in our control law: the if statement.

An if statement will execute its inner code block if its specified condition is met. For example:

.. code-block:: python

	if True:
	    print("Hello World!")

The if statement above will print "Hello World!" because its condition is true.

.. code-block:: python

	if False:
	    print("Hello World!")


The if statement above will not print "Hello World!" because its condition is always false.

.. code-block:: python

	int i = 3
	if i < 5:
	    print("Hello World!")

The if statement above will print "Hello World!" because the variable "i" is less than 5, satisfying the condition. 

In simpler controllers, if statements can be used to define our "control law". A control law is a set of rules that determines how our robot should behave.


Bang-Bang Control
----------------------

Bang-bang control is a simple closed-loop controller that uses a binary control signal (on or off) to control a process.

For example, a thermostat is a bang-bang controller. If the temperature is below the desired temperature, the thermostat turns on the heater. If the temperature is above the desired temperature, the thermostat turns off the heater.

In this lesson, we will be using bang-bang control to control our robot's behavior. Specifically, we will be using bang-bang control to "park" our XRP. 

Parking Activity
----------------------

To help us define our control law, let's first built a decision table. For each of these scenarios, do you want to go forwards or backwards?

.. list-table:: Title
   :widths: 50 50
   :header-rows: 1

   * - Sensor Input
     - Action, (go forwards or backwards?)

   * - You're a lot closer than **20 cm away**
     -
     	
   * - You're a little closer than **20 cm away**
     - 
     
   * - You're **20 cm away**
     - 
     
   * - You're a little farther than **20 cm away**	
     - 
     
   * - You're a lot farther than **20 cm away**
     -   
     
Try implementing this table using if statements on your robot. 

Design Thinking
---------------------

What are some problems you're running into?

* Does the robot stop?
* Does it move too fast?
* Does it move too slow?

Why are these problems happening, and how can they be solved?
