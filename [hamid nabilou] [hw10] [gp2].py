from random import randint

import numpy as np

from functools import reduce



def solver_python(grid):

    number = np.arange(1,10)

    p,j = np.where(grid == 0)

    if ( p.size == 0 ):

        return(True,grid)

    else:
        j = j[0]
        p = p[0]
        
        r = grid[p,:]
        C = grid[:,j]

        
        S = grid[(p // 3) * 3: ( 3 + ( p // 3 ) * 3 ),( j // 3 ) * 3:( 3 + ( j // 3 )* 3 ) ].reshape(9)

        

        Value = np.setdiff1d(number , reduce(np.union1d,(r,C,S)))

        grid_temp = np.copy(grid) 

        for value in Value:

            grid_temp[p,j] = value

            A = solver_python(grid_temp)

            if (A[0]):

                return(A)

        return(False,None)

    

result = np.array([[0,0,0,0,0,0,0,0,0],

                  [0,0,0,0,0,0,0,0,0],

                  [0,0,0,0,0,0,0,0,0],

                  [0,0,0,0,0,0,0,0,0],
    
                  [0,0,0,0,0,0,0,0,0],

                  [0,0,0,0,0,0,0,0,0],

                  [0,0,0,0,0,0,0,0,0],

                  [0,0,0,0,0,0,0,0,0],

                  [0,0,0,0,0,0,0,0,0]])



result[randint(0 , 9)][randint(0 , 9)] = randint(0 , 9)

result = solver_python(result)[1]




numberDelete = int(input("Enter the number of deleted ones: "))



for p in range (numberDelete):

    result[randint(0 , 9)][randint(0 , 9)] = 0

    
print (result)
