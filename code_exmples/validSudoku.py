import time
from random import sample


class Solver(object):
    base = 3
    side = base * base

    def hasDuplicate(self, iterable):
        seen = set()
        for item in iterable:
            if item != '.':
                if item in seen:
                    return True
                seen.add(item)
        return False

    def isValidSudoku(self, board):
        for row in range(9):
            if self.hasDuplicate(board[row][col] for col in range(9)):
                print('has duplicate in row')
                return False

        for col in range(9):
            if self.hasDuplicate(board[row][col] for row in range(9)):
                print('has duplicate in col')
                return False

        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                if self.hasDuplicate(board[row][col] for i in range(3) for j in range(3)):
                    print('has duplicate in 3*3 box')
                    return False

        return True

    def buildSudoku(self):

        def pattern(r, c):
            return (self.base * (r % self.base) + r // self.base + c) % self.side

        def shuffle(s):
            return sample(s, len(s))

        rBase = range(self.base)
        rows = [g * (self.base + r) for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g * (self.base + c) for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, self.base * self.base + 1))
        board = [[nums[pattern(r, c)] for c in cols] for r in rows]
        # when you want to print
        for line in board:
            print(line)
        return board

    def createNewSudokuToSolve(self):
        time.sleep(1)
        print(' thinking ....')
        time.sleep(2)
        sample_board = self.buildSudoku()
        squares = self.side * self.side
        empties = squares * 3 // 4
        for p in sample(range(squares), empties):
            sample_board[p // self.side][p % self.side] = 0

        numSize = len(str(self.side))
        for line in sample_board:
            print(*(f"{n or '.':{numSize}} " for n in line))


sudoku = Solver()
print(f" is valid Sudoku ? + ${sudoku.isValidSudoku(sudoku.buildSudoku())}")
print()
print()
# sudoku.createNewSudokuToSolve()
