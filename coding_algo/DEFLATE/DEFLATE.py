import zlib


def deflate_compress(data):
    return zlib.compress(data.encode())


def deflate_decompress(data):
    return zlib.decompress(data).decode()


text = "this is an example for DEFLATE compression"
compressed = deflate_compress(text)
print(f"Compressed: {compressed}")
decompressed = deflate_decompress(compressed)
print(f"Decompressed: {decompressed}")
