Controlling Behavior: Continuous Controllers
==========================================

Introduction:
-------------------

While the bang-bang controller works, there are issues that can be solved using another type of controller.

The bang-bang controller is a **discrete** controller. This means that the control input is either "on" or "off".

A **continuous** controller is one that can have any value. For example, the speed of a car is a continuous controller. It can be 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, etc. It can be any number. It is not limited to "on" or "off".

Continuous controllers are more difficult to implement, but they can be more effective and offer the user more control over their system. Let's try to implement one.

Let's go back to our Control Law.

.. list-table:: 
   :widths: 50 50
   :header-rows: 1

   * - Sensor Input
     - Action

   * - You're a lot closer than **20 cm away**
     - Move Back
     	
   * - You're a little closer than **20 cm away**
     - Move Back
     
   * - You're **20 cm away**
     - No Need to Move
     
   * - You're a little farther than **20 cm away**	
     - Move Forward
     
   * - You're a lot farther than **20 cm away**
     - Move Forward

Here, there are some obvious changes that we can make. For example, if we are very far away, it doesn't make sense to be moving at the same speed as if we were a little bit away. We should be moving faster.

This concept of "how far off" our robot is from the target is called the **error**. The error is the difference between the target and the current position. Many optimal control laws use the error to determine how the robot should react. 

Let's try to visualize this with this new table:

.. list-table:: 
   :widths: 50 50
   :header-rows: 1

   * - Sensor Input
     - Action, (go forwards or backwards? Fast or slow?)

   * - You're a lot closer than **20 cm away**
   	(far away from the target)
     -
     	
   * - You're a little closer than **20 cm away**
   	(close to the target)
     - 
     
   * - You're **20 cm away**
   	(at the target)
     - 
     
   * - You're a little farther than **20 cm away**
   	(close to the target)
     - 
     
   * - You're a lot farther than **20 cm away**
	(far from the target)
     -   

Now that we have a better idea of a better control law, let's try to realize it with a proportional controller. 

Proportional Control 
--------------------

A proportional controller is one multiplies the error by a constant **kp** to produce a control effort. 

That means that if the error is large (you have to go a far distance), so is the control effort. If the error is negative (you have to go backwards), the control effort is in the other direction.

*Remember -- the error is the distance between the point you are at, and the point you want to go to.*

Now, please note that there is no "exact" way to find kp. This is an aribtrary constant that you will have to tune to match the needs of your robot. 

That being said, thinking about how it is used in your program can help you find a kp value that works for you. For example, if you want to change the speed of your robot, then having a kp value of ~1000 is way too big and a value of ~0.001 is way too small.

Like this, there are many logical steps that you can take which will help you find your kp value faster than trial and error.

Other Continuous Controllers
----------------------------------

You may have heard of a PID controller. This is a controller that uses the error, the integral of the error, and the derivative of the error to determine the control effort.

In a PID controller, the "P" stands for proportional, the "I" stands for integral, and the "D" stands for derivative.

The integral and derivative are more advanced concepts that we will breifly touch on in this course. For now, all you need to know is that an integral is the sum of all the errors, and a derivative is the rate of change of the error.

Therefore, for more complicated systems (like an autonomous car or bipedal robot), they can be very useful. However, for our relatively simple system, a proportional controller is more than enough.
