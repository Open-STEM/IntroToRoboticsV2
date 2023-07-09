======================
Building the XRP robot
======================

Assembling the XRP robot is easy, but be sure to follow the steps here to be sure that
the wiring is correct and all the pieces are added correctly to the chassis.

Below is a video provided by SparkFun Electronics showing how to assemble the robot followed
by a step by step set of written instructions below.

.. youtube:: G7gfPi7XHuA

|
|

The XRP kit
===========

The XRP kit contains all the parts you need to assemble and use your robot.
You only need to supply 4 AA Batteries (preferably rechargeable) and a micro USB
cable to connect your computer to the robot. The contents of the kit are shown
to help you identify the parts during assembly.

**Robot chassis**
    .. image:: media/Assembly/chassis.jpeg
        :width: 200
        :alt: Robot Chassis that holds all the components

The chassis is a single-piece design that holds all of the robot components. It is designed
with a rail system that is designed to make adding additional components easy and without
the need for tools. All the robot parts simply snap onto the chassis to make assembly as
simple as possible. You can also 3D print your own parts to attach to the chassis.


**Robot controller**

    .. image:: media/Assembly/robot_controller.jpeg
        :width: 200
        :alt: Robot controller circuit board

The robot controller has the RP2040 microprocessor that reads the sensors inputs, runs
the Python or Blockly program and drives the actuators (motors). It also has additional
components to sense accelerations and headings of the robot, and communicate over WiFi
with your laptop or phone.

**Electronics parts**

    .. image:: media/Assembly/electronics_parts.jpeg
        :width: 200
        :alt: Electronics parts background

The components in the bag of elctronics parts will each be shown individually below.

**Motors and cables**

    .. image:: media/Assembly/motors_and_cables.jpeg
        :width: 200
        :alt: Robot drive motors and cablese

The motors are used to drive the robot and are attached to motor controller through
the associated cables.

**Battery case**

    .. image:: media/Assembly/battery_case.jpeg
        :width: 200
        :alt: Battery case for AA cells

The battery case holds 4 AA batteries. You can use any standard alkaline cells but
rechargeable cells are prefered so that you don't have to keep replacing them as
they run out of energy.

**Sensor cables**
    .. image:: media/Assembly/sensor_cables.jpeg
        :width: 200
        :alt: Cables for rangefinder and line follower sensors

These cables connect the rangefinder and line following sensors to the robot controller.
**When installing these on the sensor end, you must be careful to install the wires correctly,
so be sure to carefully read the instructions when attaching them.** Miswiring is the motors is the most
common cause of problems when assembling the XRP robot.

**Tires (o-rings)**
    .. image:: media/Assembly/tires.jpeg
        :width: 200
        :alt: O-rings to be used as tires over the wheels

These o-rings are used to form tires to slip over the plastic wheels to give the robot
more traction, especially on smooth surfaces.

**Servo motor**
    .. image:: media/Assembly/servo.jpeg
        :width: 200
        :alt: Servo motor for the robot arm

The servo is a special type of motor such that when programmed with a position
the shaft will automatically move to the specified angle. This is used to power the arm
on your robot it can move to predetermined angles all by itself.

**Casters**
    .. image:: media/Assembly/casters.jpeg
        :width: 200
        :alt: Nylon balls to use as front wheel casters

The casters simply provide a low friction contact point for the front of the robot to 
allow the two rear drive wheels to easily steer the robot forwards, backwards, or any angle.


Inserting the casters into the chassis
======================================

    .. image:: media/Assembly/installing_casters.jpeg
        :width: 300
        :alt: Nylon casters inserted into the chassis

Install the white front casters (balls) into the chassis by pushing them into place.
Once they are installed, the casters should rotate freely.

Inserting the robot controller into the chassis
===============================================

Insert the robot controller circuit board into the chassis as shown in the following picture.
Observe the orientation of the board where the battery connector (5) istowards the back of the
robot as shown. Also the top corners of the board are inserted part way into the corner
pockets as shown at (1) and (2). The clips in the chassis (3) and (4) are designed to hold the chassis
in place when it is pushed in.

    .. image:: media/Assembly/inserting_controller_1.jpeg
        :width: 300
        :alt: First step in installing the controller is to push in the top corners

Then push down and foward on the back edges of the board so that the front corners
are completely seated in the pocket as shown at (1) and (2) and the board snaps down as shown at (3) and (4)
in the following photograph. It might be helpful to view this part of the assembly in the video
from the top of this page.

    .. image:: media/Assembly/inserting_controller_2.jpeg
        :width: 300
        :alt: Second stem in stalling the controller by pushing it forwards and down into place

Adding the motors
=================

Putting the tires onto the wheels
---------------------------------

The tires are rubber o-rings that slip into the groove on the outside rim of the wheel. Simply stretch
the o-ring to get it to move into place. These will provide friction when the robot is driving,
especially on smooth surfaces.

Putting the wheels onto the motors
----------------------------------

The wheels press fit onto the white motor shafts. Notice that the motor shafts have two flat sides
that correspond to the flat edges in the center of the wheel. The wheel is pressed over the
motor shaft so that the center part of the wheel that sticks out is closest to the motor body and
that the wheel is pressed all the way onto the motor shaft.

Connecting the motor cables to the motors
-----------------------------------------

The motor cables connect the motor to the robot controller so that it can drive the drive the motors
and receive data from the motor encoder sensors that provide position and speed information for
your robot program. This encoders all the robot to drive at a desired speed and drive for a desired
distance.

The wider connector on the cable is inserted into the motor. Notice that pins (wires) on the motor
connector are closer to one side than the other. Similarly, the holes on the connector attached to the
cable are closer to one side. 

Installing the motors into the chassis
--------------------------------------

Connecting the motor cables to the robot controller
---------------------------------------------------

Installing the battery pack
===========================

Installing battery pack holder into the chassis
-----------------------------------------------

Adding the battery cover
------------------------

Adding the Line Following Sensor
================================

Connecting the cable to the line follower
-----------------------------------------

Inserting the line follower into the bracket
--------------------------------------------

Attaching the line follower to the chassis
------------------------------------------

Adding the ultrasonic rangefinder
=================================

Attaching the bracket to the chassis
------------------------------------

Wiring the rangefinder
----------------------

Attaching the rangefinder to the bracket
----------------------------------------

Connecting the cables for the line follower and rangefinder
-----------------------------------------------------------

Attaching the servo
===================

Inserting the servo horn into the robot arm
-------------------------------------------

Mounting the arm to the servo
-----------------------------

Mounting the servo to the servo bracket
---------------------------------------

Attaching the servo and bracket to the robot chassis
----------------------------------------------------

Connecting the servo cable to the robot controller
==================================================