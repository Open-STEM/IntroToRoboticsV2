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


Finally, we need to set the speed of the XRP to our error times kp.

This is an example program that implements a proportional controller. 

[insert code]

.. admonition:: Try it out
    
    Now that you've designed a successful proportional controller, let's try some other values for kp.

    First, let's try making kp too small (0.01). What happens?

    When kp is too small, the XRP doesn't react fast enough to the error, and it takes a long time to get to the target. 

    Next, let's try making kp too big (1). What happens?

    The behavior you're seeing is called oscillation and happens when kp is too high. 

