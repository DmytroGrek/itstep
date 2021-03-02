def get_next_multiple(num):
    result = 0
    while True:
        result += num
        yield result


gen_multiple_of_two = get_next_multiple(2)
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))


gen_multiple_of_thirteen = get_next_multiple(13)
print(next(gen_multiple_of_thirteen))
print(next(gen_multiple_of_thirteen))
print(next(gen_multiple_of_thirteen))
print(next(gen_multiple_of_thirteen))
