***CSC14003 - Introduction to Artificial Intelligence - HCMUS***
# LAB 01 : SEARCHING
## 1. Description
* You are required to implement and compare various graph search algorithms. The algorithms to be included in this lab are as follows:
  * Breadth-first search (**BFS**)
  * Tree-search Depth-first search (**DFS**)
  * Uniform-cost search (**UCS**)
  * Iterative deepening search (**IDS**)
  * Greedy best-first search (**GBFS**)
  * Graph-search A* (**A***)
  * Hill-climbing (**HC**) variant
* You will:
  * Read input from a file.
  * Perform path search from the start node to the goal node on a given graph.
  * Write the results to an output file.
  * Compare and evaluate the algorithms based on runtime and memory usage.
* Please note that:
  *  **BFS**, **DFS** and **GBFS** algorithms stop when the goal node is generated, not when the goal node is expanded.
  *  **UCS** and **A*** algorithms stop when the goal node is expanded.
  *  If **Hill Climbing** algorithm gets stuck, it is considered as having no path.
## 2. Requirements
### 2.1 Programming Language
* The program can be written in either **Python** or **C/C++**.
*  You can use supporting any libraries, but the main algorithms directly related to the search process must be implemented by your own.
### 2.2 Input
* The input file contains information about the graph and weights, formatted as follows:
  * The first line contains the number of nodes in the graph.
  * The second line contains two integers representing the start and goal nodes.
  * The subsequent lines contain the adjacency matrix of the graph.
  * The last line contains the heuristic weights for each node (for algorithms that use heuristics).
* Note that the graph can be either directed or undirected.
* Example input file:

<center>
    <img src = "https://github.com/user-attachments/assets/d64fd73f-aeac-4b9f-b827-806a3998f23c" width="400" alt="Figure 1: Example input file for a graph"/>
	<div style="text-align: center;"><i><b>Figure 1. </b>Example input file for a graph.</i></div>
</center>

### 2.3 Output
The output file should contain:
* The path from the start node to the goal node for each algorithm. 
  If there is no path, the output is -1.
* The runtime and memory usage of each algorithm.

Example output file:
```
BFS:
Path: 0 -> 1 -> 3
Time: 0.0000003 seconds
Memory: 8 KB
...
Hill-climbing:
Path: 0 -> 2 -> 3
Time: 0.0000003 seconds
Memory: 8 KB
```
### 2.4 Report
The report must fully give the following sections:
* Your information (student ID, full name, etc.).
* Self-evaluation of the completion rate of the lab and other requirements.
* Detailed algorithm description. Illustrative images are encouraged.
* Describe the test cases and performance metrics of the algorithm. Provide a complete and detailed review of your system.
* The report needs to be well-formatted and exported to PDF. Note that for editors like Jupyter notebook, you need to find a way to format it well before exporting to PDF.
* If there are figures cut off by the page break, etc., points will be deducted.
* References (if any).
### 2.5 Submission
* All reports, programs, test cases, etc., must be contributed in the form of a compressed file (.zip, .rar, .7z) and named according to the format **StudentID.zip/.rar/.7z**.
• If the compressed file is larger than 25MB, prioritize compressing the report and program. Test cases, etc., may be uploaded to the Google Drive and shared via a link.
## 3. Assessment
| No. | Details                                                                                                                             |  Score   |
|:---:| ----------------------------------------------------------------------------------------------------------------------------------- |:--------:|
|  1  | Implement BFS correctly.                                                                                                            |   10%    |
|  2  | Implement DFS correctly.                                                                                                            |   10%    |
|  3  | Implement UCS correctly                                                                                                             |   10%    |
|  4  | Implement IDS correctly                                                                                                             |   10%    |
|  5  | Implement GBFS correctly.                                                                                                           |   10%    |
|  6  | Implement A* correctly.                                                                                                             |   10%    |
|  7  | Implement Hill-climbing correctly.                                                                                                  |   10%    |
|  8  | Generate at least 5 test cases for all algorithm with different attributes. Describe them in the experiment section of your report. |   10%    |
|  9  | Report your algorithm, experiment with some reflection or comments.                                                                 |   20%    |
|     | **Total**                                                                                                                           | **100%** |
## 4. Notices
Please pay attention to the following notices:
* This is a **INDIVIDUAL** assignment
* Any plagiarism, any tricks, or any lie will have a 0 point for the course grade.
