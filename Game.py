# from numpy import *
import copy
#from Algorithm import Algorithm
from Logic import Algorithm
from Logic import Board
class main(Board):
    game_board =([0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0] ,
                 [0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0] ,
                 [0 , 1 , 1 , 2 , 1 , 1 , 1 , 1 , 0] ,
                 [0 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 0] ,
                 [0 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 0] ,
                 [0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0] ,
                 [0 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0] ,
                 [0 , 22, 1 , 1 , 1 , 1 , 1 , 1 , 0] ,
                 [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
    )
    
    user =Algorithm()
    visited=[]
    # path = user.ucs(user.game_board, 3,2)
    # path = user.dfs_recursion(user.game_board, 3,2,visited)
    start_x, start_y = 2,3
    target_value = 22
    visited = set()  
    path = []  
    found = user.a_stare(game_board, start_x, start_y, target_value, visited, path)
    # user.print_Board(game_board)
    # if not found:
    #   print("Target not found in the matrix.")
 
        
    
      
     
     
           