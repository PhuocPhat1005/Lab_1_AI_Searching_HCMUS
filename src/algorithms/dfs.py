from common.node import Node
from common.utils import expand, reconstruct_path
from common.frontier import StackFrontier


# Tree - search Depth - first search (DFS) --> last visited - first explored
# Pseudo code

# function DFS(problem) returns a solution path or failure
#     node ← Node(state=problem.initial)
#     if problem.is_goal(node.state) then
#         return reconstruct_path(node)
#     frontier ← StackFrontier()
#     frontier.add(node)
#     while not frontier.empty() do
#         node ← frontier.remove()
#         for each child in expand(problem, node) do
#             if problem.is_goal(child.state) then
#                 return reconstruct_path(child)
#             frontier.add(child)
#     return failure


def dfs(problem):
    """Depth-First Search Algorithm (Tree Search)

    This function implements the Depth-First Search (DFS) algorithm for tree search. DFS explores the deepest nodes first before backtracking to shallower nodes. It does not keep track of visited states, which is suitable for tree structures.

    Args:
        problem (Problem): The problem to solve. The problem must provide:
            - `initial`: The initial state of the problem.
            - `is_goal(state)`: A method to check if a given state is the goal state.
            - `expand(node)`: A method to generate the child nodes from a given node.

    Returns:
        list or None: The path from the initial state to the goal state if a path is found. The path is
        represented as a list of states. If no path is found, the function returns None.
    """
    # Create the root node with the initial state.
    node = Node(state=problem.initial)

    # Check if the initial state is the goal state.
    if problem.is_goal(node.state):
        return reconstruct_path(node)

    # Initialize the frontier with the root node. Use a stack (LIFO) to implement DFS.
    frontier = StackFrontier()
    frontier.add(node)

    # Continue exploring until there are no more nodes to explore in the frontier.
    while not frontier.empty():
        # Remove the most recently added node from the frontier.
        node = frontier.remove()

        # Expand the current node to generate its children.
        for child in expand(problem=problem, node=node):
            s = child.state

            # Check if the child state is the goal state.
            if problem.is_goal(s):
                return reconstruct_path(child)

            # Add the child node to the frontier.
            frontier.add(child)

    # Return None if no path is found to the goal state.
    return None
