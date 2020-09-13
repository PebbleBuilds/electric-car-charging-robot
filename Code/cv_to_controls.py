def controls(circle, axis):
    speed = None
    if axis == 'x':
        if circle[0] > resizedw/3 and circle[0] < 2*resizedw/3:
            if circle[0] < resizedw/2 + 5 and circle[0] > resizedw/2 - 5:
                speed = 'stop'
            else:
                speed = 'slow'
        else: 
            speed = "fast"
    elif axis == 'z':
        if circle[1] > resizedh/3 and circle[1] < 2*resizedh/3:
            if circle[1] < resizedh/2 + 5 and circle[1] > resizedh/2 - 5:
                speed = 'stop'
            else:
                speed = 'slow'
        else: 
            speed = "fast"
    elif axis == 'y':
        if circle[2] > slowrad:
            if circle[2] > stoprad:
                speed = 'stop'
            else:
                speed = "slow"
        else:
            speed = 'fast'
    return speed