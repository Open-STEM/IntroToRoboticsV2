Differential steering
================

In the last section, we learned how to set the motor efforts. But currently, you only know how to get the robot to go straight! Let's fix that:

Since there is no steering wheel like you would find on a car, the way to control the robot is by varying the wheel speeds relative to each other. This is called differential steering because the difference in wheel speeds controls the direction of the robot. As we go through each type of motion, give it a try on your robot to get a better grasp of what is happening!


Driving straight
-------------------------

As you saw in the previous section, when the left wheels and the right wheels are moving forward at the same speed, the robot will drive in a straight line. This is illustrated in the following image where the wheel speeds are shown by the length and direction of the arrows:

* Both arrows going forward means the wheels are turning in a direction that causes the robot to move forward and
* The length of the arrows being equal indicates the wheels are each going at the same speed.

[insert 1 image]

[insert 1 video]

Try setting the motor efforts to be equal to each other to confirm the robot drives straight.

.. note::
  The robot turning a tiny bit while trying to drive straight is normal. We'll address how to fix this in the next section.

Turning
-------------------------

When turning there are a variety of paths that the robot might follow, whether that be a gentle curving turn to a turn in place. All of these variations can be achieved by changing the difference between the motor efforts. Let's take a look as the main categories of turns:

Making a sweeping turn right or left
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the left wheel turns faster than the right wheel, the left side of the robot tries to get ahead of the right side, resulting in a right turn. Similarly, if the right wheel turns faster than the left, the robot turns to the left. Try setting your motor effort to two non-equal positive values, such as 0.5 and 0.8

[insert 1 image]

[insert 1 video]

As you just saw, two unequal motor powers causes the robot to move forwards in a sweeping arc. The radius of the turn depends on the difference between the motor powers: a larger difference between the wheel speeds results in a tighter and a smaller radius turn, while a smaller difference results in a wider turn and a larger radius. Try running a couple different combinations of motor speeds to get a feel for this relationship.

Making a swing turn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If one of the wheels is not moving at all while the other wheel is turning, then the robot will make a pivoting turn where the center of the rotation of the robot will be on the non-moving wheel. For example, if the right wheel is turning and the right wheel is fixed, then the robot will make a turn that pivots on the left (non-moving) wheel.

[insert 1 image]

[insert 1 video]

A swing turn rotating on the right wheel.

The robot's path is circular with the turning wheel (left side) forming the outside of the circle and the pivot wheel being the center. The radius of this circle will be the distance between the wheel centers. 

Point turn
~~~~~~~~~~~

Another type of turn is where the left and right wheels turn in at an equal speed but in opposite directions. With this turn, the center of rotation is a point approximately between the left and right wheels, causing the robot to turn in place.

[insert 1 image]

[insert 1 video]

Generally, point turns are considered the most useful of the turning types, as the center of the robot remains stationary during the turn and is the fastest of the turns.

.. note::
  The turning center of the robot is the center point between the two drive wheels. This is not necessarily the exact center of the robot, and for these robots is likely a bit farther back.

Mini-Challenge: Running in Circles
--------------------------------------

To exercise our new skills in controlling the robot's driving, let's try making a function that can drive in a circle of a specified radius.

Python Programming Note:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To give your new function some context, like the radius you want the robot to drive, you just include that value inside of the parenthesis. Also note that the turn_radius function comes before main. This is important since Python can not call a function before it is defined.

def turn_radius(radius):
    print(f"turning on a radius of {radius}")

def main()
    turn_radius(10)

We are going to need to use a sweeping turn, as we saw earlier. The ratio between the wheel speeds is what specifies the radius of the turning, as is specified in this formula:


[insert 1 image]

, where the trackWidth is the distance between the two wheels. The output of this formula is a ratio, which can be used to get the wheel speeds by setting the outside wheel to motor effort 1 and having the inner wheel be set to 1/MotorEffortRatio
