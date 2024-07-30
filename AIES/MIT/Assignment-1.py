import heapq

class Puzzle:
    def __init__(self, board, goal):
        self.board = board
        self.goal = goal
        self.n = len(board)
    
    def heuristic(self, state):
        """Calculate the Manhattan distance for a given state."""
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                if state[i][j] != 0:
                    x, y = divmod(state[i][j] - 1, self.n)
                    distance += abs(x - i) + abs(y - j)
        return distance
    
    def get_neighbors(self, state):
        """Generate all possible moves from the current state."""
        neighbors = []
        x, y = [(ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0][0]
        directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for dx, dy in directions:
            if 0 <= dx < self.n and 0 <= dy < self.n:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[dx][dy] = new_state[dx][dy], new_state[x][y]
                neighbors.append(new_state)
        return neighbors
    
    def a_star_search(self):
        """Perform the A* search to find the solution path."""
        start = self.board
        goal = self.goal
        
        # Priority queue to store frontier nodes
        frontier = []
        heapq.heappush(frontier, (0 + self.heuristic(start), 0, start))
        explored = set()
        parent_map = {}
        g_scores = {str(start): 0}
        
        while frontier:
            _, g, current = heapq.heappop(frontier)
            if current == goal:
                path = []
                while str(current) in parent_map:
                    path.append(current)
                    current = parent_map[str(current)]
                path.append(start)
                return path[::-1]
            
            explored.add(str(current))
            
            for neighbor in self.get_neighbors(current):
                new_g = g + 1
                if str(neighbor) not in explored or new_g < g_scores.get(str(neighbor), float('inf')):
                    g_scores[str(neighbor)] = new_g
                    f = new_g + self.heuristic(neighbor)
                    heapq.heappush(frontier, (f, new_g, neighbor))
                    parent_map[str(neighbor)] = current
        
        return None

def get_board_from_input():
    """Get board configuration from user input."""
    n = int(input("Enter the size of the board (e.g., 3 for a 3x3 board): "))
    print("Enter the board row by row, with each number separated by a space:")
    board = []
    for i in range(n):
        row = list(map(int, input().split()))
        board.append(row)
    return board

# Get initial board and goal board from user input
print("Enter the initial board configuration:")
initial_board = get_board_from_input()

print("Enter the goal board configuration:")
goal_board = get_board_from_input()

puzzle = Puzzle(initial_board, goal_board)
solution = puzzle.a_star_search()

if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
