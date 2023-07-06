Implementing a Proportional Controller
======================================

Now that you've learned about proportional controllers, let's implement one on the train activity

Steps
-----

The first step when creating a proportional controller is to define your target and error terms. 

For our target, let's set it to 20 cm. 

The error is the difference between the target and the current distance from the object in front of the XRP. 

Now, we need to define our proportional gain. 

    The first step of this is understanding the range of values that the error can take.

    The error can be any value between -20 and 20, meaning we're really close or really far. 

    Then, the error would need to be scaled for an appropriate control signal (something from -1 to 1)

    Therefore, a good starting kp value would be 0.05. 

Then, we need to calculate our control signal. Remember, the control signal is the product of the proportional gain and the error.

Finally, we need to set the speed of the XRP to the control signal.

This is an example program that implements a proportional controller. 

[insert code]


