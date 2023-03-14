Controlling Behavior: Introduction
==================================

The main purpose of sensors is to introduce feedback into the system. During actuation, the state of the robot and its environment is continuously changing. Feedback informs the system how much the state has changed and how much more the state should change. Feedback introduces more control over autonomous behavior - a fundamental characteristic of all intelligent robots!

Incorporating Feedback
----------------------

Your sensors tell you where you are. Robots need to understand where they are in order to make decisions about where to go, and so do you. When driving, you can choose to go faster or slower. In order to know whether to go faster or slower you need to know the speed limit, the speed of your car, and the speed of the car in front of you.

[insert image]

You can tell how fast you are using your speedometer, and you can see how fast the car in front of you is going. These are **sensor inputs**, and you want to take these into account when deciding whether to drive faster or slower. How a robot decides to move is called it's **control law**.

For the XRP robots, your control law will decide how much effort to use on each wheel depending on where you want to go and what sensor inputs you have. You're going to design your own robot control law.

Python Programming Note: If Statement
-------------------------------------

An if statement will execute its inner code block if its specified condition is met. For example:

.. code-block::python
	if True:
	    print("Hello World!")

The if statement above will print "Hello World!" because its condition is true.

.. code-block::python
	if False:
	    print("Hello World!")


The if statement above will not print "Hello World!" because its condition is always false.

.. code-block::python
	int i = 3;
	if i < 5:
	    print("Hello World!")

The if statement above will print "Hello World!" because the variable "i" is less than 5, satisfying the condition. 

You can imagine how this might be used in a control law.

Maybe it could be something like -- "If your sensors see that you are exactly where you need to be, you don't need to do anything!"

