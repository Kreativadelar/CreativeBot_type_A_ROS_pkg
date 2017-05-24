#!/usr/bin/env python
# license removed for brevit
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import ColorRGBA
from geometry_msgs.msg import Twist

r = 0
g = 0
b = 0
a = 0

msg = Twist()

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

    if buttons[2] == 1:
	r = 0
	g = 0
        b = 255
    elif buttons[3] == 1:
        r = 255
	g = 255
        b = 0
    elif buttons[1] == 1:
        r = 255
	g = 0
        b = 0
    elif buttons[0] == 1:
        r = 0
	g = 255
        b = 0
    else:
	r = 0
	g = 0        
	b = 0

    pubRGB.publish(r,g,b,a)



# Defining variables
# ----------------------
pubRGB = rospy.Publisher('rgb', ColorRGBA, queue_size=1)
pubTwist = rospy.Publisher('cmd_vel', Twist, queue_size=100)


def main():
    global msg

    # Subscribe for teleoperations
    rospy.Subscriber("joy", Joy, joyCallback)

    rospy.init_node('teleop', anonymous=False)

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
	pubTwist.publish(msg)

        rate.sleep()
        #print("been here!")
        
            


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
	pass
