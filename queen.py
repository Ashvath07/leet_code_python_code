class Solution(object):

    def solveNQueens(self, n):

        # Stores all valid solutions
        self.result = []

        # Create board filled with '.'
        board = [['.' for _ in range(n)] for _ in range(n)]

        # Start backtracking from row 0
        self.solve(board, 0)

        return self.result

    def solve(self, board, r):

        # Base Case: All rows processed
        if r == len(board):

            temp = []

            # Convert each row into string
            for row in board:
                temp.append("".join(row))

            # Store solution
            self.result.append(temp)

            return

        # Try placing queen in every column
        for c in range(len(board)):

            # Check if position is safe
            if self.isSafe(board, r, c):

                # Place Queen
                board[r][c] = 'Q'

                # Move to next row
                self.solve(board, r + 1)

                # Backtrack (remove queen)
                board[r][c] = '.'

    def isSafe(self, board, r, c):

        # Check same column upwards
        for i in range(r):
            if board[i][c] == 'Q':
                return False

        # Check upper-left diagonal
        i, j = r - 1, c - 1
        while i >= 0 and j >= 0:

            if board[i][j] == 'Q':
                return False

            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = r - 1, c + 1
        while i >= 0 and j < len(board):

            if board[i][j] == 'Q':
                return False

            i -= 1
            j += 1

        return True
