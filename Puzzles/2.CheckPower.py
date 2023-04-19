# Given two positive numbers X and Y, check if Y is a power of X or not.

# Input:
# X = 2, Y = 8
# Output:
# 1
# Explanation:
# 2^3 is equal to 8.

#Try powering the the smallest number and check if it is equal to the larger one

def isPower(X,Y):

    if (X==1):
        if(Y==1):
            return 1
        else:
            return 0

    pow = 1
    while (pow<Y):
        pow = pow * X

    if(pow == Y):
        return 1
    else:
        return 0

print(isPower(2,8))