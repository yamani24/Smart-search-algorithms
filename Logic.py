
from numpy import *
import copy
class Board:
    row=9
    col=9
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

     
    
    def print_Board(self,game_board):
     for row in game_board:
      for element in row:
        print(element, end=" ")
      print()
    
    
    ######################################
    
    def Next_step(self,gamme_board,i,j):
     if game_board[i+1][j]==1:  
       print("Possible states:")
       print("state :down")
       for i in range(8):
        for j in range(8):
         if game_board[i][j]==2 :
          while game_board[i+1][j] == 1: 
           game_board[i][j]=1  
           game_board[i+1][j]=2
           if i >= 8: 
               break
       self.print_Board(game_board) 
      
     if  game_board[i][j+1]==1:
       for i in range(8):
        for j in range(8):
         if game_board[i][j]==2 :
          if game_board[i][j+1]==1:
           while game_board[i][j+1] == 1:          
            game_board[i][j]=1  
            game_board[i][j+1]=2
            if j >= 8: 
               break 
       print("state right:")           
       self.print_Board(game_board)
      # self.print_Board(game_board)
     if game_board[i-1][j]==1:
       for i in range(8):
        for j in range(8):
         if game_board[i][j]==2 :
           if game_board[i-1][j] == 1:
            while game_board[i-1][j] == 1: 
             game_board[i][j]=1  
             game_board[i-1][j]=2
             i-=1
             if j >= 8: 
               break 
       print("state up:")       
       self.print_Board(game_board)   
     if game_board[i][j-1]==1:                 
       for i in range(8):
        for j in range(8):
         if game_board[i][j]==2 :
          while game_board[i][j-1] == 1: 
           game_board[i][j]=1  
           game_board[i][j-1]=2
           j-=1
           if j >= 8: 
             break 
       print("state left:")       
       self.print_Board(game_board)
     return [copy.deepcopy(gamme_board) for _ in range(4)]
       
      
 ###########################################################
    def can_move(self,game_board,i,j,x):  
      if x=="w":
       if game_board[i-1][j]==1:
        return True
       else:
        return False

      if x=="s":
       if game_board[i+1][j]==1:
        return True
       else:
        return False

      if x=="d":
       if game_board[i][j+1]==1:
        return True
       else:
        return False

      if x=="a":
       if game_board[i][j-1]==1:
        return True
       else:
        return False

      else:
       return False
      
     #####################################

    def check(self,game_board,i , j):
      if game_board[i+1][j]==22 or game_board[i-1][j]==22 or game_board[i][j+1]==22 or game_board[i][j-1]==22:
        return i,j
      else: 
        return  False  
    
    # def check(self, game_board, i, j):
    # # إذا كانت game_board هي كائن من نوع Board، يمكنك الوصول إلى المصفوفة 2D داخل الكائن كما يلي:
    #  board = game_board.board_matrix  # تأكد من أن `board_matrix` هي المصفوفة 2D داخل كائن `Board`
    
    # # الآن يمكنك استخدام board بدلاً من game_board:
    #  if board[i+1][j] == 22 or board[i-1][j] == 22 or board[i][j+1] == 22 or board[i][j-1] == 22:
    #     return i,j
    #  return False

    #######################################
    
    def move_s(self,game_board,x):
      if x=="s": 
        for i in range(8):
         for j in range(8):
          if game_board[i][j]==2 :
           while game_board[i+1][j] == 1: 
            game_board[i][j]=1  
            game_board[i+1][j]=2
            i+=1
            if i >= 8: 
               break
          #  self.print_Board(game_board)   
           ch=self.check(game_board,i,j)
           if ch==True:
             print("you win")
          #  else :
          #   print("try again:")
          #   x=input()
          #   use=Board()
          #   use.move(game_board,x ) 
      # players = Board()
      return  game_board[i][j] 
    
    ################################################
    
    def move_d(self,game_board,x):     
      if x=="d": 
      #  can=self.can_move(game_board,i,j,"d") 
      #  if can==True: 
        for i in range(8):
         for j in range(8):
          if game_board[i][j]==2 :
           while game_board[i][j+1] == 1: 
            game_board[i][j]=1  
            game_board[i][j+1]=2
            j+=1
            if j >= 8: 
               break 
          #  self.print_Board(game_board)   
           ch=self.check(game_board,i,j)
           if ch==True:
             print("you win")
          #  else :
            # print("try again:")
            # x=input()
            # use=Board()
            # use.move(game_board,x ) 
      #  else:
      #    print("you canot move it!") 
      playerd = Board()
      return  playerd
    
    #####################################################
    
    def move_w(self,game_board,x):                                           
      if x=="w":
      #  can=self.can_move(game_board,i,j,"w") 
      #  if can==True:
        for i in range(8):
         for j in range(8):
          if game_board[i][j]==2 :
           while game_board[i-1][j] == 1: 
            game_board[i][j]=1  
            game_board[i-1][j]=2
            i-=1
            if i>= 8: 
               break 
          #  self.print_Board(game_board)   
           ch=self.check(game_board,i,j)
           if ch==True:
             print("you win")
          #  else :
          #   print("try again:")
          #   x=input()
          #   use=Board()
          #   use.move(game_board,x ) 
      #  else:
      #    print("you canot move it!") 
      playerw = Board()
      return  playerw  
    
    ################################################
    
    def move_a(self,game_board,x):                 
      if x=="a":
      #  can=self.can_move(game_board,i,j,"a") 
       #if can==True:
        for i in range(8):
         for j in range(8):
          if game_board[i][j]==2 :
           while game_board[i][j-1] == 1: 
            game_board[i][j]=1  
            game_board[i][j-1]=2
            j-=1
            if j >= 8: 
               break 
          #  self.print_Board(game_board)   
           ch=self.check(game_board,i,j)
           if ch==True:
             print("you win")
          #  else :
          #   print("try again:")
          #   x=input()
          #   use=Board()
          #   use.move(game_board,x )      
      #  else:
      #    print("you canot move it!") 
      playera = Board()
      return  playera
     
      ##############################################
    def equal(matrix1, matrix2):
     if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False
      
     for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    
     return True
    

    ##############################################    
game_board =    ([0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0] ,
                 [0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0] ,
                 [0 , 1 , 1 , 2 , 1 , 1 , 1 , 1 , 0] ,
                 [0 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 0] ,
                 [0 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 0] ,
                 [0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0] ,
                 [0 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0] ,
                 [0 , 22 ,1 , 1 , 1 , 1 , 1 , 1 , 0] ,
                 [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
    )

# game_board1=copy.deepcopy(game_board)
# game_board2=copy.deepcopy(game_board)
# game_board3=copy.deepcopy(game_board)
# game_board4=copy.deepcopy(game_board)
    
# player1 = Board()
# player2= Board()
# player3 = Board()
# player4 = Board()
# print("copied Board") 
# player1.print_Board(game_board1)
# player1.Next_step(game_board1,"s")
# player2.Next_step(game_board2,"d")
# player3.Next_step(game_board3,"w")
# player4.Next_step(game_board4,"a")
# print("original Board:")
# player1.print_Board(game_board)