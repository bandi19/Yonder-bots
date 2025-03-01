def fst_non_repeating(s):
        for char in s:
            if s.count(char) == 1:
                return char
        return None

print(fst_non_repeating("chess"))