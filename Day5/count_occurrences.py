def count_occurrences(arr, target):
    count = 0

    for element in arr:
        if element == target:
            count += 1

    return count


arr = [2, 5, 2, 8, 2, 9]
target = 2

result = count_occurrences(arr, target)

print("Count:", result)