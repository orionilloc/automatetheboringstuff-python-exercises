# Write rotate(items, n). It returns a new list with the first n items moved to the
# end, keeping their order. If n is larger than the list, it wraps around. Do not
# modify the list that was passed in.

original = [1, 2, 3, 4, 5]

def rotate(items, n):
    if not items:
        return []
    n = n % len(items)
    rotated_original = items[n:] + items[:n]
    return rotated_original

assert rotate(original, 2) == [3, 4, 5, 1, 2]
assert original == [1, 2, 3, 4, 5]
assert rotate(original, 0) == [1, 2, 3, 4, 5]
assert rotate(original, 5) == [1, 2, 3, 4, 5]
assert rotate(original, 7) == [3, 4, 5, 1, 2]
assert rotate([], 3) == []
assert rotate(["a"], 10) == ["a"]
