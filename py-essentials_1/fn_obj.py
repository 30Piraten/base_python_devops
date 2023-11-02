def double(input):
    return input * 2


def triple(input):
    return input * 3


functions = [double, triple]

for function in functions:
    print(function(3))
