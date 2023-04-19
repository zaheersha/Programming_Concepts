'''
A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people,
find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j
is set to 1 it means ith person knows jth person. Here M[i][i] will always be 0.
Note: Follow 0 based indexing.


Example 1:

Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0},
         {0 1 0}}
Output: 1
'''

def celebrity(M, n):
    #Initialization
    a= 0
    b=n-1

    while a<b:
        if(M[a][b] == 1):
            a+= 1
        else:
            b -=1

    for i in range(n):
        #Check if the person does not know any other person
        if((i != a)) and (M[a][i]==1 or M[i][a] == 0):
            return -1
    return a

print(celebrity([[0,1,0],[0,0,0],[0,1,0]],3))





