def intersection(arr1, arr2):
    set1 = set(arr1)
    result = set()

    for num in arr2:
        if num in set1:
            result.add(num)

    return list(result)


arr1 = [1, 2, 2, 1]
arr2 = [2, 2, 3]

result = intersection(arr1, arr2)

print("Intersection:", result)