import math
robot_sizes = [1,2,3,4,5]
person_power = 1
def calcRobotPower (rs):
    rp = 0
    for i in range(1,rs+1):
        rp = rp + i
    return rp

#calculate fuction
for rs in robot_sizes:
    robot_power=calcRobotPower(rs)
    people_required = math.ceil(robot_power/person_power)
    print('Number of people required to defeat a robot of size',
rs, 'is:', people_required)

print('To be continued')
