import math
x_direction, y_direction = 0, 0
while True:
    step = input('Please enter direction(UP | DOWN | LEFT | RIGHT) and number \n')
    if(step == ""):
        break
    
    splits =  step.split(' ')
    if(splits[0] == 'up'  or splits[0] == 'UP'):
        x_direction = y_direction + int(splits[1]) 
    elif(splits[0] == 'down'  or splits[0] == 'DOWN'):
        x_direction = y_direction - int(splits[1])
    elif(splits[0] == 'left' or splits[0] == 'LEFT'):
         y_direction = x_direction - int(splits[1])
    elif(splits[0] == 'right'  or splits[0] == 'RIGHT'):
         y_direction = x_direction + int(splits[1])

# CALCULATING DISTANCE
distance = math.sqrt(x_direction**2 +  y_direction**2)
print("distance", distance)