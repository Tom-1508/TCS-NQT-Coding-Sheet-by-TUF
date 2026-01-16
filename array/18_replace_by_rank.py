def replace_by_rank(arr):
    sorted_unique = sorted(set(arr))  # step 1: sort unique values

    # step 2: create rank map
    rank = {}
    for i, value in enumerate(sorted_unique):
        rank[value] = i + 1

    # step 3: replace each element by its rank
    result = []
    for num in arr:
        result.append(rank[num])

    return result

print(replace_by_rank([40, 10, 30, 20]))