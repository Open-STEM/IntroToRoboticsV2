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

To code this, we can start by setting the drive motor speeds to spin in opposite directions to start spinning
the robot in place. Then, once the change in distance reading is greater than
the threshold, the robot can stop spinning and head towards the object.

In the following example code, we use a change threshold of 30 cm.

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            changeThreshold = 30 # distance change in cm needed to trigger detection

            # store initial value for current distance
            currentDistance = rangefinder.distance()

            # start spinning in place until an object is detected
            drivetrain.set_speed(5, -5)

            while True: # doesn't actually repeat forever. loop will be broken if an object is detected
                
                # update previous and current distance
                previousDistance = currentDistance
                currentDistance = rangefinder.distance()

                # if sudden decrease in distance, then an object has been detected
                if previousDistance - currentDistance > changeThreshold:
                    break # break out of the while loop

                time.sleep(0.1)

            # stop spinning drive motors
            drivetrain.stop()


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

We're already quite familiar with turning until an edge is detected. Now, we'll need to detect *both* edges. However, it would be
quite unwieldy and error-prone to just copy the edge detection code, so let's make a function to generalize this. Note that the existing
code detects a sudden *decrease* in distance, but we want to handle sudden *increases* in distances too.

How can we support both behaviors in a single function? We can pass in a parameter to specify whether we want to detect an increase
or decrease in distance! We can call this parameter :code:`isIncrease` and pass in a boolean (true or false) value.

If :code:`increase` is :code:`True`, then we want to detect an increase in distance, which is when :code:`currentDistance - previousDistance > changeThreshold`.

If :code:`increase` is :code:`False`, then we want to detect a decrease in distance, which is when :code:`previousDistance - currentDistance > changeThreshold`.

For more flexibility, let's add a parameter for the change threshold.

Here's the function definition:

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            def turnUntilEdge(isIncrease, changeThreshold):

                # store initial value for current distance
                currentDistance = rangefinder.distance()

                # start spinning in place until an object is detected
                drivetrain.set_speed(5, -5)

                while True: # doesn't actually repeat forever. loop will be broken if an object is detected
                    
                    # update previous and current distance
                    previousDistance = currentDistance
                    currentDistance = rangefinder.distance()

                    if isIncrease and currentDistance - previousDistance > changeThreshold:
                        # if sudden increase in distance, then an object has been detected
                        break
                    elif not isIncrease and previousDistance - currentDistance > changeThreshold:
                        # if sudden decrease in distance, then an object has been detected
                        break

                    time.sleep(0.1)

                # stop spinning drive motors
                drivetrain.stop()


    .. tab-item:: Blockly

        .. image:: media/detectiondefinition.png
            :width: 900

Here's the equivalent function call to the turn and detection code in the previous section:

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            turnUntilEdge(False, 30)

    .. tab-item:: Blockly

        .. image:: media/detectioncall.png
            :width: 200

Now, it's time to write the full program to detect both edges and turn to the center.

Implementing Dual Edge Detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's walk through each step of the process in code.

First, the robot should spin in place until it detects the first edge, then stop. This is simply the function call we saw earlier.

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            turnUntilEdge(False, 30)

    .. tab-item:: Blockly

        .. image:: media/detectioncall.png
            :width: 200

Next, we want to record the robot's heading for this first edge, and store it to :code:`firstAngle`.

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            firstAngle = imu.get_yaw()

    .. tab-item:: Blockly

        .. image:: media/firstangle.png
            :width: 200

Then, the robot should spin in place again until it detects the second edge, which is when there is a sudden increase in distance.

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            turnUntilEdge(True, 30)

    .. tab-item:: Blockly

        .. image:: media/turntoedgetrue.png
            :width: 200

Once the robot has detected the second edge, it should record its heading and store it to :code:`secondAngle`. Now, need to figure
out how much the robot needs to backtrack to aim for the center of the object. We can do this by finding the difference between
the two angles, and dividing by two. This is half the angle between the two edges, and if the robot backtracks by this amount,
it will be facing the center of the object. Let's store this in a variable called :code:`angleToTurn`.

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            secondAngle = imu.get_yaw()
            angleToTurn = (firstAngle - secondAngle) / 2

    .. tab-item:: Blockly

        .. image:: media/angletoturn.png
            :width: 400

Finally, the robot can turn this much to face the center of the object, and head towards it.

Here's the full code. Note that half-second pauses are added to make the robot's actions more visible:

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            # turn to first edge
            turnUntilEdge(False, 30)

            # store angle at first edge
            firstAngle = imu.get_yaw()

            time.sleep(0.5)

            # turn to second edge
            turnUntilEdge(True, 30)

            # store angle at second edge and calculate angle to turn
            secondAngle = imu.get_yaw()
            angleToTurn = (firstAngle - secondAngle) / 2

            time.sleep(0.5)

            # turn to center of object
            drivetrain.turn(angleToTurn)

    .. tab-item:: Blockly

        .. image:: media/fulldualedge.png
            :width: 400