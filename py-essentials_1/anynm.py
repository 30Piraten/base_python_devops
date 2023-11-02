items = [[0, "a", 2], [5, "b", 0], [2, "c", 1]]

# using sorted  method
result = sorted(items)  # return first entry

print(result)

# using a function


def second(item):
    # return second entry
    return item[1]


result = sorted(items, key=second)
print(result)


# using lambda

second_place = sorted(items, key=lambda item: item[1])
third_place = sorted(items, key=lambda item: item[2])

print(second_place)
print(third_place)
