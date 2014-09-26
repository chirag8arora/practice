# 5.7 x ** y
def power(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    c = power(x, y >> 1)
    if y & 1:
        return c * c * x
    else:
        return c * c

print power(1.1, 1000)
