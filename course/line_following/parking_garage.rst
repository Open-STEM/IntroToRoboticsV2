Parking Garage Challenge! (Bonus Activity)
===========================================

Now that we've learned how to follow lines using a proportional controller, let's try to apply this knowledge to a more complicated scenario: a parking garage!

The Goal
~~~~~~~~

The primary goal of our robot is to successfully find and park in an empty space. 

To accomplish this goal, we can break the problem down into 2 smaller steps: 

1. Find an empty parking spot
2. Properly park in the empty parking spot

Finding an Empty Parking Spot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main process we will employ here is simple: 

1.  Go forward the length of a parking spot 
2.  Turn 90 degrees right and check to see if the parking spot is open
3.  If the parking spot is not open, turn 180 degrees left and check to see if the parking spot on the left is open
4.  If both parking spots are not open, turn back to straight using the line following understanding_the_sensor

In order to see if a parking spot is open, we can use our ultrasonic range finder and see if there is any object in a parking spot. 

Leveraging the Line Following Sensors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this activity, we can use our line following sensors for three main purposes:

1.  To follow the line on the ground to the next parking spot
2.  To detect the "end" of the parking spot
3.  To turn back to straight after checking the left parking spot

In terms of following the line, we can use the same proportional controller that we used in the previous activities. 

As for detecting the end of the parking spot, we can use the same logic that we used when detecting an intersection. 

Finally, to turn back to straight, we can turn the XRP clockwise until the left line following sensor detects the line.

By breaking this complicated problem down into a series of smaller steps, we can easily program our XRP to park itself!

.. TODO a graphic would be super useful throughout this section 
.. also include code and a video of the robot parking itself
