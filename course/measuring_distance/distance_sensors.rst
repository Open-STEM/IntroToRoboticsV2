Distance Sensors
================
Distance Measuring Sensors
--------------------------

So, what are some sensors that allow you to measure distances?

Mechanical Sensors
------------------

If you touch it, then you know it's there. Mechanical sensors detect some form of mechanical deformation (bend, press, etc) and translate that into an electrical signal. This is a very naive, but still valid way to approach distance measurement. The obstructing object could activate a mechanical switch upon contact, signaling its presence. 

An example of a mechanical sensor is a Whisker Sensor. The whisker itself is a long flexible piece of metal that can bend and trigger a mechanical witch to notify the obstacle ahead. Whisker sensors can consist of multiple whiskers to sense obstacles from multiple directions.

Reflective sensors
------------------

Lidar (Light Detection and Ranging), Sonar (Sound navigation and ranging), and Radar (Radio Detection and Ranging) all follow the same principle. A transmitter emits light, sound, or radio waves, which bounce back from an obstructing object, resulting in echoes. A receiver captures these echoes, allowing for the calculation of distance based on the travel time of the wave.

Using the Ultrasonic Sensor
---------------------------

.. image:: media/setpointtarget.png

We will be using an Ultrasonic Sensor which is one type of Reflective Sensor that uses Sonar to measure and calculate the distance. We have just one function for getting input from the ultrasonic sensor.

.. code-block::python
    sonar.get_distance()
    
This function returns the distance, in cm, from the sensor to the nearest object.

 

Mini Challenge: Show distance
-----------------------------
Try writing code that checks the distance every 50 ms (0.05 seconds) and prints the output.