def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    import numpy as np
    old_m = len(a)
    old_n = len(a[0])

    new_m = old_n
    new_n = old_m
    
    output = np.zeros(shape=(new_m, new_n))


    for i in range(old_m):
        for j in range(old_n):
            output[j][i] = a[i][j]

    
    return output

