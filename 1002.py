# 1002 写出这个数

def solution():
    pinyin_map = {0:"ling", 1:"yi", 2:"er", 3:"san", 4:"si", 5:"wu", 6:"liu", 7:"qi", 8:"ba", 9:"jiu"}
    sum = 0
    input_str = input()

    for char in input_str:
        sum += int(char)

    sum_str = str(sum)

    count = 0
    for digit in sum_str:
        count += 1
        print(pinyin_map[int(digit)], end = "" if count == len(sum_str) else " ")

if __name__ == '__main__':
    solution()