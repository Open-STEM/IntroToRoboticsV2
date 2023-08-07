Driving With Geometry
=====================

The XRP's driving and turning functions can also be used to draw geometric patterns!
By driving a set distance and turning by a certain angle several times, you can draw a 
shape with as many sides as you want.

.. tip:: 

    To see the path your XRP has driven, you can place a dry-erase marker between the
    robot's wheels and trace your pattern on a whiteboard.


To draw a shape of any side length, you just need to know the size of the shape's exterior angles,
and you need to decide how long the sides should be. Then, you just have to drive straight with the distance
of the side length, turn by the interior angle of the shape.

.. image:: media/exterior-angle.png

triangle
--------

For a triangle, the interior angle will be 60, so the exterior angle will be 120. If we use a side length
of 30, then we can just drive forward and turn 3 times. 

.. tab-set::
    .. tab-item:: Python
        .. code-block:: python
            differentialDrive.straight(30, 0.5)
            differentialDrive.turn(120, 0.5)
            differentialDrive.straight(30, 0.5)
            differentialDrive.turn(120, 0.5)
            differentialDrive.straight(30, 0.5)

    .. tab-item:: Blockly
        .. image:: media/triangle-blockly.png
            :width: 300


square
------

A square will be similar to a triangle. The interior angle is 90 degrees so
the exterior angle is also 90 degrees. We can keep using a 30cm side length, 
so we just have to turn 90 degrees and drive straight by 30cm 4 times.

.. tab-set::
    .. tab-item:: Python
        .. code-block:: python
            differentialDrive.straight(30, 0.5)
            differentialDrive.turn(90, 0.5)
            differentialDrive.straight(30, 0.5)
            differentialDrive.turn(90, 0.5)
            differentialDrive.straight(30, 0.5)
            differentialDrive.turn(90, 0.5)
            differentialDrive.straight(30, 0.5)

    .. tab-item:: Blockly
        .. image:: media/square-blockly.png
            :width: 300

polygons
--------

You can use the same procedure used to make a triangle and square to make any polygon. You just have to
determine the exterior angle and choose a side length. However, this starts to get very tedious. 
We repeat the same code several times, so instead we can use a function to simplify the process. 

First, lets determine what information the function needs. To trace a polygon, you need the number of sides 
and the length of each side. We can create a function that takes these two values as an input. 
The function will drive the distance we gave it, turn by the exterior angle, and then repeat that process
as many times as there are sides in the shape. We can use a loop for this. The one problem is:
how do we know what the exterior angle is? Fortunately, this can be easily calculated with this equation:

.. math:: 
    360/n

With this information, you can write a function to draw a polygon of any size!

.. tab-set::
    .. tab-item:: Python
        .. code-block:: python
            def polygon(sideLength, numSides):
                for i in range(int(numSides)):
                    differentialDrive.turn((360 / numSides), 0.5)
                    differentialDrive.straight(sideLength, 0.5)

    .. tab-item:: Blockly
        .. image:: media/polygon-blockly.png
            :width: 300

Pinwheel
--------

Now we know how to easily draw any polygon, but we can take it one step further and draw a polygon pinwheel.
This pattern consists of several polygons entending out from a center point, and the XRP can easily draw it
by drawing several polygons consecutively and turning between every new polygon. A pinwheel of 3 squares should look 
something like this:

.. image:: media/pinwheel-square.jpg

Programming this may seem like a daunting task, but it is actually simple. Every time you want to make a part
of the pinwheel, you just need to call your polygon function from before and turn. Repeat this as many times
as there are polygons in the pinwheel, and your pattern will be finished!

.. tab-set::
    .. tab-item:: Python
        .. code-block:: python
            def pinwheel(sideLength, numSides, instances):
                for i in range(int(instances)):
                    polygon(numSides, numSides)
                    differentialDrive.turn((360 / instances), 0.5)

    .. tab-item:: Blockly
        .. image:: media/pinwheel-blockly.png
            :width: 300