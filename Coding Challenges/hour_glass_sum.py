def hourglassSum(arr):
    max_hourglass_sum = -9*7
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            hourglass_sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2]
                                      + arr[i+1][j+1]
                        + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            if hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = hourglass_sum

    return max_hourglass_sum
