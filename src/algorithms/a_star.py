import heapq
from common.problem import Problems
from common.node import Node
from common.utils import expand, reconstruct_path

# Graph Search A* (A*)
# Pseudo code

# function A_STAR_SEARCH(problem) returns a solution path or failure
#     node ← NODE(STATE=problem.initial, PATH_COST=0, HEURISTIC=problem.heuristics[problem.initial])
#     frontier ← a priority queue ordered by node.PATH_COST + node.HEURISTIC, with node as an element
#     reached ← a dictionary with key problem.initial and value node

#     while frontier is not empty do
#         _, current_node ← POP(frontier)

#         if problem.IS_GOAL(current_node.STATE) then
#             return RECONSTRUCT_PATH(current_node)

#         for each child in EXPAND(problem, current_node) do
#             if child.STATE not in reached or child.PATH_COST < reached[child.STATE].PATH_COST then
#                 reached[child.STATE] ← child
#                 PUSH(frontier, (child.PATH_COST + child.HEURISTIC, child))
#     return failure


def a_star_search(problem):
    """Graph Search A* Algorithm

    This function implements the A* search algorithm to find the optimal path from the initial state
    to the goal state of a given problem. A* uses a heuristic to guide the search, aiming to minimize
    the total estimated cost (path cost + heuristic).

    Args:
        problem (Problems): The problem to solve. The problem must provide:
            - `initial`: The initial state of the problem.
            - `goal`: The goal state of the problem.
            - `is_goal(state)`: A method to check if a given state is the goal state.
            - `heuristics`: A list of heuristic values for each state.

    Returns:
        list or None: The path from the initial state to the goal state if a path is found.
        The path is represented as a list of states. If no path is found, the function returns None.
    """
    # Initialize the start node with the initial state, no parent, no action, zero path cost, and the heuristic value.
    start_node = Node(
        state=problem.initial,
        parent=None,
        action=None,
        path_cost=0,
        heuristic=problem.heuristics[problem.initial],
    )

    # Initialize the priority queue (frontier) with the start node. The priority is the sum of the path cost and the heuristic.
    frontier = [(start_node.path_cost + start_node.heuristic, start_node)]

    # Initialize the reached dictionary to keep track of the best known path to each state.
    reached = {problem.initial: start_node}

    # Continue searching while there are nodes to explore in the frontier.
    while frontier:
        # Pop the node with the lowest estimated total cost (path cost + heuristic) from the priority queue.
        _, current_node = heapq.heappop(frontier)

        # Check if the current node's state is the goal state.
        if problem.is_goal(current_node.state):
            return reconstruct_path(current_node)

        # Expand the current node to generate its children.
        for child in expand(problem=problem, node=current_node):
            # If the child state is not reached yet, or the new path cost is lower than the previously known path cost:
            if (
                child.state not in reached
                or child.path_cost < reached[child.state].path_cost
            ):
                # Update the reached dictionary with the new child node.
                reached[child.state] = child
                # Push the child node to the priority queue with its estimated total cost.
                heapq.heappush(frontier, (child.path_cost + child.heuristic, child))

    # Return None if no path is found to the goal state.
    return None
