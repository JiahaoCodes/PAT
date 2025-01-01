# 1006 换个格式输出整数

def solution():
    digit_str = "123456789"
    n = input()
    result = ""
    length = len(n)
    if length == 3:
        result += str("B"*int(n[0]))
    if length >= 2:
        result += str("S"*int(n[-2]))
    result += digit_str[:int(n[-1])]
    print(result)

if __name__ == "__main__":
    solution()
