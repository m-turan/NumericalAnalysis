import numpy as np


def replace_center_with_minus_one(d: int, n: int, m: int) -> np.ndarray:
    if d <= 0:
        raise ValueError("d must be greater than or equal to zero")
    if m > n:
        raise ValueError("m must be less than or equal to n")
    if n < 0:
        raise ValueError("n must be greater than zero")
    if m < 0:
        raise ValueError("m must be greater than zero")

    arr = np.random.randint(0, 10**d, (n, n))

    center_offset = (n - m) // 2
    arr[center_offset:center_offset + m, center_offset:center_offset + m] = -1

    return arr
