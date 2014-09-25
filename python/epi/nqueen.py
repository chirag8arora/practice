class NQueen():
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for i in range(n)]

    def is_attack(self, row, col):
        for i in range(self.n):
            if self.board[i][col] == 1:
                return True
        i, j = row, col
        while i < self.n and j < self.n:
            if self.board[i][j] == 1:
                return True
            i += 1
            j += 1
        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return True
            i -= 1
            j -= 1
        i, j = row, col
        while i >= 0 and j < self.n:
            if self.board[i][j] == 1:
                return True
            i -= 1
            j += 1
        i, j = row, col
        while i < self.n and j >= 0:
            if self.board[i][j] == 1:
                return True
            i += 1
            j -= 1

    def placing(self, row):
        if row >= self.n:
            for l in self.board:
                print l
            print '===' * self.n
            return

        for col in range(self.n):
            # check attack now
            if self.is_attack(row, col):
                continue
            self.board[row][col] = 1
            self.placing(row + 1)
            self.board[row][col] = 0

q = NQueen(8)
q.placing(0)
