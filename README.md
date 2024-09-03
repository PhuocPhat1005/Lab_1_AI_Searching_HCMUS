*CSC14003 - Introduction to Artificial Intelligence - Faculty of Information Technology - HCMUS*
# LAB 01 : SEARCHING
## 1. Description
* You are required to implement and compare various graph search algorithms. The algorithms to be included in this lab are as follows:
  * Breadth-first search (BFS)
  * Tree-search Depth-first search (DFS)
  * Uniform-cost search (UCS)
  * Iterative deepening search (IDS)
  * Greedy best-first search (GBFS)
  * Graph-search A* (A*)
  * Hill-climbing (HC) variant
* You will:
  * Read input from a file.
  * Perform path search from the start node to the goal node on a given graph.
  * Write the results to an output file.
  * Compare and evaluate the algorithms based on runtime and memory usage.
* Please note that:
  *  BFS, DFS and GBFS algorithms stop when the goal node is generated, not when the goal node is expanded.
  *  UCS and A* algorithms stop when the goal node is expanded.
  *  If Hill Climbing algorithm gets stuck, it is considered as having no path.
## 2. Requirements
### 2.1. Programming Language
* The program can be written in either Python or C/C++.
*  You can use supporting any libraries, but the main algorithms directly related to the search process must be implemented by your own.
### 2.2. Input
* The input file contains information about the graph and weights, formatted as follows:
  * The first line contains the number of nodes in the graph.
  * The second line contains two integers representing the start and goal nodes.
  * The subsequent lines contain the adjacency matrix of the graph.
  * The last line contains the heuristic weights for each node (for algorithms that use heuristics).
* Note that the graph can be either directed or undirected.
* Example input file:

<center>
    <img src = "https://github.com/user-attachments/assets/d64fd73f-aeac-4b9f-b827-806a3998f23c" width="400" alt="Figure 1: Example input file for a graph"/>
	<div style="text-align: center;"><i><b>Figure 1.</b>Example input file for a graph.</i></div>
</center>

### 2.3. Output

