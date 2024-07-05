def lz77_compress(data, window_size=20):
    i = 0
    output = []
    while i < len(data):
        match = ''
        best_pos = 0
        for j in range(max(0, i - window_size), i):
            k = 0
            while (i + k < len(data)) and (data[j + k] == data[i + k]):
                k += 1
            if k > len(match):
                match = data[j:j + k]
                best_pos = i - j
        if len(match) > 0:
            if i + len(match) < len(data):
                next_char = data[i + len(match)]
            else:
                next_char = ''
            output.append((best_pos, len(match), next_char))
            i += len(match) + 1
        else:
            output.append((0, 0, data[i]))
            i += 1
    return output


def lz77_decompress(compressed):
    output = []
    for pos, length, char in compressed:
        start = len(output) - pos
        for i in range(length):
            output.append(output[start + i])
        if char != '':
            output.append(char)
    return ''.join(output)


text = "abracadabra"
compressed = lz77_compress(text)
print(f"Compressed: {compressed}")
decompressed = lz77_decompress(compressed)
print(f"Decompressed: {decompressed}")
