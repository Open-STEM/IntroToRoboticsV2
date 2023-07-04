Implementing a Proportional Controller
=================

Now that you've learned about proportional controllers, let's implement one on the train activity

Steps
-----------------------------------

The first step when creating a proportional controller is to define your target and error terms. For our target, let's set it to 20 cm and for our error, let's use the difference between the target and the current distance from the object in front of the XRP. 

Now, we need to define our proportional gain. Let's set it to 0.5 for now. 

Then, we need to calculate our control signal. Remember, the control signal is the product of the proportional gain and the error.

Finally, we need to set the speed of the XRP to the control signal.

This is an example program that implements a proportional controller. 

[insert code]


