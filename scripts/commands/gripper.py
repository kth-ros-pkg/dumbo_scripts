#!/usr/bin/env python

import rospy
from brics_actuator.msg import JointPositions, JointValue
from cob_srvs.srv import Trigger

if __name__ == "__main__":
    rospy.init_node('gripper_open_node')

    gripper_pos_pub = rospy.Publisher('/PG70_controller/command_pos', JointPositions)
    gripper_recover_srv = rospy.ServiceProxy('/PG70_controller/recover', Trigger)


    # recover
    gripper_recover_srv()
    rospy.sleep(4.0)

    # open the gripper
    joint_pos_msg = JointPositions()
    joint_val = JointValue()
    joint_val.timeStamp = rospy.Time.now()
    joint_val.joint_uri = "left_arm_top_finger_joint"
    joint_val.unit = "mm"
    joint_val.value = 16

    joint_pos_msg.positions.append(joint_val)

    gripper_pos_pub.publish(joint_pos_msg)

    rospy.sleep(4.0)

    joint_pos_msg.positions[0].value = 4

    gripper_pos_pub.publish(joint_pos_msg)