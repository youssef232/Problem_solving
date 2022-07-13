def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    oneDim = []
    output = [[0] * c for i in range(r)]
    m = len(mat)
    n = len(mat[0])
    if (m * n) != (r * c):
        return mat
    for i in range(m):
        for j in range(n):
            oneDim.append(mat[i][j])
    s = 0
    for i in range(r):
        for j in range(c):
            output[i][j] = oneDim[s]
            s += 1

    return output


mat = [[1, 2], [3, 4]]
r = 2
c = 4
print(matrixReshape(mat, r, c))
