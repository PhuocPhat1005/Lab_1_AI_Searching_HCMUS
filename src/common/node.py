# Pseudo - code
# class Node:
#     def __init__(self, state, parent=None, action=None, path_cost=0, heuristic=0):
#         self.state ← state
#         self.parent ← parent
#         self.action ← action
#         self.path_cost ← path_cost
#         self.heuristic ← heuristic

#     def __lt__(self, other):
#         return (self.path_cost + self.heuristic) < (other.path_cost + other.heuristic)


class Node:
    """
    A class to represent a node in the search tree.

    Attributes:
        state: The state represented by this node.
        parent: The parent node of this node.
        action: The action taken to get to this node.
        path_cost: The cost of the path from the initial state to this node.
        heuristic: The heuristic value of this node.
    """

    def __init__(self, state, parent=None, action=None, path_cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.heuristic = heuristic

    def __lt__(self, other):
        """
        Less than comparison based on the sum of path cost and heuristic.
        This is used to order nodes in priority queues.
        """
        return (self.path_cost + self.heuristic) < (other.path_cost + other.heuristic)
