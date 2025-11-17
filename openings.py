import json
from collections import Counter

from hazm import Normalizer, word_tokenize


def main():
    normalizer = Normalizer()

    opening_ones: Counter[str] = Counter()
    opening_twos: Counter[str] = Counter()
    opening_threes: Counter[str] = Counter()
    opening_fours: Counter[str] = Counter()

    with open("hemistichs.txt", "r", encoding="utf-8") as f:
        for line in f:
            normalized = normalizer.normalize(line.strip())
            tokens = word_tokenize(normalized)

            if len(tokens) >= 1:
                opening_ones[tokens[0]] += 1
            if len(tokens) >= 2:
                opening_twos[" ".join(tokens[:2])] += 1
            if len(tokens) >= 3:
                opening_threes[" ".join(tokens[:3])] += 1
            if len(tokens) >= 4:
                opening_fours[" ".join(tokens[:4])] += 1

    # Filter for >= 2 occurrences, sort descending, save to JSON
    for name, counter in [
        ("opening_ones", opening_ones),
        ("opening_twos", opening_twos),
        ("opening_threes", opening_threes),
        ("opening_fours", opening_fours),
    ]:
        filtered = {k: v for k, v in counter.items() if v >= 2}
        sorted_items = sorted(filtered.items(), key=lambda item: item[1], reverse=True)
        ordered = dict(sorted_items)

        with open(f"{name}.json", "w", encoding="utf-8") as f:
            json.dump(ordered, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
