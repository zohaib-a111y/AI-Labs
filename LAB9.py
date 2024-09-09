# ------ task 1
# max_min function that returns the value of the root node in task 1
def max_min(current_node, level, isMaximizingPlayer):
    # If this is a leaf node, return its value
    if level == 0 or not current_node.sub_nodes:
        return current_node.node_value
    
    if isMaximizingPlayer:
        highestValue = float('-inf')
        for sub_node in current_node.sub_nodes:
            evaluation = max_min(sub_node, level - 1, False)
            highestValue = max(highestValue, evaluation)
        return highestValue
    else:
        lowestValue = float('inf')
        for sub_node in current_node.sub_nodes:
            evaluation = max_min(sub_node, level - 1, True)
            lowestValue = min(lowestValue, evaluation)
        return lowestValue


# ------ task 2
# Function that implements alpha-beta pruning
def max_min_alpha_beta(current_node, level, alpha, beta, isMaximizingPlayer):
    # If this is a leaf node, return its value
    if level == 0 or not current_node.sub_nodes:
        return current_node.node_value
    
    if isMaximizingPlayer:
        highestValue = float('-inf')
        for sub_node in current_node.sub_nodes:
            evaluation = max_min_alpha_beta(sub_node, level - 1, alpha, beta, False)
            highestValue = max(highestValue, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break  # Beta cutoff
        return highestValue
    else:
        lowestValue = float('inf')
        for sub_node in current_node.sub_nodes:
            evaluation = max_min_alpha_beta(sub_node, level - 1, alpha, beta, True)
            lowestValue = min(lowestValue, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break  # Alpha cutoff
        return lowestValue


# -------- Creating a class to represent tree nodes and their children, usable in both tasks
class TreeNode:
    def __init__(self, node_value=None, sub_nodes=None):
        self.node_value = node_value  # Value of the node (used for leaf nodes)
        self.sub_nodes = sub_nodes if sub_nodes is not None else []  # List of child nodes

# Creating the leaf nodes
leaf_A = TreeNode(node_value=3)
leaf_B = TreeNode(node_value=5)
leaf_C = TreeNode(node_value=6)
leaf_D = TreeNode(node_value=9)

# Creating intermediate nodes
node_1 = TreeNode(sub_nodes=[leaf_A, leaf_B])
node_2 = TreeNode(sub_nodes=[leaf_C, leaf_D])
node_3 = TreeNode(sub_nodes=[leaf_A, leaf_B])  # Reusing leaf_A and leaf_B
node_4 = TreeNode(sub_nodes=[leaf_C, leaf_D])  # Reusing leaf_C and leaf_D

# Creating the higher-level nodes
node_X = TreeNode(sub_nodes=[node_1, node_2])
node_Y = TreeNode(sub_nodes=[node_3, node_4])

# Creating the root node
root_node = TreeNode(sub_nodes=[node_X, node_Y])

# -------- Running Max-Min Algorithm
max_min_value = max_min(root_node, level=3, isMaximizingPlayer=True)
print("Max-Min Value:", max_min_value)

# Creating the leaf nodes for alpha-beta pruning
# *** You can also reuse the nodes above by commenting out the code from lines 85 to 105
leaf_A = TreeNode(node_value=3)
leaf_B = TreeNode(node_value=5)
leaf_C = TreeNode(node_value=6)
leaf_D = TreeNode(node_value=9)
leaf_E = TreeNode(node_value=11)
leaf_F = TreeNode(node_value=14)
leaf_G = TreeNode(node_value=16)
leaf_H = TreeNode(node_value=21)

# Creating intermediate nodes
node_1 = TreeNode(sub_nodes=[leaf_A, leaf_B])
node_2 = TreeNode(sub_nodes=[leaf_C, leaf_D])
node_3 = TreeNode(sub_nodes=[leaf_E, leaf_F])  
node_4 = TreeNode(sub_nodes=[leaf_G, leaf_H])  

# Creating the higher-level nodes
node_X = TreeNode(sub_nodes=[node_1, node_2])
node_Y = TreeNode(sub_nodes=[node_3, node_4])

# Creating the root node
root_node = TreeNode(sub_nodes=[node_X, node_Y])

# *-------- Running Max-Min with Alpha-Beta Pruning
max_min_ab_value = max_min_alpha_beta(root_node, level=3, alpha=float('-inf'), beta=float('inf'), isMaximizingPlayer=True)
print("Max-Min with Alpha-Beta Pruning Value:", max_min_ab_value)
