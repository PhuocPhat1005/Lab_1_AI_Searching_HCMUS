# Pseudo code
# class Problems
#     method __init__(initial, goal, adjacency_matrix, heuristics)
#         self.initial ← initial
#         self.goal ← goal
#         self.adjacency_matrix ← adjacency_matrix
#         self.heuristics ← heuristics

#     method is_goal(state) returns boolean
#         return state == goal

#     method actions(state) returns list of actions
#         return list of indices i where adjacency_matrix[state][i] > 0

#     method result(state, action) returns new_state
#         return action

#     method action_cost(s, action, s_prime) returns cost
#         return adjacency_matrix[s][action]


class Problems:
    def __init__(self, initial, goal, adjacency_matrix, heuristics):
        self.initial = initial
        self.goal = goal
        self.adjacency_matrix = adjacency_matrix
        self.heuristics = heuristics

    def is_goal(self, state):
        return state == self.goal

    def actions(self, state):
        # Return actions sorted by index
        return [i for i, x in enumerate(self.adjacency_matrix[state]) if x > 0]

    def result(self, state, action):
        return action

    def action_cost(self, s, action, s_prime):
        return self.adjacency_matrix[s][action]
