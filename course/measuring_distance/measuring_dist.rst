Measuring Distances
============================

Animal Echolocation
~~~~~~~~~~~~~~~~~~~~~~~

To understand why we would want to be able to measure distances, let's look at how animals use distance measuring to navigate their environment.

One example of this are bats which emit ultrasonic waves and listen to the echo to determine the distance of objects. This is called echolocation. Bats use echolocation to navigate through dark caves and find food where animals like bats emit high-frequency sound waves using their mouths. They listen to the echo of the sound waves bouncing back from the environment with their highly sensitive ears, allowing them to determine the size, shape, and texture of objects.

Similar to bats, whales also use echolocation to navigate underwater and locate food. They emit high-frequency clicking sounds using their nasal passages.

.. image:: media/batEcholocation.jpg
  :width: 200
  :alt: Alternative text



Robotic Echolocation
~~~~~~~~~~~~~~~~~~~~~

Just like bats and other animals, robots have evolved to have their own distance sensors which can give the robot more information about where it is relative to its environment. This allows the robot to make more informed decisions about how to navigate its environment.

So, what are some sensors that allow you to measure distances?

Reflective sensors
------------------

Lidar (Light Detection and Ranging), Sonar (Sound navigation and ranging), and Radar (Radio Detection and Ranging) all follow the same principle. These sensors all have one transmitter that "sends" a signal and a receiver that "listens" for the signal that was sent out. 

One common example is an ultrasonic range finder, which emits sound waves and listens for the echo. The sensor then calculates the distance based on the time it takes for the sound wave to bounce back.

Mechanical Sensors
------------------

Another type of sensor that can indirectly inform the robot about distance are mechanical sensors like limit switches. These sensors operate by physically touching an object and can be used to detect when a robot has reached a certain point in its environment.

The way that these sensors work is that they have a small metal piece that is pushed in when the switch is pressed. This completes a circuit and allows the robot to know that the switch has been pressed. 

Using the Ultrasonic Sensor
---------------------------

.. image:: media/setpointtarget.png

While using the XRP, your main distance sensor will be an ultrasonic range finder. Here is the method call to get the distance from the sensor:

.. code-block:: python

    sonar.get_distance()
    
This function returns the distance, in cm, from the sensor to the nearest object.


Mini Challenge: Show distance
-----------------------------
Try writing code that checks the distance every 50 ms (0.05 seconds) and prints the output.
