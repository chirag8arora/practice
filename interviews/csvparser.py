import unittest

class Solution:

    def add_cell_to_row(self, cell, row):
        row.append(''.join(cell).strip())
        del cell[:]

    def add_row_to_result(self, cell, row, result):
        self.add_cell_to_row(cell, row)
        result.append(list(row))
        del row[:]

    def parse(self, s):
        row, result, cell = [], [], []
        in_quote, after_slash = False, False
        for i in s:
            if i == ',' and not in_quote and not after_slash:
                self.add_cell_to_row(cell, row)
            elif i == '"' and not after_slash:
                in_quote = (not in_quote)
            elif i == '\\' and not after_slash and in_quote:
                after_slash = True  # slash for escape
            elif i == '\n':
                self.add_row_to_result(cell, row, result)
            else:
                after_slash = False
                cell.append(i)
        self.add_row_to_result(cell, row, result)
        return result

class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.parse('123, jason, "hello world"'),
            [['123', 'jason', 'hello world']])
        self.assertEqual(s.parse(r'''123, jason, "hello world"
            124, mike, "nihao shijie"
            125, mike\, "\"nihao shijie\\"'''),
            [['123', 'jason', 'hello world'],
             ['124', 'mike', 'nihao shijie'],
             ['125', 'mike\\', '"nihao shijie\\']])


if __name__ == '__main__':
    unittest.main()
