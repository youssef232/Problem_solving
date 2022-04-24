def average(salary: list[int]) -> float:
    minimum = salary[0]
    maximum = salary[1]
    count = 0
    sum = 0
    for i in salary:
        if i < minimum:
            minimum = i
        elif i > maximum:
            maximum = i
        sum += i
        count += 1

    return (sum - minimum - maximum) / (count - 2)

print(average([8000, 9000, 2000, 3000, 6000, 1000]))
