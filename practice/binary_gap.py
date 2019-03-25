def max_binary_gap(number: int) -> int:

    if type(number) == int and number > 0:

        binary_gaps = [0]
        binary_number = format(number, "b")
        digits = [int(x) for x in str(binary_number)]

        inGap = False
        current_binary_gap = 0

        for digit in digits:
            if inGap and digit == 0:
                current_binary_gap += 1
            if digit == 1:
                if inGap:
                    binary_gaps.append(current_binary_gap)
                    current_binary_gap = 0
                else:
                    inGap = True

        return max(binary_gaps)

    else:
        return "Please enter positive integer value"


if __name__ == "__main__":
    max_binary_gap(26)
