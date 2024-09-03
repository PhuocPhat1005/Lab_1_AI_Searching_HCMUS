import heapq
from common.node import Node
from common.utils import expand, reconstruct_path

# Uniformed Cost Search (UCS)
# Pseudo code

# function UNIFORM_COST_SEARCH(problem) returns a solution path or failure
#     start_node ← Node(state=problem.initial, parent=None, action=None, path_cost=0)
#     frontier ← priority queue ordered by PATH_COST, initially containing (0, start_node)
#     reached ← dictionary with key problem.initial and value start_node
#     while frontier is not empty do
#         _, current_node ← heappop(frontier)  // Remove the node with the lowest PATH_COST
#         if problem.is_goal(current_node.state) then
#             return reconstruct_path(current_node)  // Return the path to the goal
#         for each child in expand(problem, current_node) do
#             if child.state is not in reached or child.path_cost < reached[child.state].path_cost then
#                 reached[child.state] ← child  // Update reached with the new lower PATH_COST
#                 heappush(frontier, (child.path_cost, child))  // Add the child to the frontier
#     return None  // Return None if no path to the goal is found


def ucs(problem):
    """Uniformed Cost Search (UCS)

    Args:
        problem (Problems): The problem instance which includes the initial state, goal state, adjacency_matrix, and heuristics

    Returns:
        list: A list representing the path from the initial state to the goal state if a path is found, otherwise None.
    """

    # Create the start node with initial state, no parent, no action, and a path cost of 0.
    start_node = Node(state=problem.initial, parent=None, action=None, path_cost=0)
    # Initialize the frontier as a priority queue ordered by path cost, starting with the initial node.
    frontier = [(0, start_node)]
    # The reached dictionary keeps track of the best path cost to reach each state.
    reached = {problem.initial: start_node}

    # Loop until the frontier is empty.
    while frontier:
        # Pop the node with the lowest path cost from the frontier.
        _, current_node = heapq.heappop(frontier)

        # If the current node is the goal state, reconstruct and return the path.
        if problem.is_goal(current_node.state):
            return reconstruct_path(current_node)

        # Expand the current node to generate its children.
        for child in expand(problem=problem, node=current_node):
            # If the child state has not been reached yet or if the new path cost is lower than the previously known path cost to this state.
            if (
                child.state not in reached
                or child.path_cost < reached[child.state].path_cost
            ):
                # Update the reached dictionary with the new lower path cost for this state.
                reached[child.state] = child
                # Add the child to the frontier with its path cost as the priority.
                heapq.heappush(frontier, (child.path_cost, child))

    # If the goal state is not reached and the frontier is empty, return None indicating failure.
    return None
