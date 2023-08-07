Intersection into Drop Off  
=========================

Now that we've learned how to detect an intersection and develop custom functions, let's try to put it all together to create a program that can drop a basket off at a designated location.

The Process:  
------------

Let's first think about the process: 

We want to first detect an intersection and know that we can accomplish this by waiting for both line sensors to detect a line. 

Once we detect an intersection, we want to turn 180 degrees to ensure that we are facing the correct direction to drop off the basket.

Then, we want to travel a certain distance to ensure that we are at the correct location to drop off the basket.

Once we are at the correct location, we want to drop off the basket.

Then, we want to drive back to the intersection. Since we are already facing "backwards", this means that we don't have to correct our orientation before returning to the intersection.

Finally, we want to put the arm back into the starting position and start line following again.

Put together, this process can be broken into these steps:

1. Detect an intersection
2. Turn 180 degrees
3. Travel our desired distance
4. Drop off the basket
5. Drive back to the intersection
6. Put the arm back into the starting position
7. Start line following again

We can use the functions we've already created to do this:

.. error:: 

    TODO add code and a video 
