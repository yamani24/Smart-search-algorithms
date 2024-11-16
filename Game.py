from numpy import *
import copy
from Algorithm import Algorithm
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
    print("user.dfs")
    # print("enter one key a,s,d,w:")
    # x=input()
    visited=[]
    user.dfs(game_board,3,2, visited)
    # path = user.bfs(user.game_board, 3,2)
    # if path:
    #     print("Path found:", path)
    # else:
    #     print("No path found")   
        
    
      
     
     
           