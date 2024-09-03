from common.node import Node
from common.utils import expand, reconstruct_path
from common.frontier import QueueFrontier


# Breath - First Search (BFS) --> first visited - first explored
# Pseudo code

# function BFS(problem) returns a solution path or failure
#     node ← NODE(STATE=problem.initial)
#     if problem.IS-GOAL(node.STATE) then
#         return RECONSTRUCT-PATH(node)
#     frontier ← QueueFrontier()
#     frontier.add(node)
#     reached ← set containing problem.initial
#     while not frontier.empty() do
#         node ← frontier.remove()
#         for each child in EXPAND(problem, node) do
#             if problem.IS-GOAL(child.STATE) then
#                 return RECONSTRUCT-PATH(child)
#             if child.STATE not in reached and not frontier.contains_state(child.STATE) then
#                 add child.STATE to reached
#                 frontier.add(child)
#     return failure


def bfs(problem):
    """Breadth-First Search Algorithm

    Args:
        problem (Problem): The problem to solve, which includes the initial state, goal state, and state transitions.

    Returns:
        list or None: The path from the initial state to the goal state, or None if no path is found.
    """
    # Initialize the initial node with the initial state of the problem
    node = Node(state=problem.initial)

    # Check if the initial state is the goal state
    if problem.is_goal(node.state):
        return reconstruct_path(node)

    # Initialize the frontier using a queue and add the initial node
    frontier = QueueFrontier()
    frontier.add(node)

    # Initialize the reached set with the initial state
    reached = {problem.initial}

    # Continue searching while there are nodes to explore
    while not frontier.empty():
        # Remove a node from the frontier (FIFO)
        node = frontier.remove()

        # Expand the node to generate its children
        for child in expand(problem=problem, node=node):
            s = child.state

            # If the child state is the goal state, return the reconstructed path
            if problem.is_goal(s):
                return reconstruct_path(child)

            # If the child state has not been reached and is not in the frontier
            if s not in reached and not frontier.contains_state(s):
                # Add the child state to the reached set
                reached.add(s)
                # Add the child node to the frontier
                frontier.add(child)
    # Return None if no solution is found
    return None
