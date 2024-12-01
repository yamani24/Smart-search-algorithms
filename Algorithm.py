from Logic import Board
import queue 

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
 
   ########################################################
   
    def heurestic_manh(x1,y1):
        return x1+y1
    
    def heurestic(self,game_board):
        temp=0
        for n in range(8):
            h=18
            temp=min(temp,self.heurestic_manh(2,5))
            if h!=18:
             temp+=h
        return temp     
    
    #######################################################
    
    def a_stare(self,game_board,begin_i,begin_j):
        visited = set() 
        parent = {} 
        q = queue.PriorityQueue()
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
                    heurestic=self.heurestic(game_board[carrent_i][carrent_j]) 
                    visited.add(n)
                    parent[n] = (carrent_i, carrent_j)
        print(heurestic)              
        return None
        
        
    
        
 