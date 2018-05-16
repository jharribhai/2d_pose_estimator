# Jatin Harribhai 23/04/2018
# This module calculates and estimates the robot's position in a 2D plane (x,y,heading_angle)
import numpy as np

def estimated_pose(time,alpha,ticks,omega,x,y,theta):
	#time = time [s]
	#alpha = steering_angle [rad]
	#ticks = encoder_ticks
	#omega = angular_velocity [rad/s]
	
	#robot's current position
	# x
	# y
	# theta = heading_angle [rad]
    
    R = 1
    d = 0.75
    # 1 revolution 512 ticks
    rev = 512
    r = 0.2
    
    # distance is calculated in [m]
    factor = ticks / float(rev)
    dist = factor*2*np.pi*r
    #print dist

    #velocity of the steering wheel
    vst = dist / time

    vstx = vst * np.cos(alpha)
    vsty = vst * np.sin(alpha)

    # angular velocity at steering wheel
    omegast = vsty / R

    #global velocities
    vx = vstx * np.cos(theta)
    vy = vstx * np.sin(theta)

    # for 1 second 
    x0 = x
    y0 = y
    theta0 = theta
	
	# calculate the velocity in instantaneous velocities in the x and y direction
    for i in range(time):
        x = x0 + vx*1
        y = y0 + vy*1
        theta = theta0 + omegast*1
        #theta_deg = (theta*180) / np.pi
        vx = vstx * np.cos(theta)
        vy = vstx * np.sin(theta)
        x0 = x
        y0 = y
        theta0 = theta
    
	#return the estimated pose of the robot x,y and heading_angle
    return x,y,theta
