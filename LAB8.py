# ----------Task 1-------------------
import math

# Define a class to represent each node (city) in the graph
class CityNode:
    def __init__(self, city_name, cost_from_start=0, heuristic_cost=0):
        self.city_name = city_name               # The name of the city
        self.g_cost = cost_from_start            # Cost from the start node to this node
        self.h_cost = heuristic_cost             # Heuristic cost to reach the goal node
        self.f_cost = self.g_cost + self.h_cost  # Total cost (f = g + h)
        self.parent_node = None                  # Parent node in the optimal path

    def __repr__(self):
        return f"CityNode(city_name={self.city_name}, g_cost={self.g_cost}, h_cost={self.h_cost}, f_cost={self.f_cost})"

# A* algorithm implementation
def a_star_search(start_node, goal_node, get_neighbors, get_heuristic):
    open_set = []             # Nodes to be evaluated
    closed_set = set()        # Nodes already evaluated
    
    # Initialize the start node with costs
    start_node.g_cost = 0
    start_node.h_cost = get_heuristic(start_node.city_name)
    start_node.f_cost = start_node.g_cost + start_node.h_cost
    open_set.append(start_node)
    
    while open_set:
        # Select the node with the lowest f_cost
        current_node = min(open_set, key=lambda node: node.f_cost)
        open_set.remove(current_node)
        
        # If the goal is reached, reconstruct and return the path
        if current_node.city_name == goal_node.city_name:
            return reconstruct_path(current_node)
        
        closed_set.add(current_node.city_name)
        
        # Explore the neighbors of the current node
        for neighbor_name, travel_cost in get_neighbors(current_node.city_name):
            neighbor_node = CityNode(neighbor_name)
            neighbor_node.g_cost = current_node.g_cost + travel_cost
            neighbor_node.h_cost = get_heuristic(neighbor_node.city_name)
            neighbor_node.f_cost = neighbor_node.g_cost + neighbor_node.h_cost
            neighbor_node.parent_node = current_node
            
            if neighbor_node.city_name in closed_set:
                if neighbor_node.g_cost >= current_node.g_cost + travel_cost:
                    continue
            
            # If the neighbor is already in the open set, check if we have found a better path
            existing_node = next((node for node in open_set if node.city_name == neighbor_node.city_name), None)
            if existing_node:
                if neighbor_node.g_cost >= existing_node.g_cost:
                    continue
                open_set.remove(existing_node)
            
            # Add the neighbor to the open set
            open_set.append(neighbor_node)
    
    return None  # No path found

# Reconstruct the path by following parent nodes
def reconstruct_path(node):
    path = []
    while node:
        path.append(node.city_name)
        node = node.parent_node
    path.reverse()
    return path

# Define the neighbors (connections between cities and their costs)
def get_neighbors(city_name):
    city_connections = {
        'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
        'Zerind': [('Oradea', 71)],
        'Oradea': [('Sibiu', 151)],
        'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80)],
        'Timisoara': [('Lugoj', 111)],
        'Lugoj': [('Mehadia', 70)],
        'Mehadia': [('Drobeta', 75)],
        'Drobeta': [('Craiova', 120)],
        'Craiova': [('Rimnicu Vilcea', 146)],
        'Rimnicu Vilcea': [('Pitesti', 97)],
        'Pitesti': [('Bucharest', 101)],
        'Fagaras': [('Bucharest', 211)],
        'Bucharest': []
    }
    return city_connections.get(city_name, [])

# Define the heuristic function based on straight-line distances to Bucharest
def get_heuristic(city_name):
    estimated_distances = {
        'Arad': 366,
        'Zerind': 374,
        'Oradea': 380,
        'Sibiu': 253,
        'Timisoara': 329,
        'Lugoj': 244,
        'Mehadia': 241,
        'Drobeta': 242,
        'Craiova': 160,
        'Rimnicu Vilcea': 193,
        'Pitesti': 98,
        'Fagaras': 176,
        'Bucharest': 0
    }
    return estimated_distances.get(city_name, float('inf'))

# Initialize start and goal nodes
start_node = CityNode('Arad')
goal_node = CityNode('Bucharest')

# Perform A* search and print the result
found_path = a_star_search(start_node, goal_node, get_neighbors, get_heuristic)
print("Path found:", found_path)

# -----------------Task 2-----------------
# Define a class to represent each node (city) in the graph
class CityNode:
    def __init__(self, city_name, heuristic_cost=0):
        self.city_name = city_name               # The name of the city
        self.h_cost = heuristic_cost             # Heuristic cost to reach the goal node
        self.f_cost = self.h_cost                # Total cost (f = h) in Greedy Best-First Search
        self.parent_node = None                  # Parent node in the optimal path

    def __repr__(self):
        return f"CityNode(city_name={self.city_name}, h_cost={self.h_cost}, f_cost={self.f_cost})"

