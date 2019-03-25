import pytest, time


def solution(input):
    return input


def test_solution():
    print(test_solution.__name__)
    start_time = time.time()

    data = 0
    result = solution(data)

    assert result == 0

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    pytest.main()
