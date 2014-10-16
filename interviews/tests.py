def try1(s):
    start, in_space, in_quote = 0, False, False
    res = []
    s += ' '
    for i in range(len(s)):
        print i, s[i], in_quote, in_space
        if s[i] == ' ' and not in_quote:
            if not in_space:
               res.append(s[start: i])
            in_space = True
        elif s[i] ==  '"':
            if in_space and not in_quote:
                start = i
            in_quote = (not in_quote)
            in_space = False
        else:
            if in_space and not in_quote:
                in_space = False
                start = i
            continue
    return res

def try2(s):
    in_word = False
    in_quote = False
    start = 0
    s += ' '
    res = []
    for i in range(len(s)):
        if s[i] != ' ' or in_quote:
            if not in_word:
                in_word = True
                start = i
            if s[i] == '"':
                in_quote = not in_quote
        else:
            if in_word:
                res.append(s[start: i])
            in_word = False
    return res

def try1again(s):
    def consume_spaces(s, i):
        while i < len(s) and s[i] == ' ':
            i += 1
        return i

    def consume_quote(s, i):
        while i < len(s) and s[i] != '"':
            i += 1
        return i + 1

    def consume_words(s, start, res):
        i = start
        while i < len(s):
            if s[i] == '"':
                i = consume_quote(s, i + 1)
            elif s[i] == ' ':
                break
            else:
                i += 1
        res.append(s[start:i])
        return i

    i, res = 0, []
    while i < len(s):
        if s[i] == ' ':
            i = consume_spaces(s, i)
        else:
            i = consume_words(s, i, res)
    return res

# print try1again('I   have a   "fucking problem" am i')

def try3(matrix):

    def get_sum(matrix, start_point):
        i, j = start_point
        s = 0
        while i < len(matrix) and j < len(matrix[0]):
            s += matrix[i][j]
            i, j = i + 1, j + 1
        return s

    res = []
    if not matrix or not matrix[0]:
        return res

    for i in range(len(matrix))[::-1]:
        # m-1 -> 0
        res.append(get_sum(matrix, (i, 0)))
    for i in range(1, len(matrix[0])):
        res.append(get_sum(matrix, (0, i)))

    return res

# print try3([[1,2,3],[1,2,3],[1,2,3]])
# print try3([[1,2,3],[4,5,6],[7,8,9]])
# print try3([[1,2],[4,5],[7,8]])
# 123
# 123
# 123
# 12
# 45
# 78


def try4(n):
    def easy(n):
        c = 0
        while n:
            if n & 1:
                c += 1
            n = n >> 1
        return c

    def better(n):
        c = 0
        while n:
            n &= (n - 1)
            c += 1
        return c
    return better(n)

# print try4(2)


class Try5():
    """
    Unfinished, only add and subtract implemented
    """

    def add(self, num1, num2):
        if num1[0] == '-' and num2[0] == '-':
            return '-' + self.__add(num1[1:], num2[1:])
        elif num1[0] == '-':
            return self.__sub(num2, num1[1:])
        elif num2[0] == '-':
            return self.__sub(num1, num2[1:])
        else:
            return self.__add(num1, num2)

    def __add(self, num1, num2):
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        carry, result = 0, []
        while p1 >= 0 and p2 >= 0:
            tmp = int(num1[p1]) + int(num2[p2]) + carry
            result.append(tmp % 10)
            carry = tmp / 10
            p1, p2 = p1 - 1, p2 - 1
        if p2 >= 0:
            p1 = p2
            num1 = num2
        while p1 >= 0:
            tmp = int(num1[p1]) + carry
            result.append(tmp % 10)
            carry = tmp / 10
            p1 -= 1
        if carry:
            result.append(carry)
        return ''.join([str(i) for i in result[::-1]])

    def __compare(self, num1, num2):
        if len(num1) > len(num2):
            return 1
        elif len(num1) < len(num2):
            return -1
        else:
            for i in range(len(num1)):
                if num1[i] < num2[i]:
                    return -1
                elif num1[i] > num2[i]:
                    return 1
            return 0

    def sub(self, num1, num2):
        if num1[0] == '-' and num2[0] == '-':
            tmp = self.__sub(num1[1:], num2[1:])
            if tmp[0] == '-':
                return tmp[1:]
            else:
                return '-' + tmp
        elif num1[0] == '-':
            return '-' + self.__add(num2, num1[1:])
        elif num2[0] == '-':
            return self.__add(num1, num2[1:])
        else:
            return self.__sub(num1, num2)

    def __sub(self, num1, num2):
        # num1 - num2
        # make sure num1 > num2
        # otherwise swap them and add flag
        neg = False
        if(self.__compare(num1, num2) < 0):
            neg = True
            num1, num2 = num2, num1
        p1, p2 = len(num1) - 1, len(num2) - 1
        borrow, result = 0, []
        while p1 >= 0 and p2 >= 0:
            tmp = int(num1[p1]) - int(num2[p2]) - borrow
            if tmp < 0:
                borrow = 1
                result.append(10 + tmp)
            else:
                borrow = 0
                result.append(tmp)
            p1, p2 = p1 -1, p2 - 1
        while p1 >= 0:
            tmp = int(num1[p1]) - borrow
            if tmp < 0:
                borrow = 1
                result.append(10 + tmp)
            else:
                borrow = 0
                result.append(tmp)
            p1 -= 1
        if neg:
            return '-' + ''.join([str(i) for i in result[::-1]])
        return ''.join([str(i) for i in result[::-1]])


