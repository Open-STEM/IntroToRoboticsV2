IntroToRobotics - Style Guide
=================================
Introduction to Robotics Curriculum

A list of rules to follow while documenting a .rst file:

Headings
------------

* **Main Heading** - usually the title of the module, underline the main title using '=' operator. Make sure the number of '=' sign is more than the number of characters of the title. For example:: 
  
     Main Heading
     ==============

* **Sub Heading** - underline the sub title using '-' operator. Make sure the number of '-' sign is more than the number of characters of the sub title. For example:: 
  
     Sub Heading
     -------------

* **Sub sub Heading** - underline the sub sub title using '~' operator. Make sure the number of '~' sign is more than the number of characters of the sub sub title. For example:: 
  
     Sub Sub Heading
     ~~~~~~~~~~~~~~~~~


An example of the above headings can be seen in this image below:

.. image:: headings.jpg
  :width: 800
  
The code for the above image::

      Main Heading
      ==============

      Sample Text 1

      Sub Heading
      -------------

      Sample Text 2

      Sub Sub Heading
      ~~~~~~~~~~~~~~~~~

      Sample Text 3

Inserting images
------------------------

An image is inserted by using the following code::

     .. image:: media/image1.jpg
        :width: 100

This command will attach the image titled 'image1' with the '.jpg' extension and width 100, located in the folder titled 'media' relative to the current directory.

Documenting code snippets
---------------------------

``.. code-block:: programming_language`` is used to write a piece of code in your documentation. For example, including the following lines in your .rst file::

      .. code-block:: python
      
      if sonarDistance > targetDistance:

            set a positive effort (move forwards)

      if sonarDistance < targetDistance:

            set a negative effort (move backwards)

would get you the following output:

  .. code-block:: python
      
      if sonarDistance > targetDistance:

            set a positive effort (move forwards)

      if sonarDistance < targetDistance:

            set a negative effort (move backwards)



Highlighting text
---------------------------
* use ``single asterisk``: (``*text*``) for making the text *italics*.
* use ``double asterisks``: (``**text**``) for making the text **bold**.
* use ``double backquotes``: (````text````) for ``highlighting`` the text. Highlight all filenames that have been mentioned as plain text in this documentation. For example: "Let us refer to the code in ``motors.py``." Here, in this plain text, the general rule is to highlight the filename.



Inserting tables
---------------------------

Use::

      .. list-table:: Title
         :widths: 25 25 50
         :header-rows: 1

         * - Heading row 1, column 1
           - Heading row 1, column 2
           - Heading row 1, column 3
         * - Row 1, column 1
           -
           - Row 1, column 3
         * - Row 2, column 1
           - Row 2, column 2
           - Row 2, column 3

This would output the following table:

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Heading row 1, column 1
     - Heading row 1, column 2
     - Heading row 1, column 3
   * - Row 1, column 1
     -
     - Row 1, column 3
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3
     
     
Math Equations
--------------------
Use::

      .. math::

         (a + b)^2 = a^2 + 2ab + b^2

         \pi * x = \frac{5}{17}

This would output the following equation:

.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   \pi * x = \frac { 5 } { 17 }     # the fraction looks perfect in Readthedocs, there is some issue with viewing it in Github. 
      



Styleguide
----------

Refer to the folders and files as Modules and Pages

Get rid of the “indices and tables” section

How do we introduce “challenge activities”? Other activities? Is there a difference?

How do we ask questions? What are the different types of questions?  

Add captions to important images 

Put in links whenever other pages are linked. Open a new tab for a link

Formatting lists -- 
  numbered if they’re steps, bulleted otherwise
  Always have the topic of the list or description of the list directly beforehand. Add colons.
  No spaces between different list points or heading of the list and first list point
  Indent sub-lists
  If a numbered sub-list is below a numbered list, use letters

Use \`\` \`\` to deal with embedded code.

Use a sphinx “note” to refer to things about the course?

Use a sphinx “reminder” to refer to things about the course?

Add boxes in images when a part needs to be highlighted

Add blocks for “Python Programming”. Find an appropriate name for python programming notes

Bold important words
