# Given two lists V1 and V2 of sizes n and m respectively. Return the list of elements
# common to both the lists and return the list in sorted order. Duplicates may be there in the output list.
#
# Example:
#
# Input:
# n = 5
# v1[] = {3, 4, 2, 2, 4}
# m = 4
# v2[] = {3, 2, 2, 7,2}
# Output:
# 2 2 3
# Explanation:
# The common elements in sorted order are {2 2 3}

#Dictionary  2:2 3: 1

def comEl(v1, v2):
    d=dict()
    d1=dict()

    for i in v1:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for i in v2:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1

    ans = []
    for i in sorted(d):
        if i in d1:
            #       [2] *  2 = [2][2]
            ans += [i]*min(d[i], d1[i])
    return ans

print(comEl([2,3,2,6,4,1], [4,8,2,1,9]))
