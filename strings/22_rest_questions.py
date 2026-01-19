def next_lexicographic(s):
    res = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            res += 'a' if ch == 'z' else chr(ord(ch) + 1)
        elif 'A' <= ch <= 'Z':
            res += 'A' if ch == 'Z' else chr(ord(ch) + 1)
        else:
            res += ch
    return res

def largest_word(s):
    words = s.split()
    if not words:
        return ""
    ans = words[0]
    for w in words:
        if len(w) > len(ans):
            ans = w
    return ans

def sort_characters(s):
    return "".join(sorted(s))

def count_words(s):
    return len(s.split())

def word_highest_repeated_letters(s):
    words = s.split()
    best_word = ""
    best_repeat = -1

    for w in words:
        freq = {}
        for ch in w:
            freq[ch] = freq.get(ch, 0) + 1

        max_in_word = max(freq.values())  # highest repetition in this word

        if max_in_word > best_repeat:
            best_repeat = max_in_word
            best_word = w

    return best_word



def toggle_case(s):
    res = ""
    for ch in s:
        if ch.islower():
            res += ch.upper()
        elif ch.isupper():
            res += ch.lower()
        else:
            res += ch
    return res

def concatenate_strings(s1, s2):
    return s1 + s2

def find_substring(s, sub):
    return s.find(sub)


def find_substring_1based(s, sub):
    idx = s.find(sub)
    return idx + 1 if idx != -1 else -1

def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)

print(next_lexicographic("abcz"))                 # bcda
print(largest_word("hi this is tamal"))           # tamal
print(sort_characters("tamal"))                   # aalm t? (sorted)
print(count_words("I am Tamal"))                  # 3
print(word_highest_repeated_letters("apple banana orange"))  # banana
print(toggle_case("TaMaL123"))                    # tAmAl123
print(concatenate_strings("hello", "world"))      # helloworld
print(find_substring("hello world", "world"))     # 6
print(reverse_words("I am Tamal"))                # Tamal am I