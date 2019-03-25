import pytest, time


def solution(x, y, d):
    steps = 0
    if x < y:
        steps = (y - x) // d + 1
        return steps
    else:
        return steps

def test_target_is_current():
    print(test_simple_solution.__name__)
    start_time = time.time()

    current = 5455
    minimum_target = 5455
    stepwidth = 1000000000

    result = solution(current, minimum_target, stepwidth)

    assert result == 0

    print("--- %s seconds ---" % (time.time() - start_time))


def test_maximum_target_maximum_stepwidth_solution():
    print(test_simple_solution.__name__)
    start_time = time.time()

    current = 1
    minimum_target = 1000000000
    stepwidth = 1000000000

    result = solution(current, minimum_target, stepwidth)

    assert result == 1

    print("--- %s seconds ---" % (time.time() - start_time))


def test_maximum_target_minimum_stepwidth_solution():
    print(test_simple_solution.__name__)
    start_time = time.time()

    current = 1
    minimum_target = 1000000000
    stepwidth = 1

    result = solution(current, minimum_target, stepwidth)

    assert result == 1000000000

    print("--- %s seconds ---" % (time.time() - start_time))


def test_simple_solution():
    print(test_simple_solution.__name__)
    start_time = time.time()

    current = 1
    minimum_target = 10
    stepwidth = 4
    result = solution(current, minimum_target, stepwidth)

    assert result == 3

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    pytest.main()
