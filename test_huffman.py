


text = "zxcsafjiucoqiwemrcjqklqadf"

haffman = Huffman()
encoded, coding_dict = haffman.encode(text)
print(encoded)
print(coding_dict)
decoded = haffman.decode(encoded, coding_dict)
print(decoded == text)
