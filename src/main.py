import os
import time
import tracemalloc
from common.problem import Problems
from common.utils import read_input, write_output
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.ucs import ucs
from algorithms.ids import ids
from algorithms.gbfs import gbfs
from algorithms.a_star import a_star_search
from algorithms.hill_climbing import hill_climbing

# Pseudo-code for run_algorithm()
# function RUN_ALGORITHM(algorithm, problem) returns path
#     path ← algorithm(problem)  # Execute the algorithm on the problem
#     return path  # Return the path found by the algorithm


def run_algorithm(algorithm, problem):
    """
    Wrapper function to run the specified algorithm on the given problem.

    Args:
        algorithm (function): The search algorithm to be executed.
        problem (Problems): The problem instance on which the algorithm will run.

    Returns:
        list: The path found by the algorithm from the initial state to the goal state.
    """
    path = algorithm(problem)  # Run the algorithm on the problem instance.
    return path  # Return the path found by the algorithm.


# Pseudo-code for measure_time()
# function MEASURE_TIME(algorithm, problem) returns (path, duration, memory_usage)
#     tracemalloc.start()  # Start memory tracking
#     start_time ← time.perf_counter()  # Record start time
#     path ← RUN_ALGORITHM(algorithm, problem)  # Run the algorithm
#     end_time ← time.perf_counter()  # Record end time
#     duration ← end_time - start_time  # Calculate duration
#     current, peak ← tracemalloc.get_traced_memory()  # Get memory usage
#     tracemalloc.stop()  # Stop memory tracking
#     return path, duration, peak / 1024  # Return path, duration, and memory usage in KB


def measure_time(algorithm, problem):
    """
    Wrapper function to measure the time and memory taken to run the algorithm.

    Args:
        algorithm (function): The search algorithm to be executed.
        problem (Problems): The problem instance on which the algorithm will run.

    Returns:
        tuple: A tuple containing the path, duration (in seconds), and memory usage (in KB).
    """
    tracemalloc.start()  # Start tracing memory allocations.
    start_time = time.perf_counter()  # Record the start time.
    path = run_algorithm(algorithm, problem)  # Run the algorithm.
    end_time = time.perf_counter()  # Record the end time.
    duration = (
        end_time - start_time
    )  # Calculate the duration of the algorithm execution.
    current, peak = (
        tracemalloc.get_traced_memory()
    )  # Get the current and peak memory usage.
    tracemalloc.stop()  # Stop tracing memory allocations.
    return (
        path,
        duration,
        peak / 1024,
    )  # Convert memory usage to KB and return the results.


# Pseudo-code for main()
# function MAIN(input_file, output_file)
#     try
#         problem ← READ_INPUT(input_file)  # Read the problem from the input file
#     catch Exception e
#         print("Error reading input file " + input_file + ": " + e)
#         return

#     algorithms ← {
#         "BFS": bfs,
#         "DFS": dfs,
#         "UCS": ucs,
#         "IDS": ids,
#         "GBFS": gbfs,
#         "A*": a_star_search,
#         "Hill-climbing": hill_climbing,
#     }
#     results ← empty dictionary

#     for each (name, algorithm) in algorithms do
#         try
#             path, duration, memory_usage ← MEASURE_TIME(algorithm=algorithm, problem=problem)  # Measure the algorithm execution
#             results[name] ← (path, duration, memory_usage)  # Store the results
#         catch Exception e
#             print("Error running " + name + " on " + input_file + ": " + e)
#             results[name] ← (None, 0, 0)  # Store default values in case of an error

#     try
#         WRITE_OUTPUT(output_file, results)  # Write the results to the output file
#     catch Exception e
#         print("Error writing output file " + output_file + ": " + e)


def main(input_file, output_file):
    try:
        problem = read_input(input_file)
    except Exception as e:
        print(f"Error reading input file {input_file}: {e}")
        return
    algorithms = {
        "BFS": bfs,
        "DFS": dfs,
        "UCS": ucs,
        "IDS": ids,
        "GBFS": gbfs,
        "A*": a_star_search,
        "Hill-climbing": hill_climbing,
    }
    results = {}
    for name, algorithm in algorithms.items():
        try:
            path, duration, memory_usage = measure_time(
                algorithm=algorithm, problem=problem
            )
            results[name] = (path, duration, memory_usage)
        except Exception as e:
            print(f"Error running {name} on {input_file}: {e}")
            results[name] = (None, 0, 0)

    try:
        write_output(output_file, results)
    except Exception as e:
        print(f"Error writing output file {output_file}: {e}")


if __name__ == "__main__":
    input_folder = "test/input"
    output_folder = "test/output"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(1, 6):
        input_file = os.path.join(input_folder, f"input{i}.txt")
        output_file = os.path.join(output_folder, f"output{i}.txt")
        main(input_file, output_file)
