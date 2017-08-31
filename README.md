# TauNet
Copyright (c) 2015 Jason Ritz
Licensed under: The MIT License (MIT)
Encrypted peer to peer Raspberry Pi texting

Writen for and tested on a Raspeberry Pi 2B. Sould work on any computer with Python 2.7 or later, but is tested and intended for the RP2B.

This is a class project for my cs300 Fall 2015 class at PSU

The program will allow users to text from one raspeberry Pi to another securly. It is written in Python and uses sockets (tcp/ip) to transfer RC4 encrypted strings back and forth using a private key and a custome protocal. 

# Build and Execution Instructions:

TauNet requires two terminal windows to opperate. The first terminal will display incoming messages
while the user can send messages from the second terminal. 

1. In a terminal run TauNet_Server.py by typing "python TauNet_Server.py"
	All Incoming messages will be displayed in this terminal. 

2. In a new terminal run TauNet_Client.py by typing "python TauNet_Client.py"
	The user can type and send messages to other TauNet users from this terminal

3. Sending the message 'q' to the user 'home' will exit the program in both terminals 
