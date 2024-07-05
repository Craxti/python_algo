def rle_encode(data):
    encoding = ""
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        encoding += data[i] + str(count)
        i += 1
    return encoding


def rle_decode(data):
    decoding = ""
    i = 0
    while i < len(data):
        char = data[i]
        count = int(data[i + 1])
        decoding += char * count
        i += 2
    return decoding


text = "AAAABBBCCDAA"
encoded = rle_encode(text)
print(f"Encoded: {encoded}")
decoded = rle_decode(encoded)
print(f"Decoded: {decoded}")
