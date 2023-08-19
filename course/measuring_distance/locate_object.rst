Locating a Nearby Object
===========================

Another way to utilize the ultrasonic rangefinder is to use it to locate a nearby object. 

.. admonition:: Try it out

    What's the most effective way to locate an object? Try it out!

Turn and Detect
~~~~~~~~~~~~~~~

To first detect an object, the robot can slowly spin in a circle while continuously polling the rangefinder.
Then, when an object is detected, it can stop spinning, and head towards the object.

How can we tell when an object is detected? Imagine that the robot is in the center of an empty room, and a
random object is placed somewhere near the robot. The rangefinder would be giving large distance readings, until
it reaches the object, at which point the distance reading would drop. It's the *change* in distance readings that
hints that an object has been detected.

How can we find the change in distance readings over each iteration of the loop? We can store the previous distance
reading in a variable, and compare it to the current distance reading. If this change is greater than some threshold,
then we can assume that an object has been detected.

But, it's possible that there are some objects super far away that still result in a large change in distance readings.
To avoid this, we can set a maximum distance threshold, and only consider an object to be detected if it's within some
maximum distance.

To code this, we can start by setting the drive motor speeds to spin in opposite directions to start spinning
the robot in place. Then, we can utilize a while loop to keep spinning while the distance reading is greater than
some threshold, meaning that the robot has not yet found an object. Once the change distance reading is greater than
the threshold, the robot can stop spinning and head towards the object.

In the following example code, we use a change threshold of 15cm, and a maximum distance threshold of 40cm.

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            changeThreshold = 15 # distance change in cm needed to trigger detection
            maximumDistance = 40 # maximum distance in cm to consider an object detected

            # store initial values for current and previous distance
            currentDistance = rangefinder.distance()
            previousDistance = currentDistance

            # start spinning in place until an object is detected
            differentialDrive.set_speed(5, -5)

            # repeat until change in distance is greater than threshold, and current distance is less than maximum
            while not (previousDistance - currentDistance > changeThreshold and currentDistance < maximumDistance):
                
                time.sleep(0.1)

                # update previous and current distance
                previousDistance = currentDistance
                currentDistance = rangefinder.distance()

            # stop spinning
            differentialDrive.stop()


    .. tab-item:: Blockly

        .. image:: media/detection.png
            :width: 900

Improving Accuracy
~~~~~~~~~~~~~~~~~~

Do you see any issues with this solution?

When the rangefinder distance dips below the threshold, the implication isn't that the robot has found an object,
but rather that the robot has found its *edge*. So, the robot will aim for the edge of the object, rather than the center.

Instead, the robot should remember the heading it faces when detecting *both* edges. Then, the robot can aim for the center
between those edges, and thus the center of the object. We can store each edge angle in variables, naming them :code:`firstAngle`
and :code:`secondAngle`.

Let's walk through the code step by step.

First, the robot should spin in place until it detects the first edge, then stop. The code should be similar as before.

[code]

Next, we want to record the robot's heading for this first edge, and store it to :code:`firstAngle`.

[code]

Then, the robot should spin in place again until it detects the second edge, then stop. The whole time while the robot is spinning
from the first to second edge, it should be detecting the object in close proximity, so the robot should know its hit the second
edge when the distance reading is greater than the threshold again, plus a few cm, in case the object is slightly concave.

[code]

Once the robot has detected the second edge, it should record its heading and store it to :code:`secondAngle`. Now, need to figure
out how much the robot needs to backtrack to aim for the center of the object. We can do this by finding the difference between
the two angles, and dividing by two. This is half the angle between the two edges, and if the robot backtracks by this amount,
it will be facing the center of the object. Let's store this in a variable called :code:`angleToTurn`.

[code]

Finally, the robot can turn this much to face the center of the object, and head towards it.

Here's the full code:

[code]