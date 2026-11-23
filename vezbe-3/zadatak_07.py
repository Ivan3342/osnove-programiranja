def k_deljiv(k, n):
    for i in range(1, n + 1):
        if k % i != 0:
            return False
    return True