#!/usr/bin/env python
# license removed for brevit
import rospy

from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from math import pi

# Parameters
max_rpm = 180.0
distance_between = 0.145
wheel_diameter = 0.043
angular_velocity_multiplier = 5.59
linear_velocity_multiplier = 0.41


left_vel = 0.0
right_vel = 0.0

last_left_vel = 0.0
last_right_vel = 0.0


# Receives twist messages and convert to motor vel
def twistCallback(vel):
    global left_vel
    global right_vel

    two_pi = pi * 2

    # Distance between wheels are 145 mm
    # Wheel plus thicknes of track are 4 3mm in diameter 43 / 2 = 2.15 mm

    angularCalc = vel.angular.z * angular_velocity_multiplier;
    linearCalc = vel.linear.x * linear_velocity_multiplier;
  
    rad_sec_left = (linearCalc - angularCalc * distance_between / 2.0)/(wheel_diameter/2.0);

    rad_sec_right = (linearCalc + angularCalc * distance_between / 2.0)/(wheel_diameter/2.0); 

    rpm_left = (60/two_pi) * rad_sec_left; 

    rpm_right = (60/two_pi) * rad_sec_right;

    if rpm_left > max_rpm:
        rpm_left = max_rpm
    
    elif rpm_left < -max_rpm:
        rpm_left = -max_rpm
    
  
    if rpm_right > max_rpm:
        rpm_right = max_rpm
    
    elif rpm_right < -max_rpm:
        rpm_right = -max_rpm

    right_vel = rpm_right
    left_vel = rpm_left



# Defining variables
# ----------------------
pubLeftMotorVel = rospy.Publisher('lwheel_vtarget', Float32, queue_size=100)
pubRightMotorVel = rospy.Publisher('rwheel_vtarget', Float32, queue_size=100)


def main():
    global last_left_vel
    global last_right_vel
    global left_vel
    global right_vel


    # Subscribe for teleoperations
    rospy.Subscriber("cmd_vel", Twist, twistCallback)

    rospy.init_node('twistToMotor', anonymous=False)

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        
	if left_vel != last_left_vel:
		pubLeftMotorVel.publish(left_vel)
		last_left_vel = left_vel
	
	if right_vel != last_right_vel:
		pubRightMotorVel.publish(right_vel)
		last_right_vel = right_vel     
		
        rate.sleep()
        #print("been here!")
        
            


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
	pass
