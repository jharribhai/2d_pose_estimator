# 2d_pose_estimator
Python 2D Pose Estimator 

To estimate (estimate.py) module includes a function called estimated_pose that performs the above calculation to determine the pose of the robot.
Attached to this document is a main.py file as example on how to use the module as shown below:
from estimate import estimated_pose

#initialise the robot's position x = 0, y = 0, heading angle theta # = 0
x = 0
y = 0
theta = 0

#estimated_pose(time,steering_angle,encoder_ticks,angular_velocity,x,y,heading_angle)
[x,y,theta] = estimated_pose(20,0.74,1010,1.2,x,y,theta)
print x,y,theta 
print estimated_pose(20,0,1010,1.2,x,y,theta)
