#!/usr/bin/env python

import rospy
from moveit_commander import MoveGroupCommander



if __name__=="__main__":
    rospy.init_node('move_joint_pos')

    robot = MoveGroupCommander('left_arm')

    q = [-0.3228016793727875, -1.2804502248764038, -0.1374697983264923, -0.46571001410484314, 0.08562547713518143, -1.4503231048583984, 0.9202476739883423]

    robot.set_joint_value_target(q)

    robot.go()
