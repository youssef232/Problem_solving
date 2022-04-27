def checkStraightLine(coordinates: list[list[int]]) -> bool:

    x, y = (coordinates[1][0] - coordinates[0][0]), (coordinates[1][1] - coordinates[0][1])
    for i in range(2, len(coordinates)):
        if ((coordinates[i][1] - coordinates[0][1]) * x) != ((coordinates[i][0] - coordinates[0][0]) * y):
            return False
    return True


print(checkStraightLine([[0,0],[0,1],[0,-1]]))
