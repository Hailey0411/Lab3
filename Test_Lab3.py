import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    # REQ-01: Sort in ascending order with < 10 elements
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected_arr = [11, 12, 22, 25, 34, 64, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == expected_arr


def test_bubble_sort_descending():
    # REQ-02: Sort in descending order with < 10 elements
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    expected_arr = [90, 64, 34, 25, 22, 12, 11]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
   
    assert result == expected_arr


def test_bubble_sort_invalid():
    # Test case for invalid sorting order
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    result = Lab3.bubble_sort(input_arr, 3)
    assert result == []


def test_bubble_sort_large_input():
    # REQ-03: Return 1 if >= 10 numbers are entered
    input_arr = [64, 34, 25, 12, 22, 11, 90, 45, 55, 39]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 1


def test_bubble_sort_empty_input():
    # REQ-04: Return 0 if 0 numbers are entered
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 0


def test_bubble_sort_non_integer_input():
    # REQ-05: Return 2 if any values are not integers
    input_arr = [64, 34, "twenty-five", 12, 22, 11, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert result == 2
