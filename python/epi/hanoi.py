class Hanoi():

    def __init__(self, n):
        self.n = n
        self.sticks = [[], [], []]
        self.sticks[0] = range(1, n + 1)[::-1]

    def run(self):
        self.hanoi(self.n, 1, 2)

    def get_buffer(self, f, t):
        return (set([1, 2, 3]) - set([f, t])).pop()

    def hanoi(self, n, f, t):
        if n == 1:
            self.sticks[t-1].append(
                self.sticks[f-1].pop())
            print self.sticks
            return

        b = self.get_buffer(f, t)
        self.hanoi(n-1, f, b)
        self.hanoi(1, f, t)
        self.hanoi(n-1, b, t)

h = Hanoi(6)
h.run()

# example
# n = 3, from p1 [3, 2, 1] to p2
# b = p3
# 2 from p1 to p3
    # b = p2
    # 1 from p1 [3, 2] to p2 [1]
    # 1 from p1 [3] to p3 [2]
    # 1 from p2 [] to p3 [2, 1]
# 1 from p1 to p2
    # 1 from p1 [] to p2 [3]
# 2 from p3 to p2
    # b = p1
    # 1 from p3 [2] to p1 [1]
    # 1 from p3 [] to p2 [3, 2]
    # 1 from p1 [] to p2 [3, 2, 1]
