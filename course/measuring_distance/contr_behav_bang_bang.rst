Controlling Behavior: Bang Bang
===============================

Parking your XRP
----------------

You want to create a control law that parks your XRP at a set distance of 20 cm from a wall. You know that, in order to do that, you only need your distance sensor!

[insert image]

In order to build your control law, you build a table. For each of these scenarios, do you want to go forwards or backwards?

.. list-table:: Title
   :widths: 50 50
   :header-rows: 1

   * - Sensor Input
     - Action, (go forwards or backwards?)

   * - You're a lot closer than **20 cm away**
     -
     	
   * - You're a little closer than **20 cm away**
     - 
     
   * - You're **20 cm away**
     - 
     
   * - You're a little farther than **20 cm away**	
     - 
     
   * - You're a lot farther than **20 cm away**
     -   
     
Try implementing this table using if statements on your robot. How many if statements would you need? 

Design Thinking
---------------------

What are some problems you're running into?

	Does the robot stop?

	Does it move too fast?

	Does it move too slow?

Why are these problems happening, and how can they be solved? 

Hint: Do you need the robot to always move at full speed? When should the robot slow down?

Bang Bang control
-----------------

The Robot only needed to move forwards when it was too far, and backwards when it was too close. 

 
.. code-block::python
	if sonarDistance > targetDistance:

	 set a positive effort (move forwards)

	if sonarDistance < targetDistance:

	 set a negative effort (move backwards)

	if sonarDistance == targetDistance:

	 set the effort to 0

This is called **Bang Bang control**. What efforts did you choose? Did you set the efforts to 0.5 and -0.5? It's called "Bang Bang" because it's always either full throttle forwards, or full throttle backwards (Bang forwards, Bang backwards). When it's close to it's goal, does it need to be so fast? How can you change that?  
