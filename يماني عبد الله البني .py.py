
from numpy import *
import copy
from Algorithm import Algorithm
from Logic import Board
import queue 
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
      return  game_board[i][j]
    
    ################################################
    
    def move_d(self,game_board,x):     
      if x=="d": 
        for i in range(8):
         for j in range(8):
          if game_board[i][j]==2 :
           while game_board[i][j+1] == 1: 
            game_board[i][j]=1  
            game_board[i][j+1]=2
            j+=1
            if j >= 8: 
               break 
           self.print_Board(game_board)   
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
      
      return  game_board[i][j] 
    
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
      # playerw = Board()
      return  game_board[i][j] 
    
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
      
      return  game_board[i][j] 
     
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


class Algorithm(Board):
    
    def bfs(self,game_board,begin_i,begin_j):
        print("bfs is called")
        visited = set() 
        parent = {} 
        q = queue.Queue()  
        q.put((begin_i, begin_j))   
        parent[(begin_i, begin_j)] = None 
        while not q.empty():
            carrent_i,carrent_j=q.get()
            visited.add((begin_i, begin_j))
            parent[(begin_i, begin_j)] = None
            if game_board[begin_i][begin_j] is self. check(game_board,carrent_i,carrent_j):
                goal_i, goal_j=self. check(self,game_board,carrent_i,carrent_j)
                return self.reconstruct_path(parent, (goal_i, goal_j))
            Next =[self. Next_step (game_board,carrent_i,carrent_j) ] 
            for n in range (len(Next)) :
                if n not in visited: 
                    q.put(n) 
                    visited.add(n)
                    parent[n] = (carrent_i, carrent_j)
        return None 
    ######################################################
    
    def reconstruct_path(self, parent, goal):
        path = []
        current = goal
        while current is not None:
            path.append(current)  
            current = parent[current]  
        path.reverse()  
        return path
    
    #############################################################
     
    def dfs(self, game_board, i, j, visited):
     print("dfs is called")
     stack = [(i, j)] 
     parent_map = {} 
     
     while stack:
        current_state = stack.pop()
        (x, y) = current_state  
        visited.append(current_state)
        if self.check(game_board, x, y): 
            path = []
            while current_state is not None:
                path.append(current_state)  
                current_state = parent_map.get(current_state)  
            path.reverse() 
            print(path)
            # def print_Board(self,game_board):
            for row in game_board:
              for element in row:
                print(element, end=" ")
            print()
            return path
        if x + 1 < len(game_board) and game_board[x + 1][y] == 1 and (x + 1, y) not in visited:
            (i,j)=(x,y)
            while game_board[x + 1][y] == 1:
                x+=1
            stack.append((x , y))  
            parent_map[(x, y)] = (i,j) 
        if x - 1 > 0 and game_board[x - 1][y] == 1 and (x - 1, y) not in visited:
            (i,j)=(x,y)
            while game_board[x - 1][y] == 1:
                x-=1
            stack.append((x , y))
            parent_map[(x , y)] = (i,j)
        if y + 1 < len(game_board[0]) and game_board[x][y + 1] == 1 and (x, y + 1) not in visited:
            (i,j)=(x,y)
            while game_board[x ][y+1] == 1:
                y+=1 
            stack.append((x, y ))
            parent_map[(x, y )] = (i,j)
        if y - 1 > 0 and game_board[x][y - 1] == 1 and (x, y - 1) not in visited:
            (i,j)=(x,y)
            while game_board[x][y-1] == 1:
                y-=1
            stack.append((x, ))
            parent_map[(x, y )] = (i,j)
     print("No path found")
     return []
 
    ####################################################
    
    def dfs_recursion(self,game_board, x, y, target, visited, path):
     if x < 0 or y < 0 or x >= len(game_board) or y >= len(game_board[0]):
        return False
     if (x, y) in visited:
        return False
     path.append((x, y))
     
     if game_board[x][y] == target:
        print(f"Found target at {x}, {y}")
        print(f"Path: {path}")
        return True
    
     visited.add((x, y))
     if game_board[x][y] == 2:
        print(f"Moved element at ({x}, {y}) with value 2")
     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
     for dx, dy in directions:
        if self.dfs_recursion(game_board, x + dx, y + dy, target, visited, path):
            return True
     path.pop()
     for row in game_board:
      for element in row:
        print(element, end=" ")
      print()
     return False    
    
    ####################################################
    
    def Dfs(self,game_board, x, y, target, visited, path):
        if x < 0 or y < 0 or x >= len(game_board) or y >= len(game_board[0]):
          return False
        if (x, y) in visited:
          return False
        path.append((x, y))
        if game_board[x][y] == target:
          print(f"Found target at {x}, {y}")
          print(f"Path: {path}")
          return True
        visited.add((x, y))
        if game_board[x][y]==1:
            Next =[self. Next_step (game_board,x,y) ] 
            for n in range (len(Next)) :
                if n not in visited:
                    self.Dfs(game_board,x,y,target,visited,path) 
        self.print_Board(game_board)    
    
    ####################################################
                
    def ucs(self,game_board,begin_i,begin_j):
      visited = set() 
      parent = {} 
      q = queue.PriorityQueue()
      q.put((begin_i, begin_j))   
      parent[(begin_i, begin_j)] = None  
      cost=0
    #   print(cost)  
      while not q.empty():
            carrent_i,carrent_j=q.get()
            visited.add((begin_i, begin_j))
            parent[(begin_i, begin_j)] = None
            if game_board[begin_i][begin_j] is self. check(game_board,carrent_i,carrent_j):
                goal_i, goal_j=self. check(self,game_board,carrent_i,carrent_j)
                return self.reconstruct_path(parent, (goal_i, goal_j))
            Next =[self. Next_step (game_board,carrent_i,carrent_j) ] 
            for n in range (len(Next)) :
                if n not in visited: 
                    q.put(n)
                    cost+=1 
                    visited.add(n)
                    parent[n] = (carrent_i, carrent_j)
      print(cost)              
      return None

######################################################### 

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
    found = user.dfs_recursion(game_board, start_x, start_y, target_value, visited, path)
    # user.print_Board(game_board)
    # if not found:
    #   print("Target not found in the matrix.")
 
        
    
      
     
     
           