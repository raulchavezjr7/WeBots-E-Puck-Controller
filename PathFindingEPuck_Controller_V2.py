"""PathFindingEPuck_Controller_V1 controller."""
# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import time
import math

def run_robot(robot):
    
    # get the time step of the current world.
    TIME_STEP = int(robot.getBasicTimeStep())
    ROBOT_WHEEL_RADIUS = 0.0205
    ROBOT_AXLE_LENGTH = 0.052 
    MAX_SPEED = 6.28
    ACTION_TYPE = 'DEFAULT'
    
    left_motor = robot.getDevice("left wheel motor")
    right_motor = robot.getDevice("right wheel motor")
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    left_position_sensor = robot.getDevice("left wheel sensor")
    right_position_sensor = robot.getDevice("right wheel sensor")
    left_position_sensor.enable(TIME_STEP)
    right_position_sensor.enable(TIME_STEP)
    
    prox_sensors = []
    for i in range(8):
        sensor_name = 'ps' + str(i)
        prox_sensors.append(robot.getDevice(sensor_name))
        prox_sensors[i].enable(TIME_STEP)
    

    def forward():
        left_motor.setVelocity(MAX_SPEED)
        right_motor.setVelocity(MAX_SPEED)

    def backward():
        left_motor.setVelocity(-MAX_SPEED)
        right_motor.setVelocity(-MAX_SPEED)
        
    def left():
        left_motor.setVelocity(-MAX_SPEED/10)
        right_motor.setVelocity(MAX_SPEED/10)
        
    def right():
        left_motor.setVelocity(MAX_SPEED/10)
        right_motor.setVelocity(-MAX_SPEED/10)
        
    def stop():
        left_motor.setVelocity(0)
        right_motor.setVelocity(0) 
    
    def getNextLocation():
        new_x = saved_location[0][0]
        new_y = saved_location[0][1]
        match direction:
            case 1:
                return new_x, new_y + 1
            case 2:
                return new_x + 1, new_y + 1
            case 3:
                return new_x + 1, new_y
            case 4:
                return new_x + 1, new_y - 1
            case 5:
                return new_x, new_y - 1
            case 6:
                return new_x - 1, new_y - 1
            case 7:
                return new_x - 1, new_y
            case 8:
                return new_x - 1, new_y + 1
            
    def reach_goal_logic():
        print('logic')
        print(saved_location)
        #print(direction)
        #print(prox_sensors_value)
        print(math.degrees(math.atan2(-(goal[1]-saved_location[saved_points][1]), goal[0]-saved_location[saved_points][0])))
        print(direction)
        #1 -90
        #2 0 -> -90
        #3 0
        #4 0 -> 90
        #5 90
        #6 90 -> 180
        #7 180
        #8 -90 -> -180
        #if prox_sensors_value[2] > 75:
         #   return "forward"
        if flag == True:
            if direction == 1 or direction == 3 or direction == 5 or direction == 7:
                return "forward"
            else:
                return "forward angle"
        angle_to_goal = math.degrees(math.atan2(-(goal[1]-saved_location[0][1]), goal[0]-saved_location[0][0]))
        if angle_to_goal == -90:
            match direction:
                case 1:
                    if prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[5] > 75:
                            return "turn around"
                        else:
                            return "left"
                    else:
                        return "forward"  
                case 2:
                    if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[4] > 75:
                            if prox_sensors_value[3] > 75:
                                return "right angle"
                            else:
                                return "right + angle"
                        else:
                            return "left + angle"
                    else:
                        return "left angle"
                case 3:
                    if prox_sensors_value[5] > 75:
                        if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                            return "right"
                        else:
                            return "turn around"
                    else:
                        return "left"
                case 4:
                    if prox_sensors_value[4] > 75:
                        if prox_sensors_value[3] > 75:
                            return "right angle"
                        else:
                            return "right + angle"
                    else:
                        return "left + angle"
                case 5:
                    if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                        if prox_sensors_value[2] > 75:
                            return "forward"
                        else:
                            return "right"
                    else:
                        return "turn around"
                case 6:
                    if prox_sensors_value[3] > 75:
                        if prox_sensors_value[1] > 75:
                            return "left angle"
                        else:
                            return "right angle"
                    else:
                        return "right + angle"
                case 7:
                    if prox_sensors_value[2] > 75:
                        if  prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75:
                            return "left"
                        else:
                            return "forward"
                    else:
                        return "right"
                case 8:
                    if prox_sensors_value[0] > 75 or prox_sensors_value[1] > 75:
                        if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                            return "left + angle"
                        else:
                            return "left angle"
                    else:
                        return "right angle"
        elif angle_to_goal > -90 and angle_to_goal < 0:
            match direction:
                case 1:
                    if prox_sensors_value[1] > 75 or prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75 or prox_sensors_value[2] > 75:
                        if prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75:
                            if prox_sensors_value[5] > 75:
                                return "turn around"
                            else:
                                return "left"
                        else: 
                            return "forward"
                    else:
                        return "right angle"
                case 2:
                    if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[4] > 75:
                            return "right + angle"
                        else:
                            return "left + angle"
                    else:
                        if has_moved == False:
                            return "forward angle"
                        else:
                            return "left angle check"
                case 3:
                    if prox_sensors_value[5] > 75 or prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75 or prox_sensors_value[6] > 75:
                        if prox_sensors_value[5] > 75:
                            if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                                return "right"
                            else:
                                return "turn around"
                        else: 
                            return "left"
                    else:
                        return "left angle"
                case 4:
                    if prox_sensors_value[5] > 75 or prox_sensors_value[4] > 75 or prox_sensors_value[7] > 75 or prox_sensors_value[6] > 75:
                        if prox_sensors_value[4] > 75:
                            if prox_sensors_value[3] > 75:
                                return "right angle"
                            else:
                                return "right + angle"
                        else: 
                            return "left + angle"
                    else:
                        return "left"
                case 5:
                    if prox_sensors_value[3] > 75 or prox_sensors_value[4] > 75 or prox_sensors_value[5] > 75:
                        if prox_sensors_value[2] > 75:
                            return "right"
                        else:
                            return "forward"
                    else:
                        if has_moved == False:
                            return "left + angle"
                        else:
                            return "turn around check"
                case 6:
                    if prox_sensors_value[3] or prox_sensors_value[4] > 75:
                        if prox_sensors_value[1] > 75 or prox_sensors_value[0] > 75:
                            return "left angle"
                        else:
                            return "right angle"
                    else:
                        if has_moved == False:
                            return "turn around"
                        else:
                            return "right + angle check"
                case 7:
                    if prox_sensors_value[3] > 75 or prox_sensors_value[4] > 75 or prox_sensors_value[2] > 75:
                        if prox_sensors_value[7] > 75 or prox_sensors_value[0] > 75:
                            return "left"
                        else:
                            return "forward"
                    else:
                        if has_moved == False:
                            return "right + angle"
                        else:
                            return "right check"
                case 8:
                    if prox_sensors_value[1] > 75 or prox_sensors_value[0] > 75 or prox_sensors_value[2] > 75 or prox_sensors_value[3] > 75:
                        if prox_sensors_value[0] > 75 or prox_sensors_value[1] > 75:
                            if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                                return "left + angle"
                            else:
                                return "left angle"
                        else: 
                            return "right angle"
                    else:
                        return "right"
        elif angle_to_goal == 0:
            match direction:
                case 1:
                    if prox_sensors_value[2] > 75:
                        if prox_sensors_value[7] > 75 or prox_sensors_value[0] > 75:
                            return "left"
                        else:
                            return "forward"
                    else:
                        return "right"
                case 2:
                    if prox_sensors_value[0] > 75 or prox_sensors_value[1] > 75:
                        if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                            return "left + angle"
                        else:
                            return "left angle"
                    else:
                        return "right angle"
                case 3:
                    if prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[5] > 75:
                            return "turn around"
                        else:
                            return "left"
                    else:
                        return "forward"  
                case 4:
                    if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[4] > 75:
                            if prox_sensors_value[3] > 75:
                                return "right angle"
                            else:
                                return "right + angle"
                        else:
                            return "left + angle"
                    else:
                        return "left angle"
                case 5:
                    if prox_sensors_value[5] > 75:
                        if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                            return "right"
                        else:
                            return "turn around"
                    else:
                        return "left"
                case 6:
                    if prox_sensors_value[4] > 75:
                        if prox_sensors_value[3] > 75:
                            return "right angle"
                        else:
                            return "right + angle"
                    else:
                        return "left + angle"
                case 7:
                    if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                        if prox_sensors_value[2] > 75:
                            return "forward"
                        else:
                            return "right"
                    else:
                        return "turn around"
                case 8:
                    if prox_sensors_value[3] > 75:
                        if prox_sensors_value[1] > 75:
                            return "left angle"
                        else:
                            return "right angle"
                    else:
                        return "right + angle"
        elif angle_to_goal > 0 and angle_to_goal < 90:
            match direction:
                case 1:
                    if prox_sensors_value[3] > 75 or prox_sensors_value[4] > 75 or prox_sensors_value[2] > 75:
                        if prox_sensors_value[7] > 75 or prox_sensors_value[0] > 75:
                            return "left"
                        else:
                            return "forward"
                    else:
                        if has_moved == False:
                            return "right + angle"
                        else:
                            return "right check"
                case 2:
                    if prox_sensors_value[1] > 75 or prox_sensors_value[0] > 75 or prox_sensors_value[2] > 75 or prox_sensors_value[3] > 75:
                        if prox_sensors_value[0] > 75 or prox_sensors_value[1] > 75:
                            if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                                return "left + angle"
                            else:
                                return "left angle"
                        else: 
                            return "right angle"
                    else:
                        return "right"
                case 3:
                    if prox_sensors_value[1] > 75 or prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75 or prox_sensors_value[2] > 75:
                        if prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75:
                            if prox_sensors_value[5] > 75:
                                return "turn around"
                            else:
                                return "left"
                        else: 
                            return "forward"
                    else:
                        return "right angle"
                case 4:
                    if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[4] > 75:
                            return "right + angle"
                        else:
                            return "left + angle"
                    else:
                        if has_moved == False:
                            return "forward angle"
                        else:
                            return "left angle check"
                case 5:
                    if prox_sensors_value[5] > 75 or prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75 or prox_sensors_value[6] > 75:
                        if prox_sensors_value[5] > 75:
                            if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                                return "right"
                            else:
                                return "turn around"
                        else: 
                            return "left"
                    else:
                        return "left angle"
                case 6:
                    if prox_sensors_value[5] > 75 or prox_sensors_value[4] > 75 or prox_sensors_value[7] > 75 or prox_sensors_value[6] > 75:
                        if prox_sensors_value[4] > 75:
                            if prox_sensors_value[3] > 75:
                                return "right angle"
                            else:
                                return "right + angle"
                        else: 
                            return "left + angle"
                    else:
                        return "left"
                case 7:
                    if prox_sensors_value[3] > 75 or prox_sensors_value[4] > 75 or prox_sensors_value[5] > 75:
                        if prox_sensors_value[2] > 75:
                            return "right"
                        else:
                            return "forward"
                    else:
                        if has_moved == False:
                            return "left + angle"
                        else:
                            return "turn around check"
                case 8:
                    if prox_sensors_value[3] or prox_sensors_value[4] > 75:
                        if prox_sensors_value[1] > 75 or prox_sensors_value[0] > 75:
                            return "left angle"
                        else:
                            return "right angle"
                    else:
                        if has_moved == False:
                            return "turn around"
                        else:
                            return "right + angle check"
        elif angle_to_goal == 90:
            match direction:
                case 3:
                    if prox_sensors_value[2] > 75:
                        if prox_sensors_value[7] > 75 or prox_sensors_value[0] > 75:
                            return "left"
                        else:
                            return "forward"
                    else:
                        return "right"
                case 4:
                    if prox_sensors_value[0] > 75 or prox_sensors_value[1] > 75:
                        if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                            return "left + angle"
                        else:
                            return "left angle"
                    else:
                        return "right angle"
                case 5:
                    if prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[5] > 75:
                            return "turn around"
                        else:
                            return "left"
                    else:
                        return "forward"  
                case 6:
                    if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[4] > 75:
                            if prox_sensors_value[3] > 75:
                                return "right angle"
                            else:
                                return "right + angle"
                        else:
                            return "left + angle"
                    else:
                        return "left angle"
                case 7:
                    if prox_sensors_value[5] > 75:
                        if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                            return "right"
                        else:
                            return "turn around"
                    else:
                        return "left"
                case 8:
                    if prox_sensors_value[4] > 75:
                        if prox_sensors_value[3] > 75:
                            return "right angle"
                        else:
                            return "right + angle"
                    else:
                        return "left + angle"
                case 1:
                    if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                        if prox_sensors_value[2] > 75:
                            return "forward"
                        else:
                            return "right"
                    else:
                        return "turn around"
                case 2:
                    if prox_sensors_value[3] > 75:
                        if prox_sensors_value[1] > 75:
                            return "left angle"
                        else:
                            return "right angle"
                    else:
                        return "right + angle"
        elif angle_to_goal > 90 and angle_to_goal < 180:
            match direction:
                case 1:
                    if prox_sensors_value[2] > 75:
                        if prox_sensors_value[7] > 75 or prox_sensors_value[0] > 75:
                            return "left"
                        else:
                            return "forward"
                    else:
                        return "right"
                case 2:
                    if prox_sensors_value[0] > 75 or prox_sensors_value[1] > 75:
                        if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                            return "left + angle"
                        else:
                            return "left angle"
                    else:
                        return "right angle"
                case 3:
                    if prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[5] > 75:
                            return "turn around"
                        else:
                            return "left"
                    else:
                        return "forward"  
                case 4:
                    if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[4] > 75:
                            if prox_sensors_value[3] > 75:
                                return "right angle"
                            else:
                                return "right + angle"
                        else:
                            return "left + angle"
                    else:
                        return "left angle"
                case 5:
                    if prox_sensors_value[5] > 75:
                        if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                            return "right"
                        else:
                            return "turn around"
                    else:
                        return "left"
                case 6:
                    if prox_sensors_value[4] > 75:
                        if prox_sensors_value[3] > 75:
                            return "right angle"
                        else:
                            return "right + angle"
                    else:
                        return "left + angle"
                case 7:
                    if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                        if prox_sensors_value[2] > 75:
                            return "forward"
                        else:
                            return "right"
                    else:
                        return "turn around"
                case 8:
                    if prox_sensors_value[3] > 75:
                        if prox_sensors_value[1] > 75:
                            return "left angle"
                        else:
                            return "right angle"
                    else:
                        return "right + angle"
        elif angle_to_goal > 0 and angle_to_goal < 90:
            match direction:
                case 3:
                    if prox_sensors_value[3] > 75 or prox_sensors_value[4] > 75 or prox_sensors_value[2] > 75:
                        if prox_sensors_value[7] > 75 or prox_sensors_value[0] > 75:
                            return "left"
                        else:
                            return "forward"
                    else:
                        if has_moved == False:
                            return "right + angle"
                        else:
                            return "right check"
                case 4:
                    if prox_sensors_value[1] > 75 or prox_sensors_value[0] > 75 or prox_sensors_value[2] > 75 or prox_sensors_value[3] > 75:
                        if prox_sensors_value[0] > 75 or prox_sensors_value[1] > 75:
                            if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                                return "left + angle"
                            else:
                                return "left angle"
                        else: 
                            return "right angle"
                    else:
                        return "right"
                case 5:
                    if prox_sensors_value[1] > 75 or prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75 or prox_sensors_value[2] > 75:
                        if prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75:
                            if prox_sensors_value[5] > 75:
                                return "turn around"
                            else:
                                return "left"
                        else: 
                            return "forward"
                    else:
                        return "right angle"
                case 6:
                    if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[4] > 75:
                            return "right + angle"
                        else:
                            return "left + angle"
                    else:
                        if has_moved == False:
                            return "forward angle"
                        else:
                            return "left angle check"
                case 7:
                    if prox_sensors_value[5] > 75 or prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75 or prox_sensors_value[6] > 75:
                        if prox_sensors_value[5] > 75:
                            if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                                return "right"
                            else:
                                return "turn around"
                        else: 
                            return "left"
                    else:
                        return "left angle"
                case 8:
                    if prox_sensors_value[5] > 75 or prox_sensors_value[4] > 75 or prox_sensors_value[7] > 75 or prox_sensors_value[6] > 75:
                        if prox_sensors_value[4] > 75:
                            if prox_sensors_value[3] > 75:
                                return "right angle"
                            else:
                                return "right + angle"
                        else: 
                            return "left + angle"
                    else:
                        return "left"
                case 1:
                    if prox_sensors_value[3] > 75 or prox_sensors_value[4] > 75 or prox_sensors_value[5] > 75:
                        if prox_sensors_value[2] > 75:
                            return "right"
                        else:
                            return "forward"
                    else:
                        if has_moved == False:
                            return "left + angle"
                        else:
                            return "turn around check"
                case 2:
                    if prox_sensors_value[3] or prox_sensors_value[4] > 75:
                        if prox_sensors_value[1] > 75 or prox_sensors_value[0] > 75:
                            return "left angle"
                        else:
                            return "right angle"
                    else:
                        if has_moved == False:
                            return "turn around"
                        else:
                            return "right + angle check"
        elif angle_to_goal == 180:
            match direction:
                case 7:
                    if prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[5] > 75:
                            return "turn around"
                        else:
                            return "left"
                    else:
                        return "forward"  
                case 8:
                    if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[4] > 75:
                            if prox_sensors_value[3] > 75:
                                return "right angle"
                            else:
                                return "right + angle"
                        else:
                            return "left + angle"
                    else:
                        return "left angle"
                case 1:
                    if prox_sensors_value[5] > 75:
                        if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                            return "right"
                        else:
                            return "turn around"
                    else:
                        return "left"
                case 2:
                    if prox_sensors_value[4] > 75:
                        if prox_sensors_value[3] > 75:
                            return "right angle"
                        else:
                            return "right + angle"
                    else:
                        return "left + angle"
                case 3:
                    if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                        if prox_sensors_value[2] > 75:
                            return "forward"
                        else:
                            return "right"
                    else:
                        return "turn around"
                case 4:
                    if prox_sensors_value[3] > 75:
                        if prox_sensors_value[1] > 75:
                            return "left angle"
                        else:
                            return "right angle"
                    else:
                        return "right + angle"
                case 5:
                    if prox_sensors_value[2] > 75:
                        if  prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75:
                            return "left"
                        else:
                            return "forward"
                    else:
                        return "right"
                case 6:
                    if prox_sensors_value[0] > 75 or prox_sensors_value[1] > 75:
                        if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                            return "left + angle"
                        else:
                            return "left angle"
                    else:
                        return "right angle"
        elif angle_to_goal > -180 and angle_to_goal < -90:
            match direction:
                case 5:
                    if prox_sensors_value[3] > 75 or prox_sensors_value[4] > 75 or prox_sensors_value[2] > 75:
                        if prox_sensors_value[7] > 75 or prox_sensors_value[0] > 75:
                            return "left"
                        else:
                            return "forward"
                    else:
                        if has_moved == False:
                            return "right + angle"
                        else:
                            return "right check"
                case 6:
                    if prox_sensors_value[1] > 75 or prox_sensors_value[0] > 75 or prox_sensors_value[2] > 75 or prox_sensors_value[3] > 75:
                        if prox_sensors_value[0] > 75 or prox_sensors_value[1] > 75:
                            if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                                return "left + angle"
                            else:
                                return "left angle"
                        else: 
                            return "right angle"
                    else:
                        return "right"
                case 7:
                    if prox_sensors_value[1] > 75 or prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75 or prox_sensors_value[2] > 75:
                        if prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75:
                            if prox_sensors_value[5] > 75:
                                return "turn around"
                            else:
                                return "left"
                        else: 
                            return "forward"
                    else:
                        return "right angle"
                case 8:
                    if prox_sensors_value[6] > 75 or prox_sensors_value[7] > 75:
                        if prox_sensors_value[4] > 75:
                            return "right + angle"
                        else:
                            return "left + angle"
                    else:
                        if has_moved == False:
                            return "forward angle"
                        else:
                            return "left angle check"
                case 1:
                    if prox_sensors_value[5] > 75 or prox_sensors_value[0] > 75 or prox_sensors_value[7] > 75 or prox_sensors_value[6] > 75:
                        if prox_sensors_value[5] > 75:
                            if prox_sensors_value[4] > 75 or prox_sensors_value[3] > 75:
                                return "right"
                            else:
                                return "turn around"
                        else: 
                            return "left"
                    else:
                        return "left angle"
                case 2:
                    if prox_sensors_value[5] > 75 or prox_sensors_value[4] > 75 or prox_sensors_value[7] > 75 or prox_sensors_value[6] > 75:
                        if prox_sensors_value[4] > 75:
                            if prox_sensors_value[3] > 75:
                                return "right angle"
                            else:
                                return "right + angle"
                        else: 
                            return "left + angle"
                    else:
                        return "left"
                case 3:
                    if prox_sensors_value[3] > 75 or prox_sensors_value[4] > 75 or prox_sensors_value[5] > 75:
                        if prox_sensors_value[2] > 75:
                            return "right"
                        else:
                            return "forward"
                    else:
                        if has_moved == False:
                            return "left + angle"
                        else:
                            return "turn around check"
                case 4:
                    if prox_sensors_value[3] or prox_sensors_value[4] > 75:
                        if prox_sensors_value[1] > 75 or prox_sensors_value[0] > 75:
                            return "left angle"
                        else:
                            return "right angle"
                    else:
                        if has_moved == False:
                            return "turn around"
                        else:
                            return "right + angle check"

    move_type = "forward"
    obstacle_detected = False
    move_count_range = 25
    move_count = 0
    direction = 1
    forward_count = 26
    angle_forward_count = 36
    #goal = [24, 24]
    goal = [24, 24]
    base_position = [24, 1]
    saved_points = 0
    temp_goal = [24,1]
    saved_location = [[24, 1]]
    has_moved = True
    flag = False
    
    while robot.step(TIME_STEP) != -1:
        prox_sensors_value = [0]*8
        #print(move_count)
        if move_count == 1:
            print(move_type)
            print(has_moved)
            print(flag)
            match move_type:
                case "forward":
                    forward()
                    saved_location[saved_points][0], saved_location[saved_points][1] = getNextLocation()
                    print(saved_location)
                    move_count_range = forward_count
                    has_moved = True
                    flag = False
                case "left":
                    left()
                    if direction == 1:
                        direction = 7
                    elif direction == 2:
                        direction = 8
                    else: 
                        direction -= 2
                    move_count_range = 111
                    has_moved = False
                    flag = True
                case "right":
                    right()
                    if direction == 7:
                        direction = 1
                    elif direction == 8:
                        direction = 2
                    else: 
                        direction += 2
                    move_count_range = 111
                    has_moved = False
                    flag = True
                case "right check":
                    right()
                    if direction == 7:
                        direction = 1
                    elif direction == 8:
                        direction = 2
                    else: 
                        direction += 2
                    move_count_range = 111
                    has_moved = True
                case "forward angle":
                    forward()
                    saved_location[saved_points][0], saved_location[saved_points][1] = getNextLocation()
                    print(saved_location)
                    move_count_range = angle_forward_count
                    has_moved = True
                    flag = False
                case "right angle":
                    right()
                    if direction == 8:
                        direction = 1
                    else: 
                        direction += 1
                    move_count_range = 56
                    has_moved = False
                    flag = True
                case "left angle":
                    left()
                    if direction == 1:
                        direction = 8
                    else: 
                        direction -= 1
                    move_count_range = 56
                    has_moved = False
                    flag = True
                case "left angle check":
                    left()
                    if direction == 1:
                        direction = 8
                    else: 
                        direction -= 1
                    move_count_range = 56
                    has_moved = True
                case "right + angle":
                    right()
                    if direction == 6:
                        direction = 1
                    elif direction == 7:
                        direction = 2
                    elif direction == 8:
                        direction = 3
                    else: 
                        direction += 3
                    move_count_range = 166
                    has_moved = False
                    flag = True
                case "right + angle check":
                    right()
                    if direction == 6:
                        direction = 1
                    elif direction == 7:
                        direction = 2
                    elif direction == 8:
                        direction = 3
                    else: 
                        direction += 3
                    move_count_range = 166
                    has_moved = True
                case "left + angle":
                    left()
                    if direction == 1:
                        direction = 6
                    elif direction == 2:
                        direction = 7
                    elif direction == 3:
                        direction = 8
                    else: 
                        direction -= 3
                    move_count_range = 166
                    has_moved = False
                    flag = True
                case "turn around":
                    left()
                    if direction == 1:
                        direction = 5
                    elif direction == 2:
                        direction = 6
                    elif direction == 3:
                        direction = 7
                    elif direction == 4:
                        direction = 8
                    else: 
                        direction -= 4
                    move_count_range = 222
                    has_moved = False
                    flag = True
                case "turn around check":
                    left()
                    if direction == 1:
                        direction = 5
                    elif direction == 2:
                        direction = 6
                    elif direction == 3:
                        direction = 7
                    elif direction == 4:
                        direction = 8
                    else: 
                        direction -= 4
                    move_count_range = 222
                    has_moved = True
        # #445 /360
        # #222 /180
        # 166 /135
        # #111 /90
        # #56 /45
        # #53 /44.1
        # #21 /17.1
        elif move_count == move_count_range:
            stop()
            print("stop")
            for i in range(8):
                prox_sensors_value[i] = prox_sensors[i].getValue()
                print("index: {}, val: {:.4f}".format(i, prox_sensors[i].getValue()))
                if prox_sensors[i].getValue() > 75:
                    #print(i)
                    obstacle_detected = True
            move_type = reach_goal_logic()
            print(move_type)
            #print('STOP')
        elif move_count == move_count_range+2 and obstacle_detected != True:
            print("no obtacle after stop")
            move_count = 0
        elif move_count == move_count_range+2 and obstacle_detected == True:
            print("obtacle after stop")
            obstacle_detected = False
            move_count = 0
        
        move_count += 1
        # Read the sensors:
        
        # Process sensor data here.
        
        # Enter here functions to send actuator commands, like:
       
    
    # Enter here exit cleanup code.
if __name__ == "__main__":
    # create the Robot instance.
    my_robot = Robot()
    run_robot(my_robot)
