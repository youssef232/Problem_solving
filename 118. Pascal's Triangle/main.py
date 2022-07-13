def generate(numRows: int) -> list[list[int]]:
    output = [[1]]
    for i in range(1, numRows):
        temp1 = output[-1] +[0]
        temp2 = [0] + output[-1]
        output.append([temp1[i] + temp2[i] for i in range(len(temp1))])
    return output

