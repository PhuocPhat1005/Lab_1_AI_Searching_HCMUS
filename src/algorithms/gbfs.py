from common.node import Node
from common.utils import expand, reconstruct_path
from common.problem import Problems
import heapq


# Greedy Best First Search (GBFS)
# Pseudo - code

# function GREEDY-BEST-FIRST-SEARCH(problem) returns a solution path or failure
#     node ← Node(state=problem.initial, parent=None, action=None, path_cost=0, heuristic=problem.heuristics[problem.initial])
#     frontier ← a priority queue ordered by heuristic, with node as an element
#     reached ← a dictionary with key problem.initial and value node

#     while frontier is not empty do
#         _, current_node ← POP(frontier)

#         if problem.is_goal(current_node.state) then
#             return RECONSTRUCT-PATH(current_node)

#         for each child in EXPAND(problem, current_node) do
#             if child.state not in reached or child.heuristic < reached[child.state].heuristic then
#                 reached[child.state] ← child
#                 ADD (child.heuristic, child) to frontier

#     return failure


def gbfs(problem):
    """Greedy Best - First Search (GBFS)

    Args:
        problem (Problems): The problem instance which includes the initial state, goal state, and other problem-specific methods.

    Returns:
        list: A list representing the path from the initial state to the goal state if a path is found, otherwise None.
    """
    # Create the start node with initial state, no parent, no action, and a path cost of 0.
    start_node = Node(
        state=problem.initial,
        parent=None,
        action=None,
        path_cost=0,
        heuristic=problem.heuristics[problem.initial],
    )
    # Initialize the frontier as a priority queue ordered by heuristic, starting with the initial node.
    frontier = [(start_node.heuristic, start_node)]

    # The reached dictionary keeps track of the best heuristic to reach each state.
    reached = {problem.initial: start_node}

    # Loop until the frontier is empty.
    while frontier:
        # Pop the node with the lowest heuristic value from the frontier.
        _, current_node = heapq.heappop(frontier)

        # If the current node is the goal state, reconstruct and return the path.
        if problem.is_goal(current_node.state):
            return reconstruct_path(current_node)

        # Expand the current node to generate its children.
        for child in expand(problem=problem, node=current_node):
            # If the child state has not been reached yet or if the new heuristic is lower than the previously known heuristic to this state.
            if (
                child.state not in reached
                or child.heuristic < reached[child.state].heuristic
            ):
                # Update the reached dictionary with the new lower heuristic for this state.
                reached[child.state] = child
                # Add the child to the frontier with its heuristic as the priority.
                heapq.heappush(frontier, (child.heuristic, child))

    # If the goal state is not reached and the frontier is empty, return None indicating failure.
    return None
