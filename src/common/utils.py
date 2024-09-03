from common.node import Node
from common.problem import Problems

# Pseudo code
# function EXPAND(problem, node) returns a generator of child nodes
#     s ← node.STATE  # Get the current state from the node
#     for each action in problem.ACTIONS(s) do  # Loop through all possible actions from the current state
#         s_prime ← problem.RESULT(s, action)  # Get the resulting state after applying the action
#         path_cost ← node.PATH_COST + problem.ACTION_COST(s, action, s_prime)  # Calculate the new path cost
#         heuristic ← problem.HEURISTICS[s_prime]  # Get the heuristic value for the new state
#         child ← NODE(STATE=s_prime, PARENT=node, ACTION=action, PATH_COST=path_cost, HEURISTIC=heuristic)  # Create a new child node
#         yield child  # Yield the child node


def expand(problem, node):
    """
    Generates the child nodes of a given node by applying all possible actions.

    Args:
        problem (Problems): The problem instance which includes the initial state, goal state, and other problem-specific methods.
        node (Node): The current node to be expanded.

    Yields:
        Node: The child node resulting from applying an action to the current node.
    """
    s = node.state  # Get the current state from the node.
    for action in problem.actions(
        s
    ):  # Loop through all possible actions from the current state.
        s_prime = problem.result(
            s, action
        )  # Get the resulting state after applying the action.
        path_cost = node.path_cost + problem.action_cost(
            s, action, s_prime
        )  # Calculate the new path cost.
        heuristic = problem.heuristics[
            s_prime
        ]  # Get the heuristic value for the new state.
        child = Node(  # Create a new child node with the new state, path cost, and heuristic.
            state=s_prime,
            parent=node,
            action=action,
            path_cost=path_cost,
            heuristic=heuristic,
        )
        yield child  # Yield the child node.


# Pseudo-code for read_input()
# function READ_INPUT(file_path) returns Problems
#     file ← open file_path for reading
#     lines ← read all lines from file
#     close file

#     num_nodes ← convert lines[0] to integer
#     start, goal ← convert lines[1] to two integers
#     adjacency_matrix ← empty list

#     for i ← 2 to 2 + num_nodes - 1 do
#         row ← convert lines[i] to list of integers
#         append row to adjacency_matrix

#     heuristics ← convert lines[2 + num_nodes] to list of integers

#     return Problems(initial=start, goal=goal, adjacency_matrix=adjacency_matrix, heuristics=heuristics)


def read_input(file_path):
    """Reads the input file and constructs the problem instance.

    Args:
        file_path (str): Path to the input file.

    Returns:
        Problems: An instance of the Problems class.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()

    num_nodes = int(lines[0].strip())  # Read the number of nodes.
    start, goal = map(int, lines[1].strip().split())  # Read the start and goal nodes.
    adjacency_matrix = []

    for i in range(2, 2 + num_nodes):  # Read the adjacency matrix.
        adjacency_matrix.append(list(map(int, lines[i].strip().split())))

    heuristics = list(
        map(int, lines[2 + num_nodes].strip().split())
    )  # Read the heuristic values.

    return Problems(
        initial=start,
        goal=goal,
        adjacency_matrix=adjacency_matrix,
        heuristics=heuristics,
    )


# Pseudo - code
# function RECONSTRUCT_PATH(node) returns path
#     path ← an empty list
#     while node is not null do
#         append node.state to path
#         node ← node.parent
#     end while
#     reverse path
#     return path


def reconstruct_path(node):
    """
    Reconstruct the path from the initial state to the goal state by following
    the parent links from the goal node back to the initial node.

    Args:
        node (Node): The goal node from which the path reconstruction starts.

    Returns:
        list: A list representing the path from the initial  state to the goal state.
    """
    path = []  # Initialize an empty list to store the path.

    while node:
        # Traverse back from the goal node to the initial node.
        path.append(node.state)  # Add the current node's state to the path.
        node = node.parent  # Move to the parent node.

    path.reverse()  # Reverse the path to get it from the initial state to the goal state.
    return path  # Return the reconstructed path.


# Pseudo-code
# function WRITE_OUTPUT(output_file, results)
#     try
#         file ← open output_file for writing
#         for each (name, result) in results.items() do
#             path, duration, memory_usage ← result
#             write name to file
#             if path is null
#                 write "Path: -1" to file
#             else
#                 write "Path: " + join path with " -> " to file
#             write "Time: " + format duration with 8 decimal places + " seconds" to file
#             write "Memory: " + format memory_usage with 2 decimal places + " KB" to file
#             write "\n===============\n\n" to file
#         end for
#         close file
#     catch Exception e
#         raise ValueError("Error writing output file " + output_file + ": " + e)


def write_output(output_file, results):
    """
    Writes the results of the search algorithms to the output file.

    Args:
        output_file (str): Path to the output file.
        results (dict): Dictionary containing the results of the search algorithms.
    """
    try:
        with open(output_file, "w") as file:
            for name, result in results.items():
                path, duration, memory_usage = result
                file.write(f"{name}:\n")
                if path is None:
                    file.write("Path: -1\n")
                else:
                    file.write("Path: " + " -> ".join(map(str, path)) + "\n")
                file.write(f"Time: {duration:.8f} seconds\n")
                file.write(f"Memory: {memory_usage:.2f} KB\n")
                file.write("\n===============\n\n")
    except Exception as e:
        raise ValueError(f"Error writing output file {output_file}: {e}")
