def odd_occurence(array: list) -> int:
    if len(array) % 2 == 1:

        if len(array) > 1:

            for digit in array:
                count = array.count(digit)
                if count == 1:
                    return digit

        else:
            return array[0]

    return "Please input an array with an odd amount of elements"


if __name__ == "__main__":
    array = [3, 6, 3, 7, 8, 8, 7]
    array = [3, 3]
    print(odd_occurence(array))
