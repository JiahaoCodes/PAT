# 1001 害死人不偿命（3n+1）猜想

def solution():
    cnt = 0
    n = int(input())
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = (3*n + 1)//2
        cnt += 1

    print(cnt)

if __name__ == '__main__':
    solution()