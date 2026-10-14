# Write dedupe(items). It returns a new list with duplicates removed, keeping the
# First occurrence of each item in its original order. Do not use set(). Do not modify the list that was passed in.

original = [3, 1, 3, 2, 1]

def dedupe(original):
    deduped_list = []
    for item in original:
        if item not in deduped_list:
            deduped_list.append(item)
    return deduped_list

assert dedupe(original) == [3, 1, 2]
assert original == [3, 1, 3, 2, 1]
assert dedupe([]) == []
assert dedupe(["a", "A", "a"]) == ["a", "A"]

