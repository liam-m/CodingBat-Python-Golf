def round10(n):
    m = n%10
    if m < 5:
        return n-m
    else:
        return n+(10-m)

def round_sum(a, b, c):
    return sum(map(round10, [a, b, c]))
