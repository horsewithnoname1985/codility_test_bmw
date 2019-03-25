import pytest, time


def solution(N):
    digit_list = [int(i) for i in str(N)]
    inverse_sorted_digit_list = sorted(digit_list, reverse=True)
    highest_sibling = int("".join(map(str, inverse_sorted_digit_list)))

    return highest_sibling


def test_lowest_digit():
    print(test_solution.__name__)
    start_time = time.time()

    data = 0
    result = solution(data)

    assert result == 0

    print("--- %s seconds ---" % (time.time() - start_time))


def test_highest_digit():
    print(test_solution.__name__)
    start_time = time.time()

    data = 10000
    result = solution(data)

    assert result == 10000

    print("--- %s seconds ---" % (time.time() - start_time))


def test_solution():
    print(test_solution.__name__)
    start_time = time.time()

    data = 1634
    result = solution(data)

    assert result == 6431

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    pytest.main()
