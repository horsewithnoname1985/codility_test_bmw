import time, pytest, logging
from random import shuffle, randint


def smallest_not_occuring_integer(A):
    start_time = time.time()

    A = sorted(A)

    min = 1
    for elem in A:
        if elem == min:
            min += 1

    return min

    # smallest_digit = 1
    #
    # while True:
    #     if smallest_digit not in A:
    #         return smallest_digit
    #     smallest_digit += 1


def test_ordered_medium_range():
    print(test_many_ranges_with_negatives.__name__)
    start_time = time.time()
    A = [i for i in range(1, 40001)]
    result = smallest_not_occuring_integer(A)
    assert result == 40001
    print("--- %s seconds ---" % (time.time() - start_time))


def test_shuffled_medium_range():
    print(test_many_ranges_with_negatives.__name__)
    A = [i for i in range(1, 40001)]
    shuffle(A)
    start_time = time.time()
    result = smallest_not_occuring_integer(A)
    assert result == 40001
    print("--- %s seconds ---" % (time.time() - start_time))


def test_shuffled_big_range():
    print(test_many_ranges_with_negatives.__name__)
    A = [i for i in range(1, 100001)]
    shuffle(A)
    start_time = time.time()
    result = smallest_not_occuring_integer(A)
    assert result == 100001
    print("--- %s seconds ---" % (time.time() - start_time))


def test_many_ranges_with_negatives():
    print(test_many_ranges_with_negatives.__name__)
    start_time = time.time()
    for i in range(100000):
        A = [i for i in range(-1, 3)]
        shuffle(A)
        result = smallest_not_occuring_integer(A)
        assert result == 3
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":

    pytest.main()

    # A = [23, 24, -45, 43, 89]
    # A = [1, 2, 3, 4, 5]
    # large_1_1
    # A = [i for i in range(1, 40001)]
    # large_1_2
    # A = [i for i in range(1, 40001)]
    # shuffle(A)
    # # large_2
    # A = [i for i in range(1, 100001)]
    # shuffle(A)
    # # # large_3
    # start_time = time.time()
    # for i in range (100000):
    #     A = [i for i in range(-1, 3)]
    #     shuffle(A)
    #     print(smallest_not_occuring_integer(A))
    #
    # start_time = time.time()
    # print(smallest_not_occuring_integer(A))
    # print("--- %s seconds ---" % (time.time() - start_time))
