# 1003 我要通过

def is_valid(s):
    af = am = ab = 0
    Pindex = Tindex = -1
    for i, char in enumerate(s):
        if char == 'P':
            if Pindex == -1:
                Pindex = i
            else:
                return False
        elif char == 'T':
            if Tindex == -1:
                Tindex = i
            else:
                return False
        elif char == 'A':
            if Pindex == -1 and Tindex == -1:
                af += 1
            elif Pindex != -1 and Tindex == -1:
                am += 1
            elif Pindex != -1 and Tindex != -1:
                ab += 1
        else:
            return False
    if am == 0 or af*am != ab or Pindex > Tindex:
        return False
    return True

def solution():
    cnt = int(input())
    for i in range(cnt):
        input_str = input()
        print("YES" if is_valid(input_str) else "NO", end="\n")

if __name__ == '__main__':
    solution()