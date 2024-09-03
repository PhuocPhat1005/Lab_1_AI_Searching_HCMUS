# Stack Frontier is for Depth - First Search (DFS)
# Pseudo code

# class StackFrontier
#     method __init__()
#         frontier ← empty list

#     method add(node)
#         append node to frontier

#     method contains_state(state) returns boolean
#         return any node.state == state for each node in frontier

#     method empty() returns boolean
#         return length of frontier == 0

#     method remove() returns node
#         if empty()
#             raise Exception("empty frontier")
#         else
#             node ← last element in frontier
#             remove last element from frontier
#             return node


class StackFrontier:
    def __init__(self):
        # Initialize an empty list to serve as the stack (frontier)
        self.frontier = []

    def add(self, node):
        # Add a node to the frontier (stack). In a stack, this is equivalent to a push operation.
        self.frontier.append(node)

    def contains_state(self, state):
        # Check if a state is already in the frontier.
        # This method returns True if any node in the frontier has the same state as the given state, otherwise False.
        return any(node.state == state for node in self.frontier)

    def empty(self):
        # Check if the frontier is empty.
        # This method returns True if the frontier is empty, otherwise False.
        return len(self.frontier) == 0

    # Define the function that removes a node from the frontier and returns it.
    def remove(self):
        # Remove and return a node from the frontier (stack). In a stack, this is equivalent to a pop operation.
        # This method removes the last node that was added to the frontier (LIFO order).

        # If the frontier is empty, raise an exception indicating that no more nodes are available to remove.
        if self.empty():
            raise Exception("empty frontier")
        else:
            # Pop the last node from the list (stack) and return it.
            node = self.frontier.pop()
            return node


# Queue Frontier is for Breadth - First Search
# Pseudo code

# class QueueFrontier inherits StackFrontier
#     method remove() returns node
#         if empty()
#             raise Exception("empty frontier")
#         else
#             node ← first element in frontier
#             remove first element from frontier
#             return node


class QueueFrontier(StackFrontier):
    # Define the function that removes a node from the frontier and returns it.
    def remove(self):
        # Terminate the search if the frontier is empty, because this means that there is no solution.
        if self.empty():
            raise Exception("empty frontier")
        else:
            # Save the oldest item on the list (which was the first one to be added)
            node = self.frontier[0]
            # Save all the items on the list besides the first one (i.e. removing the first node)
            self.frontier = self.frontier[1:]
            return node
