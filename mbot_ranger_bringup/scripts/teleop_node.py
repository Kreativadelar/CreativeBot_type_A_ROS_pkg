#!/usr/bin/env python
# license removed for brevit
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import ColorRGBA
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

r = 0
g = 0
b = 0
a = 0

last_lin_x_vel = 0
last_ang_z_vel = 0
last_buzzer = 0
last_color = ColorRGBA()

msg = Twist()
buzzer_msg = Vector3()
color_msg = ColorRGBA()

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed
def joyCallback(data):
    handleSticks(data.axes)
    handleButtons(data.buttons)


def handleSticks (axes):
    global msg
    
    msg.linear.x = axes[4]
    msg.linear.y = 0
    msg.linear.z = 0
    msg.angular.z = axes[0]
    


# Check color of button and send RGB color
def handleButtons (buttons):
    global r
    global g
    global b
    global a
    global color_msg
    global buzzer_msg

    if buttons[2] == 1:
	color_msg.r = 0
	color_msg.g = 0
        color_msg.b = 255
    elif buttons[3] == 1:
        color_msg.r = 255
        color_msg.g = 255
        color_msg.b = 0
    elif buttons[1] == 1:
        color_msg.r = 255
	color_msg.g = 0
        color_msg.b = 0	
    elif buttons[0] == 1:
        color_msg.r = 0
	color_msg.g = 255
        color_msg.b = 0
    else:
	color_msg.r = 0
	color_msg.g = 0        
	color_msg.b = 0

    color_msg.a = 0
    #pubRGB.publish(r,g,b,a)

    if buttons[5] == 1:
        buzzer_msg.x = 982
        buzzer_msg.y = 200
        #pubBuzzer.publish(982,10,0)
    elif buttons[5] == 0:
        buzzer_msg.x = 0
        buzzer_msg.y = 0



# Defining variables
# ----------------------
pubRGB = rospy.Publisher('rgb', ColorRGBA, queue_size=1)
pubTwist = rospy.Publisher('cmd_vel', Twist, queue_size=100)
pubBuzzer = rospy.Publisher('buzzer', Vector3, queue_size=1)


def main():
    global msg
    global last_lin_x_vel
    global last_ang_z_vel
    global buzzer_msg
    global last_buzzer
    global color_msg
    global last_color

    # Subscribe for teleoperations
    rospy.Subscriber("joy", Joy, joyCallback)

    rospy.init_node('teleop', anonymous=False)

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        if msg.linear.x != last_lin_x_vel or msg.angular.z != last_ang_z_vel:
	    pubTwist.publish(msg)
            last_lin_x_vel = msg.linear.x
            last_ang_z_vel = msg.angular.z
        
        if buzzer_msg.x != last_buzzer:
            pubBuzzer.publish(buzzer_msg)
            last_buzzer = buzzer_msg.x

        if color_msg != last_color:
            pubRGB.publish(color_msg)
            last_color.r = color_msg.r
            last_color.g = color_msg.g
            last_color.b = color_msg.b
            last_color.a = color_msg.a

        rate.sleep()
        #print("been here!")
        
            


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
	pass
