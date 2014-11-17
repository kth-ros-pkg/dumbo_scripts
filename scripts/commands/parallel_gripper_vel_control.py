#!/usr/bin/env python



import rospy
import numpy as np
from brics_actuator.msg import JointVelocities, JointPositions, JointValue




if __name__=='__main__':
    rospy.init_node('test_gripper_vel_control')


    gripper_pos_pub = rospy.Publisher('/PG70_controller/command_pos', JointPositions)
    gripper_vel_pub = rospy.Publisher('/PG70_controller/command_vel', JointVelocities)

    rospy.sleep(1.0)

    # set joint position
    gripper_pos_msg = JointPositions()

    gripper_pos = JointValue()
    gripper_pos.timeStamp = rospy.Time.now()
    gripper_pos.joint_uri = 'left_arm_top_finger_joint'
    gripper_pos.unit = 'm'
    gripper_pos.value = 0.025

    gripper_pos_msg.positions = [gripper_pos]

    gripper_pos_pub.publish(gripper_pos_msg)
    rospy.sleep(5.0)

    # send joint velocities

    gripper_vel_msg = JointVelocities()

    gripper_vel = JointValue()
    gripper_vel.timeStamp = rospy.Time.now()
    gripper_vel.joint_uri = 'left_arm_top_finger_joint'
    gripper_vel.unit = 'm/s'

    gripper_vel_msg.velocities = [gripper_vel]

    # while loop

    t_start = rospy.Time.now()

    A = 8e-3
    f = 0.5

    loop_rate = rospy.Rate(500)

    while not rospy.is_shutdown():
        gripper_vel_msg.velocities[0].value = (A)*(2*np.pi*f)*np.sin(2*np.pi*f*(rospy.Time.now()-t_start).to_sec())

        gripper_vel_pub.publish(gripper_vel_msg)
        loop_rate.sleep()
