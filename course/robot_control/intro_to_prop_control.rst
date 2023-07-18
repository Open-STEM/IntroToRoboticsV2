Controlling Behavior: Continuous Controllers
============================================

Introduction:
-------------

While the on-off controller works, there are issues that can be solved using another type of controller.

The on-off controller is a **discrete** controller. This means that the controller has discrete states. It can be "on" or "off". It cannot be "half on" or "half off".

A **continuous** controller is one that can have any value. For example, the speed of a car is a continuous controller. It is not limited to "on" or "off".

Continuous controllers are more effective and offer the user more control over their system, but are also easier to implement. 

Basic Definitions + Steps of a Proportional Controller
------------------------------------------------------

A proportional controller is the simplest type of continuous controller. It is also known as a P controller. 

Before implementing one, we need to define some terms and steps. 

**Target Value** - The value that you want to go to. In this example, let's set our target value to 5 cm

**Error** - The difference between the target value and the actual value. For example, if you want to go to 5 cm but you are currently at 3 cm, then the error is 2 cm.

**Control Effort** - The value that the controller outputs.

**kp** - The constant that you scale the error by to get the control effort. For example, if you want to go to 5 cm but you are currently at 3 cm, then the error is 2 cm. If **kp** is 0.5, then the control effort is 1 (0.5 * 2 cm).

Now that we have defined some terms, let's go over the steps to implement a continuous controller.

1.  Define your target value 
2.  Find the error 
3.  Multiply the error by a constant **kp** to get the control effort 
4.  Feed the control effort into your system

Tips on finding "kp"
--------------------

Finding the right value for **kp** is a bit tricky. If **kp** is too small, then the system will not respond fast enough. If **kp** is too large, then the system will overshoot the target value and oscillate around it.

When first finding a **kp** value, you want to "scale" an expected range of errors into an acceptable control signal. 

For example, if your expected error ranges from 0-40 but your control signal ranges from 0-1, a "good" starting kp value would be 0.025 (1/40).\

From there, you can adjust the kp value to get the desired response after testing. 

