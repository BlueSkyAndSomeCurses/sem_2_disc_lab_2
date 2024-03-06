class Huffman:
    def encode(self, text: str) -> tuple[str, dict[str, str]]:
        probabilities = {
            char: float(f"{text.count(char) / len(text):.3f}") for char in text
        }
        tree = sorted(probabilities.items(), key=lambda pair: pair[1], reverse=True)

        tree_hist = [tree]

        while not len(tree_hist) or len(tree_hist[-1]) != 2:
            new_entry = tree_hist[-1][:]
            last_el = new_entry.pop(-1)
            new_entry[-1] = (new_entry[-1][0], last_el[0]), new_entry[-1][1] + last_el[
                1
            ]
            new_entry.sort(key=lambda pair: pair[1], reverse=True)
            tree_hist.append(new_entry)

        coding_dict = {tree_hist[-1][0]: 1, tree_hist[-1][1]: 0}

        tree_hist = tree_hist[::-1][1:]

        for node in tree_hist:
            for key, value in coding_dict.items():
                if key not in node:
                    print(key, node)

        return coding_dict

    def decode(self, code: str, coding_dict: dict[str, str]):
        pass


text = "asdfasdfdfsfaaaaafsdaaa"

haffman = Huffman()
encoded = haffman.encode(text)
print(encoded)
