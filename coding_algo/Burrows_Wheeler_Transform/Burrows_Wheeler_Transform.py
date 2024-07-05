def bwt_transform(text):
    n = len(text)
    m = sorted(text[i:] + text[:i] for i in range(n))
    last_column = [row[-1] for row in m]
    return ''.join(last_column), m.index(text)


def bwt_inverse(last_column, index):
    n = len(last_column)
    table = [""] * n
    for i in range(n):
        table = sorted([last_column[i] + table[i] for i in range(n)])
    return table[index]


text = "banana"
transformed, index = bwt_transform(text)
print(f"Transformed: {transformed}, Index: {index}")
original = bwt_inverse(transformed, index)
print(f"Original: {original}")
