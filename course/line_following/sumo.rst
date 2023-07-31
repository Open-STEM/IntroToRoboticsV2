Challenge: Sumo-Bots!
=====================

.. image:: media/sumo.png

It's time for SUMO bots! Two XRP bots battle it out in the ring in a completely
autonomous match to push the other robot outside of the ring.

Robots start facing away from each other in the orientation above, and have one
minute to knock the other robot outside. They may utilize distance sensors to
detect the presence and location of the other robot, and use the reflectance
sensors to keep themselves inside the ring. 

.. hint:: 

    A basic SUMO-bots program may consist of a robot continuously point turning
    until an enemy robot is found with the distance sensor, and then charging at
    the robot until the black line is detected, so that the robot stays inside
    the ring. However, worthy extensions include: aligning the robot to be
    perpendicular from the black line so that the robot is not misaligned, and
    devising an algorithm to attack the opponent robot from the side to avoid a
    head-on collision and gain more leverage.