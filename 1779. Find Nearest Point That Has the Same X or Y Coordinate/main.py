import math


def nearestValidPoint(x: int, y: int, points: list[list[int]]) -> int:
    index = -1
    small_distance = math.inf
    for i in range(len(points)):
        if points[i][0] == x or points[i][1] == y:
            if small_distance > (abs(x - points[i][0]) + abs(y - points[i][1])):
                index = i
                small_distance = abs(x - points[i][0]) + abs(y - points[i][1])
    return index


print(nearestValidPoint(x=3, y=4, points=[[3, 4]]))
