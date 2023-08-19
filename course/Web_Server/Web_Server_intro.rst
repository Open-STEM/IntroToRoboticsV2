Using the XRP Web Server
========================

Introduction:
-------------

In this section, you will learn about web servers and how to use them to wirelessly communicate with the XRP! A web server is a computer program that takes instructions from another computer over the internet. 
They are used to display web pages, run video games, send messages, and do almost anything else you can do on the internet.
Using the XRP's built-in web server, you can wirelessly display values on your computer and even send instructions to the XRP with 
just the press of a button. With this functionality you can easily debug programs and even use your phone or computer to remotely control your XRP.

writing programs that use the wen server is simple. 
If you are using python, the beginning of your program must include these two lines of code. If you are using blockly, this will be done for you.

.. code-block:: python

    from XRPLib.webserver import Webserver

.. code-block:: python

    webserver = Webserver.get_default_webserver()

Next, you can add buttons and text output. This is covered in the later sections, so this is a good time to read about those and return to this page when you have your inputs and outputs written.

Once you have the code for your buttons and text output, end the program with 

.. code-block:: python

    webserver.start_network(ssid="xrp", password="password")
    
.. code-block:: python
    
    webserver.start_server()

or if you are using blobkly:

.. image:: 
    media/start-server.png

Finally, search for wifi networks on your phone or computer, and join the wifi network with the 
name and password you chose, and open a new page on your browser. You should see your new custom dashboard!

.. note:: 
    Once you start the server, the xrp program will finish and the only way to control the robot will be 
    through the web server. Make sure that you start the server at the very end of your program.

Now you know how to start your web server. Next, you will learn how to use its full functionality. 
