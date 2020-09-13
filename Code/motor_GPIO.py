#!/usr/bin/env python
import rospy, gpiozero, time
from std_msgs.msg import String

commands = ["left",0,"back",0,"up",0]

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    global commands=(data.data).split()
    global commands[2]=int(commands[2])
    global commands[4]=int(commands[4])
    global commands[6]=int(commands[6])

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('motor_GPIO', anonymous=False)

    rospy.Subscriber("motor_commands", String, callback)
    x_dirPin = gpiozero.LED(2)
    y_dirPin = gpiozero.LED(4)
    z_dirPin = gpiozero.LED(6)
    x_speedPin = gpiozero.LED(3)
    y_speedPin = gpiozero.LED(5)
    z_speedPin = gpiozero.LED(7)


    while not rospy.is_shutdown():
#directional pins
        if (commands[0] == "left"):
            x_dirPin.off()
        else:
            x_dirPin.on()
        if (commands[2] == "back"):
            y_dirPin.off()
        else:
            y_dirPin.on()
        if (commands[4] == "down"):
            z_dirPin.off()
        else:
            z_dirPin.on()

#update speeds
        x_speed = int(commands[1])
        y_speed = int(commands[3])
        z_speed = int(commands[5])

#if you're not holding down the button, set speed to zero
        if (commands[0] == "stop"):
            x_speed = 0
        if (commands[2] == "stop"):
            y_speed = 0
        if (commands[4] == "stop"):
            z_speed = 0

#finds periods at which to pulse with
        x_period = 1/x_speed*1000000
        y_period = 1/y_speed*1000000
        z_period = 1/z_speed*1000000

#use mod of timer by period to see if it's time to pulse on or off
        if((time.time*1000000)%x_period < x_period//2):
            x_speedPin.on()
        else:
            x_speedPin.off()
        if((time.time*1000000)%y_period < y_period//2):
            y_speedPin.on()
        else:
            x_speedPin.off()
        if((time.time*1000000)%z_period < z_period//2):
            z_speedPin.on()
        else:
            z_speedPin.off()
        rospy.spinOnce() # spinOnce() checks for new messages once
        
#end of while loop

if __name__ == '__main__':
    listener()

