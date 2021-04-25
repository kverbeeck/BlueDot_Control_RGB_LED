# BlueDot_Control_RGB_LED

Description Assignments
1)	Find a minimum of 5 bluetooth devices and note their bluetooth address. Check if some of these devices use the same BT chip. (Tip: your raspberry pi and arduino nano 33 IoT also have BT)
2)	Use the Raspberry Pi to transmit and/or read data via a bluetooth connection
a)	You choose how complicated you make the project, be creative!
b)	Document your project.
c)	Tips:
i.	For example, you can control a relay with your cell phone that is bluetooth connected to the raspberry pi
ii.	You can read out a sensor with your arduino which then sends this data to the pi and stores it in a file.
iii.	...


The Project
This project will control an RGB LED connected to the GPIO pins of a Raspberry Pi. We will use Blue Dot running on the ANDROID client to control the RGB LED pre-configured colors and their brightness. Below is how it will look on both sides.

Having already installed BlueZ in the previous assignment, we can use this tool to secure a stable connection with our Android device and Blue Dot application.
https://bluedot.readthedocs.io/en/latest/gettingstarted.html
https://bluedot.readthedocs.io/en/latest/index.html

In order to use Blue Dot you will need:
•	A Raspberry Pi
o	with built-in Bluetooth (such as the Raspberry Pi 3, 4 or Zero W)
o	or a USB Bluetooth dongle
•	An Android device or 2nd Raspberry Pi for the remote
•	An Internet connection (for the install)

For this assignment, we will an Android device as the client to control 