# try5 = Try5()
# print try5.add("372819372891", "-38290183123123123") \
#       == str(-38290183123123123 + 372819372891)
# print try5.sub("-372819372891", "-38290183123123123") \
#       == str(-372819372891 - -38290183123123123)


def try6(A):
    """
    what is H index???
    """
    A = sorted(A)[::-1]
    for k, v in enumerate(A):
        if v < k:
            return A[k - 1]

# print try6([2,1,1,1,1,1,3,2,3,3,5,4,4,4,4,5,6,8,4])


def try7():
    """
    cannot figure out what's the question
    """
    pass


def try8(s):
    # dfs with stack or recursion
    def dfs_stack(s):
        result = []
        stack = [[]]
        while stack:
            node = stack.pop()
            p = len(node)
            if p == len(s):
                result.append(''.join(node))
                continue
            if s[p] == '?':
                stack.append(node + ['0'])
                stack.append(node + ['1'])
            else:
                stack.append(node + [s[p]])
        return result

    def recursion(s, i, result):
        if i == len(s):
            result.append(''.join(s))
            return
        if s[i] == '?':
            s[i] = '1'
            recursion(s, i + 1, result)
            s[i] = '0'
            recursion(s, i + 1, result)
            s[i] = '?'
        else:
            recursion(s, i + 1, result)

    def dfs_recursion(s):
        result = []
        recursion(list(s), 0, result)
        return result

    return dfs_stack(s), dfs_recursion(s)

# print try8('10?01?')

def try9():
    """
    couldn't figure out the problem
    """
    pass

def try10(A):
    # brute n**2
    # count = 0
    # for i in range(len(A)):
    #     for j in range(i + 1, len(A)):
    #         if A[i] > A[j]:
    #             count += 1
    # return count
    # similar as merge sort

    def merge_count(A, count):

        if len(A) <= 1:
            return A, count
        mid = 0 + len(A) / 2
        l, count = merge_count(A[:mid], count)
        r, count = merge_count(A[mid:], count)
        return merge(l, r, count)

    def merge(l, r, count):
        if not l or not r:
            return l or r, count
        res, i, j = [], 0, 0
        while i < len(l) and j < len(r):
            if l[i] > r[j]:
                res.append(r[j])
                j += 1
                count += len(l) - i
            else:
                res.append(l[i])
                i += 1
        while j < len(r):
            res.append(r[j])
            j+= 1
        while i < len(l):
            res.append(l[i])
            i += 1
        return res, count

    _, count = merge_count(A, 0)
    return count

# print try10([5, 4, 3, 2])


class Try11():

    def __init__(self, size):
        self.size = size

    def get():
        pass

    def pop():
        pass

    def push():
        pass

    def is_empty():
        pass

    def is_full():
        pass

    """
    test cases
    t = Try11(11)
    t.get() # valueerror
    t.is_empty() # true
    t.is_full() # false
    t.push(3) #
    t.get()  # return 3
    t.push(2)
    t.get() # return 2
    t.pop()
    t.get() # return 3
    for i in range(11):
        t.push(i)
    t.get() # return 0
    t.is_full() # true
    t.is_empty() # false
    while not t.is_empty():
        t.pop() # 0,1,2,3,3, ...
    """



def try12(A, target):
    """no negative?"""
    # table save all the possiblity of A[n-1] can be one integer
    # [1, 5, 0, 6]
    # [(1), (15, 6), (15, 6, 150), (21, 12, 156, 1506)] ->
    # 1, 2, 3, 4, 5, ... n # n ** 2
    def genInt(B):
        r = 0
        for i in B:
            r = r * 10 + i
        return r

    before = []
    for i in range(len(A)):
        tmp = []
        for j in before:
            if j + A[i] <= target:
                tmp.append(j + A[i])
        if genInt(A[:i+1]) <= target:
            tmp.append(genInt(A[:i+1]))
        before = tmp

    for i in before:
        if i == target:
            return True
    return False

# print try12([1,5,0,6], 25)


