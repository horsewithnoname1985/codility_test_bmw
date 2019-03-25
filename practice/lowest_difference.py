def solution(A):

    list_length = len(A)
    lowest_difference = 0

    for i in range(1, list_length):
        first = A[:i]
        second = A[i:]
        sum_first = 0
        sum_second = 0

        for digit in first:
            sum_first += digit

        for digit in second:
            sum_second += digit

        current_difference = abs(sum_first - sum_second)

        if i == 1:
            lowest_difference = current_difference

        if current_difference < lowest_difference:
            lowest_difference = current_difference

    return lowest_difference
