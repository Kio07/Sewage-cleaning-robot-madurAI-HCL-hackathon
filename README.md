# TECH-WARRIORS
Sewage cleaning robot

In today’s era automation and artificial intelligence plays a very important role in all industrial applications for the proper disposal of sewage from
industries and household is still a challenging task. In India drainage systems are usually open which leads to disposal of
solid waste and that causes blockage. Drains are used for the adequate disposal of waste and unfortunately sometimes
there may be a threat to human life during the cleaning of blockage in the drains or it can cause serious health issues
because of the pertaining problems like malaria, dengue, etc. In order to overcome this problem as well as to save human
life we implement a design “Automatic Drainage Cleaning System”. We designed our project in order to use it in an
efficient way to control the disposal of waste along with regular filtration of drains, removal of solid waste in order to
avoid blockage in drains to promote continuous flow of drainage water which ultimately reduces the threat to human life.

# PROBLEM STATEMENT:

   - To develop a new sewage cleaning system in our environment
    - There should be no harm to the society due to the advancement of robotic technology.
    - In contrast to current systems, this robot operates wireless which significantly increases the range of application areas. 
- To manage the robot in the hazardous environment of sewers, the robot has to be designed very carefully.
	- Present situation of sewage system which shows the low level of the human’s health.
	- To avoid such situation sewage robots can be launched to make sure it should not harm the welfare of humans.
	- The description is based on the control hardware and functions of the robotics in sewage environment. 
	- Using different types of sensors, the robots act on different actions and prepare the moves according to it.
	- The sensor detects the object and cleans the dust in sewage area.
	- At current suitation, the peoples are harmed to different hazardous diseases and they are infected by different acids, toxics in sewage.
	- To avoid such situation robots are been developed


    
import numpy as np
#import matplotlib.pyplot as pt
#import pandas as pd
import math
# generate and send the correct commands to the robot
def _send_robot_commands( self ):
    v,omega=0;
    v_l, v_r = self._uni_to_diff( v, omega )
    self.robot.set_wheel_drive_rate( v_l, v_r )
    
    
def _uni_to_diff( self, v, omega ):
  # v = translational velocity (m/s)
  # omega = angular velocity (rad/s)
 
  R = self.robot_wheel_radius
  L = self.robot_wheel_base_length
  v_l = ( (2.0 * v) - (omega*L) ) / (2.0 * R)
  v_r = ( (2.0 * v) + (omega*L) ) / (2.0 * R)

  return v_l, v_r
  # update the distances indicated by the proximity sensors
def _update_proximity_sensor_distances( self ):
   
    self.proximity_sensor_distances = [ 0.02-( math.log(readval/3960.0) )/30.0 for
        readval in self.robot.read_proximity_sensors() ]
        # update the estimated position of the robot using it's wheel encoder readings
def _update_odometry( self ):
    R = self.robot_wheel_radius
    N = float( self.wheel_encoder_ticks_per_revolution )
    
    # read the wheel encoder values
    ticks_left, ticks_right = self.robot.read_wheel_encoders()
    
    # get the difference in ticks since the last iteration
    d_ticks_left = ticks_left - self.prev_ticks_left
    d_ticks_right = ticks_right - self.prev_ticks_right
    
    # estimate the wheel movements
    d_left_wheel = 2*math.pi*R*( d_ticks_left / N )
    d_right_wheel = 2*math.pi*R*( d_ticks_right / N )
    d_center = 0.5 * ( d_left_wheel + d_right_wheel )
    
    # calculate the new pose
    prev_x, prev_y, prev_theta = self.estimated_pose.scalar_unpack()
    new_x = prev_x + (d_center* math.acos(prev_theta))
    new_y = prev_y + ( d_center * math.asin( prev_theta ) )
    new_theta = prev_theta + ( ( d_right_wheel - d_left_wheel ) / self.robot_wheel_base_length )
    
    # update the pose estimate with the new values
    self.estimated_pose.scalar_update( new_x, new_y, new_theta )
    
    # save the current tick count for the next iteration
    self.prev_ticks_left = ticks_left
    self.prev_ticks_right = ticks_right
    # return a go-to-goal heading vector in the robot's reference frame
def calculate_gtg_heading_vector( self ):
    # get the inverse of the robot's pose
    robot_inv_pos, robot_inv_theta = self.supervisor.estimated_pose().inverse().vector_unpack()
    
    # calculate the goal vector in the robot's reference frame
    goal = self.supervisor.goal()
    goal = np.linalg.rotate_and_translate_vector( goal, robot_inv_theta, robot_inv_pos )
    
    return goal

