from common.node import Node
from common.problem import Problems
from common.utils import expand, reconstruct_path

# Hill-Climbing Algorithm
# Pseudo code

# function HILL_CLIMBING(problem) returns a solution path or failure
# start_node ← NODE(STATE=problem.initial, PARENT=None, ACTION=None, PATH_COST=0, HEURISTIC=problem.heuristics[problem.initial])
# current_node ← start_node
# while true do
#     if problem.IS_GOAL(current_node.STATE) then
#         return RECONSTRUCT_PATH(current_node)  // Return the path to the goal
#     neighbors ← EXPAND(problem, current_node)  // Expand the current node to find neighbors
#     if neighbors is empty then
#         return failure  // Return None if there are no neighbors (stuck)
#     next_node ← MIN(neighbors, HEURISTIC)  // Find the neighbor with the lowest heuristic value
#     if next_node.HEURISTIC ≥ current_node.HEURISTIC then
#         return failure  // Return None if the next node has a higher or equal heuristic value (stuck)
#     current_node ← next_node  // Move to the next node


def hill_climbing(problem):
    """Hill-Climbing Search (HC)

    Args:
        problem (Problems): The problem instance which includes the initial state, goal state, and other problem-specific methods.

    Returns:
        list or None: A list representing the path from the initial state to the goal state if a path is found, otherwise None.
    """
    start_node = Node(
        state=problem.initial,
        parent=None,
        action=None,
        path_cost=0,
        heuristic=problem.heuristics[problem.initial],
    )
    current_node = start_node

    while True:
        # If the current node is the goal, return the path
        if problem.is_goal(current_node.state):
            return reconstruct_path(current_node)

        # Expand the current node to find neighbors
        neighbors = list(expand(problem, current_node))

        # If there are no neighbors, return None (stuck)
        if not neighbors:
            return None

        # Find the neighbor with the lowest heuristic value
        next_node = min(neighbors, key=lambda node: node.heuristic)

        # If the next node has a higher or equal heuristic value, return None (stuck)
        if next_node.heuristic >= current_node.heuristic:
            return None

        # Move to the next node
        current_node = next_node
