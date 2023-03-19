Wall Following
==============
You've built a control law for proportional control that lets you stand off from a wall. Now how do you use it to stay a certain distance from a wall while driving? 

[insert video]

Building a control law
----------------------
What do we want to do when we are too close to the wall? how do we start to move farther from the wall?

What do we want to do when we're too far? 

 

Remember:

    If we want the robot to drive forward, we can set the motor efforts to the same value. Let's start with "0.5" maybe.

    If we want the robot to turn left slowly, we can slow the left wheel down by a little. If we want it to turn towards the right, we can slow the right wheel down. 

 

Try implementing the control law you develop to follow the wall at a distance of 20 cm. Remember that you can tune values like the "driving forward effort" (as an example, we could use 0.2 instead of 0.5).

You can clip the sensor on the side to get the distance your robot is from the wall. 

Problems
--------
Once you implemented your control law, try and think about what the problems are.

What happens if you start too far? Is the distance you are getting from the wall accurate? 

How would you solve the problems. Are there any variables you can tune to try to solve some of these problems maybe?