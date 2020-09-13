#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

import sys, termios, tty, os, time, fcntl, pygame
from pygame.locals import *

def talker():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    clock = pygame.time.Clock()
    x_dir = "stop"
    y_dir = "stop"
    z_dir = "stop"
    x_speed = 0
    y_speed = 0
    z_speed = 0
    pub = rospy.Publisher('motor_commands', String, queue_size=10)
    rospy.init_node('manual_motor_controller', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pygame.event.pump()
        keys=pygame.key.get_pressed()
        print(keys[K_a])
        if (keys[K_a]):
            x_dir = "left"
        elif (keys[K_d]):
            x_dir = "right"
        else:
            x_dir = "stop"
        if (keys[K_w]):
            y_dir = "forward"
        elif (keys[K_s]):
            y_dir = "back"
        else:
            y_dir = "stop"
        if (keys[K_i]):
            z_dir = "up"
        elif (keys[K_k]):
            z_dir = "down"
        else:
            z_dir = "stop"
        if (keys[K_l]):
            x_speed += 100
            y_speed += 100
            z_speed += 100
        elif (keys[K_j]):
            x_speed -= 100
            y_speed -= 100
            z_speed -= 100
        if (x_speed > 10000):
            x_speed = 10000
        elif (x_speed < 0):
            x_speed = 0
        if (y_speed > 10000):
            y_speed = 10000
        elif (y_speed < 0):
            y_speed = 0
        if (z_speed > 10000):
            z_speed = 10000
        elif (z_speed < 0):
            z_speed = 0
        commands = x_dir+" "+str(x_speed)+" "+y_dir+" "+str(y_speed)+" "+z_dir+" "+str(z_speed)
        print(commands)
        rospy.loginfo(commands)
        pub.publish(commands)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


