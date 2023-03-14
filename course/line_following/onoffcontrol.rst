Following the line: On/Off control
==================================

Line Following Basics
---------------------

Now, let's turn our attention towards one of the core challenges in the final project - following a line. In the project, the robot will need to drive to multiple different locations - but doing this blind can result in the robot drifting to an unexpected direction - the drive motors may not be rotating at the exact same speed resulting in the robot moving in a small arc, and the robot might not even be aimed at the right direction when going forwards.

By following a line, we can ensure that the robot stays in the exact path it should, eliminating drift over time. But how?

Consider using one of the reflectance sensors. As a refresher, gives a reading from 0 (black) to 1 (white). Assuming that the reflectance sensor is approximately at the center of the robot, it will at least partially reading the black line when the robot is centered on the line. What type of logic would we need if we wanted to follow the center of the line?

Well, if the reflectance sensor reads black, it means the robot is perfectly on the line, and we'd want to go straight, setting the motors at the same speed. But if the reflectance sensor reads grey or white, it would mean that the robot is partially or completely off the line. We'd want to correct this by steering it back to the center, but does it turn left or right?

Unfortunately, there's no way to tell. The robot has no way of knowing which direction it is drifting off the line. Instead, try following an edge of the line. If we try to follow the left edge, then there's two possible states in which the robot reacts.

* If the sensor reads closer to white, that means we're too far to the left, so we need to turn slightly to the right.
* If the sensor reads closer to black, that means we're too far to the right, so we need to turn slightly to the left.

And that's it! We want to keep polling (getting the value of) the reflectance sensor quickly, and at each time determine whether it's closer to white (with a value less than 0.5) or closer to black (with a value greater than 0.5), and depending on the result, either set the motor to turn right (set left motor speed to be faster than right) or turn left (set right motor speed to be faster than left).

This seems like a solution involving an if-else statement. Our condition would be related to whether the value is greater or less than 0.5.

Python Programming Note: example of an if-else statement. ::

    i = 21

    if i > 20:

        print("greater than 20")
    
    else:
    
        print("less than 20")

.. Image:: onoffcontrol.png

Above is an illustration of how we'd want the robot to act based on the reading of the sensor.


Mini Challenge: Line Following
------------------------------

Follow the left edge of a black line by turning right when the sensor reads closer to white, and turning left when the sensor reads closer to black.