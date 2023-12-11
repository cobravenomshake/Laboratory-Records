from collections import deque

# Class to represent the puzzle state
class PuzzleState:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

# Function to print the path from the initial state to the goal state
def print_solution(final_state):
    path = []
    while final_state:
        path.append(final_state)
        final_state = final_state.parent

    for t in reversed(path):
        if t.move is not None:
            print("Move:", t.move)
        print_board(t.board)
        print("")

# Function to print the puzzle board
def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i * 3 + j], end=" ")
        print()

# Function to find the index of the blank space in the board
def find_blank(board):
    return board.index(0)

# Function to generate possible moves from a given state
def generate_moves(state):
    moves = []
    blank_index = find_blank(state.board)
    row, col = divmod(blank_index, 3)

    if row > 0:
        moves.append("Up")
    if row < 2:
        moves.append("Down")
    if col > 0:
        moves.append("Left")
    if col < 2:
        moves.append("Right")

    return moves

# Function to apply a move and generate a new state
def apply_move(state, move):
    blank_index = find_blank(state.board)
    row, col = divmod(blank_index, 3)

    if move == "Up":
        new_row = row - 1
        new_col = col
    elif move == "Down":
        new_row = row + 1
        new_col = col
    elif move == "Left":
        new_row = row
        new_col = col - 1
    elif move == "Right":
        new_row = row
        new_col = col + 1

    new_blank_index = new_row * 3 + new_col
    new_board = state.board[:]
    new_board[blank_index], new_board[new_blank_index] = new_board[new_blank_index], new_board[blank_index]

    return PuzzleState(new_board, parent=state, move=move)

# Function to perform breadth-first search
def bfs(initial_state, goal_state):
    visited = set()
    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()

        if current_state == goal_state:
            print("Goal reached!")
            print_solution(current_state)
            return

        visited.add(current_state)

        for move in generate_moves(current_state):
            new_state = apply_move(current_state, move)
            if new_state not in visited:
                queue.append(new_state)

# Example usage:
initial_board = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]

initial_state = PuzzleState(initial_board)
goal_state = PuzzleState(goal_board)

bfs(initial_state, goal_state)
