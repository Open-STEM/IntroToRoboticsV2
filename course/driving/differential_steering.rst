Advanced: Circles and Differential Steering
===========================================

In this section, we derive the math needed to drive in circles of any radius.
Fundamentally, this requires driving the two motors at different ratio, but it
takes a little calculation to figure out this ratio for a given radius.

.. youtube:: kd2-mhI2CgE

The robot goes in an arc. The wheels draw out 2 different circles with 2
different radii. The arc with the smaller radius (:math:`r_1`, the white line)
has a smaller circumference. That means the left wheel has driven a smaller
distance. It has gone slower.

How would you drive in an arc with a given radius?
--------------------------------------------------
We know the wheels trace out arcs when we make the wheels go at different
speeds, but how do we decide what the wheel speeds should be?

What do we know?
----------------

Let us start with what we know about the two arcs, and the arc we want the
center of the robot to go through. 

  
The first thing we can say about any circle is that the radius is proportional
to the circumference. This means that the inner and outer arc lengths are
proportional to the inner and outer radii, or 

.. math:: 
    
    \frac{\text{left wheel distance}}{\text{right wheel distance}} = \frac{r_1}{r_2}

This means that the *ratio* between the wheel speeds is equal to
:math:`\frac{r_1}{r_2}`.

Hey! We found out what the ratio between the wheel speeds is supposed to be if
we know the two radii. But how do we find what the two radii are? We only know
what we want the radius of the orange circle to be.

But we know what the distance between the two wheels are. 

.. image:: media/Screenshot2023-03-07142430.png

If :math:`r_{bot}` is the distance between the two wheels, then

.. math:: 
    
    r_1 = r_{desired} - \frac{r_{bot}}{2} 

since r1 is less than the desired radius, and

.. math:: 
    
    r_2 = r_{desired} + \frac{r_{bot}}{2}
 
We found out the radii of the circles we want the left and right wheels to
trace, and we know how to find the ratio between the wheel speeds from that. 

Remember:  

.. math:: 
  
    \text{ratio between wheel speeds} = \frac{r_1}{r_2}


Putting them together, we get,

.. math:: 
    
    \text{ratio between wheel speeds} = \frac{r_{desired} - \frac{r_{bot}}{2}}{r_{desired} + \frac{r_{bot}}{2}}

.. admonition:: Try it out

    Write code to make the robot drive in a circle. Use the :code:`set_speed`
    function, and use a speed of 5 cm per second for the left wheel speed. 
    Use the ratio you calculated to find out what the right wheel speed should 
    be (multiply 5 by the ratio)

    Now try using 5 for the right wheel speed, and use the ratio for the left 
    wheel. What happened?

Additional challenges 
---------------------

Try to make the robot do a point turn! What is the radius of the circle that you
want it to drive in then? 

Try and make the robot turn around one of the wheels. What is the new desired
radius?

Try making the robot drive backwards in an arc

 