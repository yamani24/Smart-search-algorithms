from numpy import *
import copy
from Logic import Board
class main(Board):
    game_board =([0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0] ,
                 [0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0] ,
                 [0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0] ,
                 [0 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 0] ,
                 [0 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 0] ,
                 [0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0] ,
                 [0 , 1 , 1 , 1 , 2 , 1 , 1 , 0 , 0] ,
                 [0 , 22, 1 , 1 , 1 , 1 , 1 , 1 , 0] ,
                 [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
    )
    
    user =Board()
    print("enter one key a,s,d,w:")
    x=input()
    user.move(game_board,x)
    
        
    
      
     
     
           