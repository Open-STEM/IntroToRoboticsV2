Introduction to Proportional Control
====================================

What is Proportional Control?
-----------------------------

Imagine you're driving a car and you want to keep at a steady speed. If you're going too slow,
you press the accelerator a bit, and if you're going too fast, you ease off. But instead of
just fully pressing or fully releasing the accelerator (like an on-off switch), you adjust
how hard you press based on how far off you are from your desired speed. That's the basic idea
behind proportional control. The further you are from your target, the harder you try to correct it.
If you're a little off, you make a small adjustment. If you're way off, you make a big one.

Let's take this analogy further - you decide that the perfect cruising speed for your car ride is 70 mph.
This speed represents your desired value or where you ideally want to be. In control theory, this is 
called the **setpoint**.

You get on the highway, and as you settle into your drive, you glance at your speedometer. It reads 65 mph,
which is your current value. In control theory, this is called the **process variable**.

Naturally, you recognize there's a difference between where you want to be (70 mph) and where you currently are
(65 mph). This difference is the called the **error**, and in this case, it's 5 mph. It's easily calculated by
the formula:

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            error = setpoint - process_variable
    
    .. tab-item:: Blockly

        .. image:: media/set_error.png
            :width: 300

Knowing the error isn't enough. How should you, the driver, react to it? This is where the concept of Proportional
control comes into play.

Think of P control as your driving instinct. Instead of abruptly flooring the accelerator or immediately slamming the
brakes, you adjust your speed based on your error: how far you are from your desired speed.

A measure called **control output** tells you much to adjust. It's calculated as:

.. tab-set::

    .. tab-item:: Python

        .. code-block:: python

            control_output = Kp * error

    .. tab-item:: Blockly

        .. image:: media/control_output.png
            :width: 300

where Kp is a constant called the **proportional gain** and acts as a scaling factor for the error.

If Kp is high, it's like you have a heavy foot and you'll accelerate hard even for a small error. You'll get there faster, but
less precisely and you're more likely to overshoot.

On the other hand, if Kp is low, you're more of a cautious driver, gently pressing the accelerator for the same error. You'll
get there more slowly, but at a much smoother pace.

Having the constant Kp allows you to tune your control system to your liking.

Note that this analogy breaks down somewhat. Imagine your current speed is *greater* than your desired speed. In this case,
the error is negative. If you plug this into the control output formula, you'll get a negative control output. This means that
a proportional controller will actually slow you down if you're going too fast, proportional to how far you are from your desired
speed. So, you can imagine that a proportional controller is like a driver who's always trying to get to the speed limit, utilizing
both the accelerator and the brakes.

Tuning Kp
---------

The following graph shows proportional control in action.

.. image:: media/proportional.jpeg
    :width: 400

The blue line is the reference, and indicates the desired value. Red, green, and purple lines represent the current value over time
when controlled by a proportional controller with different values of Kp.

With a low Kp, the red line is slow to react to the error, and the controller is sluggish. It takes a long time to reach the desired
value, and it never quite gets there. This is called **underdamped** behavior.

With a high Kp, the purple line is quick to react to the error, and the controller is aggressive. It reaches the desired value quickly,
but overshoots, causing the error to become negative. It then corrects itself, but overshoots again, and so on. This is called **overdamped**
behavior, and results in oscillations around the desired value.

The green line is just right. It reaches the desired value quickly, and doesn't overshoot much. It's an important task to tune Kp so that
the controller approaches the desired value as quickly and smoothly as possible.

Note: You'll find that, even with excellent tuning, a proportional controller often will either oscillate a little bit, or never quite reach
the desired value. More advanced control systems like PID aim to minimize these issues, but they are out of the scope of this course.






