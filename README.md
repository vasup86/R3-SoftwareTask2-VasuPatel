# R3-SoftwareTask2-VasuPatel


This project is about creating a server and a client. The client is used to send information about rover speed and direction and the server recieves and inprets the information and prints the current speed of the rover and the status of each motor based on the direction sent by the client.


The client key input is taken though pynput and a keycode is extracted based on key pressed. For this project the only useful keys are w,a,s,d,1,2,3,4,5,esc and k. The keys w (87),a (65), s(83), d(68) is used to drive the rover with w being forward, a being left, s being reverse and d is for right. Windows has default int number for each key and its used to analyze which key is pressed. In *on_press* the pressed keys value is extracted and send to *check*. *check* used to analyze if one of the useful key is pressed or not. If the useful key is pressed then the key is logged into a txt file and the information is sent to the server to be interpreted. if *k* is pressed then the connection between server and client is disconnected and *esc*  calls *on_release* and stops listining to user key press.

The server is used as a rover, where it waits for valid user input and prints out the speed and direction in which rover would travel in.


![Screenshot (194)](https://user-images.githubusercontent.com/83378929/138540066-087bf31f-8544-41ca-973f-ac57023c2c95.png)
