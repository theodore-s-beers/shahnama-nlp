import json
from collections import Counter

from hazm import Lemmatizer, Normalizer, word_tokenize


def main():
    normalizer = Normalizer()
    lemmatizer = Lemmatizer()

    lemma_counts: Counter[str] = Counter()

    with open("hemistichs.txt", "r", encoding="utf-8") as f:
        for line in f:
            normalized = normalizer.normalize(line.strip())
            tokens = word_tokenize(normalized)
            for token in tokens:
                lemma = lemmatizer.lemmatize(token)
                lemma_counts[lemma] += 1

    sorted_items = sorted(lemma_counts.items(), key=lambda item: item[1], reverse=True)
    lemma_counts_ordered = dict(sorted_items)

    with open("lemma_counts.json", "w", encoding="utf-8") as f:
        json.dump(lemma_counts_ordered, f, ensure_ascii=False, indent=2)

    verb_lemma_counts = {k: v for k, v in lemma_counts_ordered.items() if "#" in k}
    with open("verb_lemma_counts.json", "w", encoding="utf-8") as f:
        json.dump(verb_lemma_counts, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
