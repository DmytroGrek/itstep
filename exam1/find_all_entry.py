def find_all_entry(text, symbol):
    result = []
    for i, j in enumerate(text):
        if j == symbol:
            result.append(i)
    return result


print(find_all_entry("fdiutgd", 'd'))