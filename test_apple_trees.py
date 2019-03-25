import pytest, time


def solution(A, K, L):
    total_trees = len(A)

    if K + L > total_trees:
        return -1

    if K + L == total_trees:
        apples = [int(x) for x in A]
        sum = 0
        for amount in apples:
            sum += amount
        return sum

    if K + L < total_trees:
        apples_alice = 0
        apples_bob = 0

        possible_apples_alice = get_apple_count_by_start_position(A, K)
        possible_apples_bob = get_apple_count_by_start_position(A, L)

        max_alice = 0
        for i in range(len(possible_apples_alice)):
            if possible_apples_alice[i] > max_alice:
                max_alice = possible_apples_alice[i]
                maxIndex = i



        return apples_alice + apples_bob


def get_apple_count_by_start_position(apple_count, trees):

    total_trees = len(apple_count)
    possible_count = []

    start_position = 0
    for i in range(start_position, total_trees - trees):

        apples = 0
        for j in range(i, i + trees):
            apples += apple_count[j + start_position]

        possible_count.append(apples)

    return possible_count


def test_not_enough_trees():
    print(test_not_enough_trees.__name__)
    start_time = time.time()

    apples = [10, 20, 30, 40, 50, 60]
    trees_alice = 2
    trees_bob = 3
    result = solution(apples, trees_alice, trees_bob)

    assert result == 200

    print("--- %s seconds ---" % (time.time() - start_time))


# def test_solution():
#     print(test_solution.__name__)
#     start_time = time.time()
#
#     data = 0
#     result = solution(data)
#
#     assert result == 0
#
#     print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    pytest.main()
