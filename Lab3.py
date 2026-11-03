SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):
    # REQ-04: If 0 numbers are entered, return 0
    if len(arr) == 0:
        return 0

    # REQ-03: If >= 10 numbers are entered, return 1
    if len(arr) >= 10:
        return 1

    # REQ-05: If any value is not an integer, return 2
    for item in arr:
        if not isinstance(item, int):
            return 2

    # REQ-01 & REQ-02: Sort list if < 10 numbers and all integers
    arr_result = arr.copy()
    n = len(arr_result)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorting_order == SORT_ASCENDING:
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
            elif sorting_order == SORT_DESCENDING:
                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
            else:
                return []

    return arr_result


def main():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    print("Lab 3 - Software Unit Testing with PyTest\n")

    result = bubble_sort(input_arr, SORT_ASCENDING)
    print("Sorted array in ascending order:")
    print(result)

    result = bubble_sort(input_arr, SORT_DESCENDING)
    print("Sorted array in descending order:")
    print(result)


if __name__ == "__main__":
    main()