def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    result = []
    for col in range(len(a[0])):        # col = 0, then 1  (each input column)
        new_row = []                    # a fresh EMPTY list for this output row
        for row in range(len(a)):       # row = 0, 1, 2  (walk down the column)
            new_row.append(a[row][col]) # grab one cell
        result.append(new_row)          # add the finished row (a list) to result
    return result