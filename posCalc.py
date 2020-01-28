from math import tan, atan, degrees, sqrt
'''
contains functions for calculating required angles and distances to points
'''


def targetWithStartAsOrigin(startX, startY, endX, endY):
    '''
    function returns a new set of end point with startX and startY as the origin
    '''
    newX = endX - startX
    newY = endY - startY
    return newX, newY


def angleToTarget(startX, startY, endX, endY):
    '''
    function calculates the angle from the start point to the end point in degrees
    returns value from 0 to 360
    '''
    
    # new end points with startX, startY as origin
    newX, newY = targetWithStartAsOrigin(startX, startY, endX, endY)
    
    # theta prime is opposite over adjacent 
    thetaPrime = newY / newX
    
    # inverse thing 
    thetaPrime = degrees(atan(thetaPrime))
    #print(thetaPrime)
    # if quadrant 1, no adjustment 
    if newX >=0 and newY >= 0:
        theta = thetaPrime
    # if quadrant 2, 90 degree adjustment 
    elif newX >= 0 and newY < 0: 
        theta = thetaPrime + 270
    # if quadrant 3, 180 degree adjustment 
    elif newX < 0 and newY >= 0:
        theta = thetaPrime + 90
        
    # if quadrant 4, 270 degree adjustment
    else:
        theta = thetaPrime + 180
        
    return theta 

def calculateNewTrajectory(startX, startY, endX, endY, robotHeadingStart):
    '''
    returns angle required to turn and distance to point once the robot has turned 
    '''
    # distance to target 
    distance = distanceToTarget(startX, startY, endX, endY)
    
    # angle to target assuming robot is at 0 degrees 
    angleAssumed = angleToTarget(startX, startY, endX, endY)
    
    # actual angle the robot must turn to be pointed to heading 
    angleTrue = (angleAssumed - robotHeadingStart) % 360
    
    # return 
    return angleTrue, distance
        
    

def distanceToTarget(startX, startY, endX, endY):
    '''
    returns the distance from the start to the target value 
    '''
    distance = sqrt((endX - startX) ** 2 +(endY - startY) ** 2 )
    return distance
if __name__ == '__main__':
    # example point 
    robotHeadingStart = 0
    startX, startY, endX, endY = -4,4,2,2
    print(calculateNewTrajectory(startX, startY, endX, endY, robotHeadingStart))
