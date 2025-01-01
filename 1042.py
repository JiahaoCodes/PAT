# 1042 字符统计

import string

def solution():
    input_str = input()
    char_count = {}
    input_str = input_str.lower()
    max_count = 0

    for char in input_str:
        if 'a' <= char <= 'z':
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
            max_count = max(max_count, char_count[char])

    for letter in string.ascii_lowercase:
        if letter in char_count and char_count[letter] == max_count:
            print(f"{letter} {max_count}")
            break

if __name__ == '__main__':
    solution()