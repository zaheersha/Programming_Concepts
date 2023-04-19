# Calculate the angle between hour hand and minute hand.
#
# Note: There can be two angles between hands, we need to
# print minimum of two. Also, we need to print floor of final
# result angle. For example, if the final angle is 10.61, we need to print 10.

# Input:
# H = 9 , M = 0
# Output:
# 90

def getAngle(H, M):

    if H==12:
        H=0
    if M==60:
        M=0

    hourAngle = 0.5*(H*60+M)
    minAngle = 6*M

    angle = abs(hourAngle-minAngle)

    if(angle>180):
        angle=int(360-angle)
    else:
        angle=int(angle)

    return angle


print(getAngle(8,19))


