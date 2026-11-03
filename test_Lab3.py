import Lab3

print("Test_Lab3")


# REQ-01: <10 numbers & SORT_ASCENDING returns list sorted ascending
def test_bubble_sort_ascending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)


# REQ-02: <10 numbers & SORT_DESCENDING returns list sorted descending
def test_bubble_sort_descending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)


# REQ-03: >=10 numbers entered returns integer 1
def test_bubble_sort_more_than_10():
    input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 1)


# REQ-04: 0 numbers entered returns integer 0
def test_bubble_sort_empty():
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 0)


# REQ-05: Non-integer values in list returns integer 2
def test_bubble_sort_invalid():
    input_arr = [64, 34, "abc", 12, 22]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 2)