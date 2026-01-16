def symmetric_pairs(pairs):
    seen = {}
    result = []

    for a, b in pairs:
        # check if reverse pair exists
        if b in seen and seen[b] == a:
            result.append((a, b))
        else:
            seen[a] = b

    return result

pairs = [(1,2), (3,4), (5,6), (2,1), (4,3)]
print(symmetric_pairs(pairs))