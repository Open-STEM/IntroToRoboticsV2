Introduction to Manipulation
=================

Now that we've covered different ways of controlling your robot's movement, let's cover how we can control the robot's arm to manipulate our environment. 

The XRP Arm
-----------------------------------

Every robot needs to be able to interact with it's environment. 

Your XRP does this with a simple 1 DOF arm.

In this case, "DOF" stands for "Degree of Freedom" and refers to the number of ways the arm can move. 

To move your XRP's arm, use this function;

[insert the function call that would move the arm ]

Other Robotics Manipulators
-----------------------------------

The XRP arm is a very simple manipulator.

Most robots have more complex manipulators, with more degrees of freedom.

For example, Boston Dynamic's Spot robot has a 5 DOF arm that can be used to open doors, turn valves, and even pick up objects.

For more complicated manipulators like the one that Spot has, roboticists often have to create control laws specific to those manipulators. 

In the case of Spot, the arm is equipped with a camera that halp Spot better understand it's environment and avoid obstacles while trying to use it's arm.