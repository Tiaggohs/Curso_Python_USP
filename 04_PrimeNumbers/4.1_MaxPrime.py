def maximo(n, m):
    if (m > n):
        max = m
    else:
        max = n
    return max

def test_max():
    assert maximo(3, 2) == 3
