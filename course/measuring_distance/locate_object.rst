Locating a Nearby Object
===========================

Another way to utilize the ultrasonic rangefinder is to use it to locate a nearby object. 

.. admonition:: Try it out

    What's the most effective way to locate an object? Try it out!

Turn and Detect
~~~~~~~~~~~~~~~

To first detect an object, the robot can slowly spin in a circle while continuously polling the rangefinder.
Then, when an object is detected to be within a certain distance, the robot can assume it has found an object,
stop spinning, and head towards the object.

To code this, we can start by setting the drive motor speeds to spin in opposite directions to start spinning
the robot in place. Then, we can utilize a while loop to keep spinning while the distance reading is greater than
some threshold, meaning that the robot has not yet found an object. Once the distance reading is less than the
threshold, the robot can stop spinning and head towards the object.

In the following example code, we use a variable to store our "distance threshold" of 20 cm.

.. error:: 

    TODO insert a video and code of a working example

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