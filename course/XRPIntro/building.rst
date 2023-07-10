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

The XRP kit (1:22)
==================

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

**Ultrasonic rangefinder**
    .. image:: media/Assembly/ultrasonic.jpeg
        :width: 200
        :alt: Ultrasonic rangefinder

The ultrasonic wire has two power wires labeled Vcc (red wire) and Gnd (black wire). It also has two
additional connections that operate the sensor and get range data. These are trig (blue wire) and
echo (yellow wire). A common mistake when wiring this sensor is to get these two wired incorrectly.

**Rangefinder bracket**
    .. image:: media/Assembly/rangefinder_bracket.jpeg
        :width: 200
        :alt: Ultrasonic sensor bracket


**Reflectance sensor**
    .. image:: media/Assembly/reflectance_sensor.jpeg
        :width: 200
        :alt: Reflelctance sensor for following or finding lines the robot drives over

**Reflectance sensor bracket**
    .. image:: media/Assembly/reflectance_bracket.jpeg
        :width: 200
        :alt: Reflectance sensor bracket


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

**Servo arm**
    .. image:: media/Assembly/servo_arm.jpeg
        :width: 300
        :alt: Servo arm for lifting objects

**Servo bracket**
    .. image:: media/Assembly/servo_bracket.jpeg
        :width: 200
        :alt: Servo bracket for mounting servo on back of robot

The servo is a special type of motor such that when programmed with a position
the shaft will automatically move to the specified angle. This is used to power the arm
on your robot it can move to predetermined angles all by itself.

**Casters**
    .. image:: media/Assembly/casters.jpeg
        :width: 200
        :alt: Nylon balls to use as front wheel casters

The casters simply provide a low friction contact point for the front of the robot to 
allow the two rear drive wheels to easily steer the robot forwards, backwards, or any angle.

Assembling the XRP Robot
========================

Assembling the XRP robot can be done without the use of tools with the optional exception of screwing
the servo arm to the servo. The total process should take about 15 minutes, especially once you
understand how it goes together.

Each of the following sections has a time reference for the video at the top of this page so you
can see how to assemble that part. We suggest that you view the entire video before starting the
assembly so you can get a good overview of how it goes together.

Inserting the casters into the chassis (2:07)
---------------------------------------------

    .. image:: media/Assembly/installing_casters.jpeg
        :width: 300
        :alt: Nylon casters inserted into the chassis

Install the white front casters (balls) into the chassis by pushing them into place.
Once they are installed, the casters should rotate freely.

Inserting the robot controller into the chassis (2:13)
------------------------------------------------------

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
-----------------

Putting the tires onto the wheels (2:30)
----------------------------------------

The tires are rubber o-rings that slip into the groove on the outside rim of the wheel. Simply stretch
the o-ring to get it to move into place. These will provide friction when the robot is driving,
especially on smooth surfaces.

Putting the wheels onto the motors (2:47)
-----------------------------------------

The wheels press fit onto the white motor shafts. Notice that the motor shafts have two flat sides
that correspond to the flat edges in the center of the wheel. The wheel is pressed over the
motor shaft so that the center part of the wheel that sticks out is closest to the motor body and
that the wheel is pressed all the way onto the motor shaft.

Connecting the motor cables to the motors (3:02)
------------------------------------------------

The motor cables connect the motor to the robot controller so that it can drive the drive the motors
and receive data from the motor encoder sensors that provide position and speed information for
your robot program. This encoders all the robot to drive at a desired speed and drive for a desired
distance.

The wider connector on the cable is inserted into the motor. Notice that pins (wires) on the motor
connector are closer to one side than the other. Similarly, the holes on the connector attached to the
cable are closer to one side. 

Installing the motors into the chassis (3:17)
---------------------------------------------

The motors snap into the chassis from the bottom once the wheels and cables are installed. The motor
is oriented so that the wheel goes through the slot on the chassis as shown in the picture.
Ideally you should push the wires from the motor through the opening in the chassis to the top of the
chassis so they can be attached to the robot controller. Then seat the end of the motor opposite the
cable first, then snap the wheel side of the motor into place. Repeat for both motors.



Connecting the motor cables to the robot controller (3:50)
----------------------------------------------------------

The motor cables are connected to the white connectors on the side of the chassis labeled Motor L and Motor R
for the left and right motor cables.

Installing the battery pack (3:59)
----------------------------------


Adding the battery cover (4:15)
-------------------------------

The battery cover is very easy to install, just line up the two tabs on the battery cover with the two
slots in the chassis just outside of the battery case. Then the clip snaps into place as you push the
battery cover into place.

Adding the Line Following Sensor
--------------------------------
The line following sensor can detect lines on the driving surface that have a different reflectivity.
These are typically used in robot applications to follow lines or locating interesting places on a
board or mat. It has two pairs of LEDs and photo sensors to emit infrared light and measure the
reflected brightness.

Connecting the cable to the line follower (4:32)
------------------------------------------------

Inserting the line follower into the bracket (5:04)
---------------------------------------------------

Attaching the line follower to the chassis (5:17)
-------------------------------------------------

Adding the ultrasonic rangefinder
---------------------------------
The ultrasonic rangefinder uses sound to measure the distance to objects in front of the sensor.
An ultrasonic (inaudible high frequency) short sound is sent from one of the transducers which
is reflected back by nearby objects and received by the second transducer. The time of the
sound round-trip is measured to determine distance to nearby objects.

Attaching the bracket to the chassis (5:27)
-------------------------------------------

Wiring the rangefinder (5:39)
-----------------------------

Attaching the rangefinder to the bracket (6:06)
-----------------------------------------------



Connecting the cables for the line follower and rangefinder (6:14)
------------------------------------------------------------------

Attaching the servo
-------------------
The servo is used to rotate the arm to the desired position. It has the advantage
over a normal motor in that it has sensors inside of it to allow it to move to
a desired position that you can program.

Inserting the servo horn into the robot arm (6:37)
--------------------------------------------------

Mounting the arm to the servo (6:58)
------------------------------------

Mounting the servo to the servo bracket (7:19)
----------------------------------------------

Attaching the servo and bracket to the robot chassis (7:29)
-----------------------------------------------------------

Connecting the servo cable to the robot controller (7:53)
---------------------------------------------------------