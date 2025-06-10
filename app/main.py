def count_occurrences(phrase: str, letter: str) -> int:
        phrase_lover = phrase.lower()
        counter = phrase_lover.count(letter.lower())
        return counter
#print(count_occurrences("Samsung is gnusmas", "s"))