def count_occurrences(phrase: str, letter: str) -> int:
        return phrase.lower().count(letter)
print(count_occurrences("Samsung is gnusmas", "s"))