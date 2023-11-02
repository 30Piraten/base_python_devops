# Lazy evaluation

# Generator
import sys


def count():
    n = 0
    while True:
        n += 1
        yield n


counter = count()
print(counter)

n1 = next(counter)
n2 = next(counter)
n3 = next(counter)

print(f"n1: {n1}\nn2: {n2}\nn3: {n3}\n")

print(count())

# -> case study with the return keyword instead
# -> only outputs 1, as the value


def c():
    n = 0
    while True:
        n += 1
        return n


print(c())
print(c())

# Generator --> case study: fib


def fib():
    first = 0
    last = 1
    while True:
        first, last = last, first + last
        yield first


f = fib()
f1 = next(f)
f2 = next(f)
f3 = next(f)

print(f"f1: {f1}\nf2: {f2}\nf3: {f3}")

# Generator --> case study: using
# generator in a for loop

for x in f:
    print(x)
    if x > 12:
        break

# Generator Comprehensions
list_nums = [x for x in range(100)]  # list comprehension
gen_nums = (x for x in range(100))  # generator object

print(list_nums)
print(gen_nums)

# checking size of mem used between
# list_nums & gen_nums
mem1 = sys.getsizeof(list_nums)
mem2 = sys.getsizeof(gen_nums)

print(f"mem1: {mem1}\nmem2: {mem2}")
