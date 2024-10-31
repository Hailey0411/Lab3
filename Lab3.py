print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        return 2  # REQ-05

    # Handle case where no numbers are entered
    if len(arr) == 0:
        return 0  # REQ-04

    # If there are >= 10 numbers, return 1
    if len(arr) >= 10:
        return 1  # REQ-03

    # Check if sorting_order is valid; if not, return an empty list
    if sorting_order not in (SORT_ASCENDING, SORT_DESCENDING):
        return []  # Handle invalid sorting_order early

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if sorting_order == SORT_ASCENDING:
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
            elif sorting_order == SORT_DESCENDING:
                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

    return arr_result



def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90,12,14,15,33,"22"]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)


if __name__ == "__main__":
    main()


