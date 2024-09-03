from common.node import Node
from common.problem import Problems
from common.utils import expand, reconstruct_path

# IDS (Iterative Deepening Search)
# Pseudo - code

# function DEPTH-LIMITED-SEARCH(problem, limit) returns a solution path or cutoff or failure
#     return RECURSIVE-DLS(MAKE-NODE(problem.initial), problem, limit)

# function RECURSIVE-DLS(node, problem, limit) returns a solution path or cutoff or failure
#     if problem.IS-GOAL(node.STATE) then
#         return RECONSTRUCT-PATH(node)
#     else if limit = 0 then
#         return cutoff
#     else
#         cutoff_occurred ← false
#         for each child in EXPAND(problem, node) do
#             result ← RECURSIVE-DLS(child, problem, limit - 1)
#             if result = cutoff then
#                 cutoff_occurred ← true
#             else if result ≠ failure then
#                 return result
#         if cutoff_occurred then
#             return cutoff
#         else
#             return failure


def depth_limited_search(problem, limit):
    """
    Depth-Limited Search (DLS)

    Args:
        problem (Problems): The problem instance which includes the initial state, goal state, and other problem-specific methods.
        limit (int): The depth limit for the search.

    Returns:
        list: A list representing the path from the initial state to the goal state if a path is found,
              'cutoff' if the depth limit is reached, or None if no path is found.
    """

    def recursive_dls(node, problem, limit):
        """
        Recursive helper function for Depth-Limited Search.

        Args:
            node (Node): The current node in the search.
            problem (Problems): The problem instance.
            limit (int): The current depth limit for the search.

        Returns:
            list or str or None: A list representing the path to the goal if found,
                                 'cutoff' if the depth limit is reached, or None if no path is found.
        """
        # Check if the current node is the goal state
        if problem.is_goal(node.state):
            return reconstruct_path(node)
        # If the depth limit is reached, return 'cutoff'
        elif limit == 0:
            return "cutoff"
        else:
            cutoff_occurred = False
            # Expand the current node and recurse for each child
            for child in expand(problem=problem, node=node):
                result = recursive_dls(child, problem, limit - 1)
                if result == "cutoff":
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return "cutoff" if cutoff_occurred else None

    # Start the recursive DLS with the initial node and given depth limit
    return recursive_dls(
        Node(state=problem.initial, parent=None, action=None, path_cost=0),
        problem,
        limit,
    )


# Pseudo-code for IDS
# function IDS (problem ← Problems) returns a solution path or failure
# depth ← 0
# while true do
#     result ← DLS (problem, depth)
#     if result ≠ cutoff then
#         return result
#     depth ← depth + 1


def ids(problem):
    """
    Iterative Deepening Search (IDS)

    Args:
        problem (Problems): The problem instance which includes the initial state, goal state, and other problem-specific methods.

    Returns:
        list: A list representing the path from the initial state to the goal state if a path is found, otherwise None.
    """
    depth = 0
    # Continuously increase the depth limit until a solution is found
    while True:
        result = depth_limited_search(problem, depth)
        if result != "cutoff":
            return result
        depth += 1
