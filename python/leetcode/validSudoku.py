class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean

    def ezCheck(self, r, i, flip):
        if flip[r][i] == True:
            return False
        else:
            flip[r][i] = True
        return True

    def isValidSudoku(self, board):
        lines_flip = [[False] * 9 for i in range(9)]
        rows_flip = [[False] * 9 for i in range(9)]
        block_flip = [[False] * 9 for i in range(9)]
        for r, line in enumerate(board):
            if not len(line) == 9:
                # base test
                return False
            for i, e in enumerate(line):
                # line
                if not e == '.':
                    flip_index = int(e) - 1
                    if not self.ezCheck(r, flip_index, lines_flip):
                        return False
                    if not self.ezCheck(i % 9, flip_index, rows_flip):
                        return False
                    if not self.ezCheck((r / 3) * 3 + (i / 3), flip_index, block_flip):
                        return False
        return True


def main():
    s = Solution()
    print s.isValidSudoku(
        ['53..7....',
         '6..195...',
         '.98....6.',
         '8...6...3',
         '4..8.3..1',
         '7...2...6',
         '.6....28.',
         '...419..5',
         '.....8.79']
    )


if __name__ == '__main__':
    main()
