# R3-SoftwareTask2-VasuPatel


This project is about creating a server and a client. The client is used to send information about rover speed and direction and the server receives and interprets the information and prints the current speed of the rover and the status of each motor based on the direction sent by the client.


The client key input is taken though pynput and a keycode is extracted based on key pressed. For this project the only useful keys are w,a,s,d,1,2,3,4,5,esc and k. The keys w(87), a(65), s(83), d(68) is used to drive the rover with w being forward, a being left, s being reverse and d is for right. Windows has default int number for each key and its used to analyze which key is pressed. In *on_press* the pressed keys value is extracted and send to *check*. *check* function is used to analyze if one of the required key is pressed or not. If the required key is pressed then the key is logged into a txt file and the information is sent to the server as bits to be interpreted. If *k* is pressed then the connection between server and client is disconnected and *esc* calls *on_release* and stops listening  to user key press.

The server is used as a rover, where it waits for valid user input and prints out the speed and direction in which rover would travel in. The message is converted from bits to int number and used to perform the task, if *k (75)* is received then the connection is closed. if number between 1-5 (49-53) is pressed *roverOutput* function is called, its used to set the speed of the rover and it is mapped between 0 to 255, and the direction of the rover using the function *direction*. The keys w,a,s,d is used for direction, the *direction* method is used for the output, to display in which direction and speed each motor would spin. The picture show when the server is activated.

![Screenshot (194)](https://user-images.githubusercontent.com/83378929/138540066-087bf31f-8544-41ca-973f-ac57023c2c95.png)

The picture below show when the client is connected

![Screenshot (195)](https://user-images.githubusercontent.com/83378929/138540303-8b667d45-c1c2-41c5-a2af-108062409f4a.png)


The picture below show when the *3* is pressed to set the speed and the direction is forward (w). All four motors are spinning forward at speed 153.

![Screenshot (196)](https://user-images.githubusercontent.com/83378929/138540306-b1d5270b-d203-48d9-98ca-7f1626d2c7f4.png)    
  

The picture below show when the *5* is pressed to set the speed and the direction is forward (w / 87), all four motors are spinning forward at speed 255. When the direction is reverse (s / 83), all 4 motors are spinning back. When the direction is right (d / 68), left motors are spinning forward and right motors and spinning back to turn right. When the direction is left (a / 65), left motors are spinning back and right motors and spinning forward to turn left. The IP and Port, show the message received from the client.

![Screenshot (197)](https://user-images.githubusercontent.com/83378929/138540308-cbc827b6-9fd6-4abc-bc2a-394c1058005d.png)

