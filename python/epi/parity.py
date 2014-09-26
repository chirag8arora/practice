# 5.1
# O(n) flip flop
def parity2(A):
    # O(n)
    parity = 0
    for i in A:
        while i > 0:
            if i & 1 == 1:
                parity ^= 1
            i >>= 1
    return parity

def parity(A):
    # O(k)
    # trick <- remove lowerest 1
    parity = 0
    for i in A:
        while i:
            parity ^= 1
            i &= i - 1
    return parity

A = [789327189372981,328910382910382,38291038219032,48390248951]
print parity(A)
