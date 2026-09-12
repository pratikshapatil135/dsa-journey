def find_second_largest(arr):
    largest = float("-inf")
    second_largest = float("-inf")

    for element in arr:
        if element > largest:
            second_largest = largest
            largest = element
        elif element > second_largest and element != largest:
            second_largest = element

    return second_largest


arr = [12, 35, 1, 10, 34, 1]

result = find_second_largest(arr)

print("Second largest element:", result)