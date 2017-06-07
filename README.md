# CreativeBot_type_A_ROS_pkg
Makeblock mBot Ranger / Me Auriga ROS package.

Features:
--
-- Sensors
- Get battery state - Topic battery_state
- Get ligth sensor 1 - Topic ligth 1
- Get ligth sensor 2 - Topic ligth 2
- Get left motor velocity (RPM) - Topic left_rpm
- Get right motor velocity (RPM) - Topic right_rpm
- Get sound sensor - Topic sound
- Get temperature - Topic temp
- Get ultrasonic sensor data - Topic ultrasound

-- Control
- Move robot - Topic cmd_vel (Twist)
- Send velocity to left motor (RPM) - Topic lwheel_vtarget (Float32)
- Send velocity to right tmotor (RPM) - Topic rwheel_vtarget (Float32)
- Control led ring - Topic rbg (ColorRGBA)

Hardware:
--
The Me Auriga is connected with USB cable to a Raspberry Pi running Ubuntu Mate and ROS Kinetic

[Images on hardware setup](https://1drv.ms/f/s!AvT_4rqHWl-Rhf1buRJ0OVnz2DojRQ)

Connect ultrasonic sensor to port 9

Required:
--
- [https://github.com/Kreativadelar/CreativeBot_type_A_firmware](CreativeBot type A firmware for the Me Auriga control board)
- [http://wiki.ros.org/rosserial?distro=kinetic](rosserial for communication with Me Auriga control board)
- For teleop. with xbox 360 controller you need [Joy](http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick) 

Installation:
--
cd ~/catkin_ws/src

git clone ..

Troubleshooting
--
Using Raspberry Pi - Ubuntu Mate
Problem with permission on serial port

Add user to group dialout:
usermod -a -G dialout **[user]**
*(Need to logout before it will work)*

Quick fix:
sudo chmod 666 /dev/**[port]** *ex.ttyUSB0*
