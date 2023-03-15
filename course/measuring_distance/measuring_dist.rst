Measuring Distances
============================

Real-world examples of distance sensing in robot systems
------------------------------------------------------------

In the programs you have written so far, the robot has been able to drive measured distances based on the circumference of the wheels and the number of rotations. This works as long as the objects the robot is driving toward are always precisely the same distance away. But what happens if the robot is trying to manipulate an object that might be different distances from run to run? If the robot could see the object, then it would always be able to drive to the object and stop and a repeatable distance from it. For example, if the task of the robot is to pick up a box with its arm that extends.

Welcome to the distance measuring module! The ability to measure the distance between a robot and the objects in its surrounding environment is crucial. This information allows the robot to avoid collisions and determine its current location with respect to the target.

Applications
-------------------

Autonomous Vehicles
~~~~~~~~~~~~~~~~~~~~~

Distance measuring is a fundamental feature of Tesla's Autopilot software for self-driving cars. Autonomous driving is a complex task and requires an incredible amount of information on its surrounding obstacles to avoid a collision. Measuring the forward distance to an obstacle allows the vehicle to maintain a healthy distance. Measuring sideway distance determines whether it is safe to merge highway lanes. While parking, measuring backward distance informs whether it is safe to continue backing up.

Tesla uses radars, a system using radio waves, for long-range sensing. A device, known as a transmitter, produces electromagnetic radio waves, which reflect back after hitting an object. Another device, known as a receiver, captures this reflected wave to calculate the distance of the object based on the wave's travel time and speed.

.. image:: media/tesla.jpeg
  :width: 200
  :alt: Alternative text

Marine Echolocation
~~~~~~~~~~~~~~~~~~~~~~~

Measuring distances isn't only important on land; it is important 20,000 leagues under the sea as well! Submarines use sonar, a system using sound, to navigate in the murky waters, measure distances from nearby objects, and detect notable presences in their surrounding environment, such as sunken ships.

Similar to radars, sonar detects objects by transmitting ultrasonic waves and captures the reflected echoes. Based on the travel speed and time of the wave, the distance to the object can be calculated.

.. image:: media/marine.png
  :width: 200
  :alt: Alternative text

Animal Echolocation
~~~~~~~~~~~~~~~~~~~~~~~~

While the integration of these distance-measuring sensors into technology is impressive, animals do it better!

Bats navigate through dark caves and find food through echolocation by emitting high-frequency sound waves using their mouths. They listen to the echo of the sound waves bouncing back from the environment with their highly sensitive ears, allowing them to determine the size, shape, and texture of objects.

Similar to bats, whales also use echolocation to navigate underwater and locate food. They emit high-frequency clicking sounds using their nasal passages.



