from Logic import Board
import queue 
class Algorithm(Board):
    def bfs(self,game_board,begin_i,begin_j):
        print("dfs is called")
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
        x, y = current_state  
        visited.append(current_state)
        if self.check(game_board, x, y): 
            path = []
            while current_state is not None:
                path.append(current_state)  
                current_state = parent_map.get(current_state)  
            path.reverse() 
            print(path)
            return path
        if x + 1 < len(game_board) and game_board[x + 1][y] == 1 and (x + 1, y) not in visited:
            stack.append((x + 1, y))  
            parent_map[(x + 1, y)] = (x, y) 
        if x - 1 >= 0 and game_board[x - 1][y] == 1 and (x - 1, y) not in visited:
            stack.append((x - 1, y))
            parent_map[(x - 1, y)] = (x, y)
        if y + 1 < len(game_board[0]) and game_board[x][y + 1] == 1 and (x, y + 1) not in visited:
            stack.append((x, y + 1))
            parent_map[(x, y + 1)] = (x, y)
        if y - 1 >= 0 and game_board[x][y - 1] == 1 and (x, y - 1) not in visited:
            stack.append((x, y - 1))
            parent_map[(x, y - 1)] = (x, y)

     print("No path found")
     return []

