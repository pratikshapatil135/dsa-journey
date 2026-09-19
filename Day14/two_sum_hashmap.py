def two_sum(arr, target):
    seen = {}

    for i in range(len(arr)):
        needed = target - arr[i]

        if needed in seen:
            return [seen[needed], i]

        seen[arr[i]] = i

    return []


arr = [2, 7, 11, 15]
target = 9

result = two_sum(arr, target)

print("Indices:", result)