# Greedy Best-First Search algorithm implementation
def greedy_best_first_search(start_node, goal_node, get_neighbors, get_heuristic):
    open_set = []             # Nodes to be evaluated
    closed_set = set()        # Nodes already evaluated
    
    # Initialize the start node with heuristic cost
    start_node.h_cost = get_heuristic(start_node.city_name)
    start_node.f_cost = start_node.h_cost
    open_set.append(start_node)
    
    while open_set:
        # Select the node with the lowest heuristic cost
        current_node = min(open_set, key=lambda node: node.f_cost)
        open_set.remove(current_node)
        
        # If the goal is reached, reconstruct and return the path
        if current_node.city_name == goal_node.city_name:
            return reconstruct_path(current_node)
        
        closed_set.add(current_node.city_name)
        
        # Explore the neighbors of the current node
        for neighbor_name, _ in get_neighbors(current_node.city_name):
            neighbor_node = CityNode(neighbor_name)
            neighbor_node.h_cost = get_heuristic(neighbor_node.city_name)
            neighbor_node.f_cost = neighbor_node.h_cost
            neighbor_node.parent_node = current_node
            
            if neighbor_node.city_name in closed_set:
                continue
            
            # If the neighbor is already in the open set, skip adding it again
            existing_node = next((node for node in open_set if node.city_name == neighbor_node.city_name), None)
            if existing_node:
                continue
            
            # Add the neighbor to the open set
            open_set.append(neighbor_node)
    
    return None  # No path found

# Reconstruct the path by following parent nodes
def reconstruct_path(node):
    path = []
    while node:
        path.append(node.city_name)
        node = node.parent_node
    path.reverse()
    return path

# Define the neighbors (connections between cities)
def get_neighbors(city_name):
    city_connections = {
        'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
        'Zerind': [('Oradea', 71)],
        'Oradea': [('Sibiu', 151)],
        'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80)],
        'Timisoara': [('Lugoj', 111)],
        'Lugoj': [('Mehadia', 70)],
        'Mehadia': [('Drobeta', 75)],
        'Drobeta': [('Craiova', 120)],
        'Craiova': [('Rimnicu Vilcea', 146)],
        'Rimnicu Vilcea': [('Pitesti', 97)],
        'Pitesti': [('Bucharest', 101)],
        'Fagaras': [('Bucharest', 211)],
        'Bucharest': []
    }
    return city_connections.get(city_name, [])

# Define the heuristic function based on straight-line distances to Bucharest
def get_heuristic(city_name):
    estimated_distances = {
        'Arad': 366,
        'Zerind': 374,
        'Oradea': 380,
        'Sibiu': 253,
        'Timisoara': 329,
        'Lugoj': 244,
        'Mehadia': 241,
        'Drobeta': 242,
        'Craiova': 160,
        'Rimnicu Vilcea': 193,
        'Pitesti': 98,
        'Fagaras': 176,
        'Bucharest': 0
    }
    return estimated_distances.get(city_name, float('inf'))

# Initialize start and goal nodes
start_node = CityNode('Arad')
goal_node = CityNode('Bucharest')

# Perform Greedy Best-First Search and print the result
found_path = greedy_best_first_search(start_node, goal_node, get_neighbors, get_heuristic)
print("Path found:", found_path)



# ----- Task 3
import heapq

# Define the goal state for the 8-puzzle
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Node class to represent each state of the puzzle
class PuzzleNode:
    def __init__(self, puzzle, move_cost=0, heuristic_cost=0):
        self.puzzle = puzzle                      # The current state of the puzzle
        self.g_cost = move_cost                   # Cost to reach this state
        self.h_cost = heuristic_cost              # Heuristic cost to reach the goal state
        self.f_cost = self.g_cost + self.h_cost   # Total cost (f = g + h)
        self.parent_node = None                   # Parent node in the solution path

    def __lt__(self, other):
        return self.f_cost < other.f_cost

# Calculate the heuristic (number of misplaced tiles)
def calculate_heuristic(puzzle):
    misplaced_tiles = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0 and puzzle[i][j] != goal_state[i][j]:
                misplaced_tiles += 1
    return misplaced_tiles

# Generate new states from possible moves (up, down, left, right)
def generate_new_states(puzzle):
    new_states = []
    zero_pos = [(row_i, col_i) for row_i in range(3) for col_i in range(3) if puzzle[row_i][col_i] == 0][0]
    row, col = zero_pos

    # Possible moves
    move_positions = [(row-1, col, "Up"), (row+1, col, "Down"), (row, col-1, "Left"), (row, col+1, "Right")]

    for new_row, new_col, move in move_positions:
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_puzzle = [row[:] for row in puzzle]
            new_puzzle[row][col], new_puzzle[new_row][new_col] = new_puzzle[new_row][new_col], new_puzzle[row][col]
            new_states.append((new_puzzle, move))

    return new_states

# A* search algorithm to solve the 8-puzzle problem
def solve_8_puzzle(start_puzzle):
    open_set = []
    closed_set = set()

    start_node = PuzzleNode(start_puzzle, move_cost=0, heuristic_cost=calculate_heuristic(start_puzzle))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.puzzle == goal_state:
            return reconstruct_puzzle_path(current_node)

        closed_set.add(tuple(tuple(row) for row in current_node.puzzle))

        for new_puzzle, move in generate_new_states(current_node.puzzle):
            if tuple(tuple(row) for row in new_puzzle) in closed_set:
                continue

            new_node = PuzzleNode(new_puzzle, move_cost=current_node.g_cost + 1, heuristic_cost=calculate_heuristic(new_puzzle))
            new_node.parent_node = current_node
            heapq.heappush(open_set, new_node)

    return None  # No solution found

# Reconstruct the path of moves by following parent nodes
def reconstruct_puzzle_path(node):
    path = []
    while node:
        path.append((node.puzzle, node.f_cost))
        node = node.parent_node
    path.reverse()
    return path

# Initial state of the puzzle
initial_puzzle = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

# Solve the puzzle and print the solution path
solution_path = solve_8_puzzle(initial_puzzle)
for puzzle, cost in solution_path:
    for row in puzzle:
        print(row)
    print(f"Total cost: {cost}\n")
