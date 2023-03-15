Improving Driving Forwards
==========================
In order to implement wall following, you could have used Proportional Control. If you are too close to the wall, you could slow down the wheel farther from the wall, and speed up the closer one. In this way, you could turn away from the wall. If you're too far, you could to the opposite.

//insert video
 

In the video, the left wheel is farther from the wall. If the robot is too far from the wall, the left wheel needs to speed up. 

 

The control law can be summed up like this --
.. math:: leftWheelEffort = defaultEffort + K_p \\cdot error
.. math:: rightWheelEffort = defaultEffort - K_p \\cdot error

 

 

Using Proportional Control to drive straight
--------------------------------------------
If we want to drive straight, we want both of the wheels to drive the same distance. 

If the left wheel encoder reads that the left wheel has gone "300 clicks", and the right wheel reads "280 clicks", it probably means that the robot has driven in a little bit of an arc. 

How do we keep these robots driving in a straight line using proportional control? What would we use as the "error"? In previous activities we used the distance between where the robot was and where it needed to be. 

What can we use as the error now? Once we find the error, how do we correct for it? Try implementing a function that uses proportional control to drive straight for 30 cm. 


After you implement these, try and find where it's going wrong. How can you fix these problems? Are there any other ways we can correct for error?