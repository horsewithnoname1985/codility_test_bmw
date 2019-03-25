def rotate(a, k):
    # a_shifted = [None] * len(a)

    while k > 0:

        a_shifted = [None] * len(a)

        for i in range(len(a)):
            if i < len(a) - 1:
                a_shifted[i + 1] = a[i]
            elif i == len(a) - 1:
                a_shifted[0] = a[i]

        a = a_shifted
        k -= 1

    return a


if __name__ == "__main__":
    a = [44, 334, 67, 34, 23]
    k = 2
    print(rotate(a, k))
