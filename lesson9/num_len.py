# по простому
def num_len(num):
    return len(str(num))


print(num_len(34567))


# посложнее
def num_len(num):
    result = []
    for elem in str(num):
        if elem.isdigit():
            result += elem
    return len(result)


print(num_len(34567))
print(num_len(34567.0))
print(num_len(-34567.0))
print(num_len('345hgf7'))