def try13(s):
    c1, c2, ci1, ci2, cs1, cs2 = None, None, None, None, None, None
    best = 0
    for k, i in enumerate(s):
        try:
            print s[min(cs1, cs2):max(ci1, ci2)+1], ci1, ci2, cs1, cs2, c1, c2
        except:
            pass
        if not c1 or not c2:
            # initial
            if not c1:
                c1, ci1, cs1 = i, k, k
                continue
            if not c2:
                c2, ci2, cs2 = i, k, k
                continue
        elif i not in [c1, c2]:
            # new substring! first -> k
            # remove one of c1, c2
            # update
            best = max(best, max(ci1, ci2) - min(cs1, cs2) + 1)
            if ci2 > ci1:
                # update c1
                cs2 = ci1 + 1
                c1, ci1, cs1 = i, k, k
            else:
                # update c2
                cs1 = ci2 + 1
                c2, ci2, cs2 = i, k, k
        else:
            # update ci1, ci2 not cs1, cs2
            if i == c1:
                ci1 = k
            elif i == c2:
                ci2 = k
    best = max(best, max(ci1, ci2) - min(cs1, cs2) + 1)
    return best


# print try13('abcdddbaabccc')

def try14(n):
    # not neccsarrily starts with bigest
    # func(n) = 1 + func(n-1), 1 + func(n-4), 1 + func(n-9) ...
    # DP for sure
    dp = [0]
    for i in range(1, n + 1):
        dp.append(i)
        k = 1
        while k ** 2 <= i:
            dp[i] = min(dp[i], 1 + dp[i-k**2])
            k += 1
    return dp[n]

#  print try14(3123)


def try15():
    """
    couldn't figure out what's the quesion
    """
    pass

def try16(A):
    """
    might have better solution
    """
    # let's say A has n friend
    # go n nodes, findout who is the most common
    # dic[x] with counter
    best, friend = 0, None
    for i in A.friends():
        for j in i.friends():
            if j != A:
                if j in dic:
                    dic[j] += 1
                else:
                    dic[j] = 1
                if dic[j] > best:
                    best = dic[j]
                    friend = j
    return friend


def try17():
    """
    have no idea
    maybe heartbeat signal
    no heartbeat how to restart??!
    monit your self
    """
    pass


def try18():
    """
    count and find the k
    """
    pass

def try19(A, target):
    if not A:
        return None
    if len(A) <= 1:
        return 0
    # binary search
    def helper(A, target, start, end):
        if start == end:
            return start
        mid = start + (end - start) / 2
        if A[mid] == target:
            return mid
        elif A[mid + 1] == target:
                return mid + 1
        elif A[mid] > target:
            return helper(A, target, start, mid)
        elif A[mid + 1] < target:
            return helper(A, target, mid + 1, end)
        else:
            if abs(target - A[mid]) < abs(target - A[mid + 1]):
                return mid
            else:
                return mid + 1
    return helper(A, target, 0, len(A) - 1)

# print try19([1.2, 2.5, 4.5, 9.3], 5)
# print try19([1.2, 2.5, 4.5], 0)
# 0, 2
# mid = 1 A[mid] < target A[mid + 1] > target
# compare 2.5 and 4.3 return mid =  1
# 0, 3
# mid = 1 A[mid] < 5, A[mid + 1] < 5
# helper(A, target, 2, 3)
# mid = 2, A[mid] < 5 A[mid + 1] > 5
# return mid = 2
# 0, 2 mid = 1 1 < target, 2< target return helper(A, target, 2, 2)


def try20():
    """check utf-8"""
    pass

def try21():
    """design"""
    pass

def try22(s):
    def line_comment(s, start, res):
        i = start
        while i < len(s):
            if s[i] == '\n':
                res.append(s[start: i])
                return i + 1
            i += 1
        return None

    def block_comment(s, start, res):
        i = start
        while i < len(s):
            if s[i] == '*':
                i += 1
                if s[i] == '/':
                    res.append(s[start: i-1])
                    return i + 1
            i += 1
        return None

    def quote(s, start):
        i = start
        while i < len(s):
            if s[i] == '"':
                return i + 1
            i += 1
        return None

    s += '\n'
    i, res = 0, []
    while i is not None and i < len(s):
        if s[i] == '/':
            i += 1
            if s[i] == '/':
                i = line_comment(s, i+1, res)
            elif s[i] == '*':
                i = block_comment(s, i+1, res)
        elif s[i] == '"':
            i = quote(s, i+1)
        else:
            i += 1
    return res


code = """
// shabi
function haha(nihao):
    cao=ni=ma // ceshi
    var cs = "// jian zhi diao bao le"
    // zenme zheme li hai
/* zhege fang fa te bie niubi  */
"""

# print try22(code)

def try23():
    # block1 block2
    # block3 block4
    # block4 = block1234 - block13 - block12 + block1
    pass

def try24():
    """
    same as try 3 or 4 dfs or recursion
    """
    pass

def try25():
    """
    what is this ??!
    count?
    """
    pass
