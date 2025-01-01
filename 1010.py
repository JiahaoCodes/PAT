# 1010 一元多项式求导

def solution():
    arr = list(map(int, input().split()))
    length = len(arr) // 2
    flag = 0
    for i in range(length):
        if(arr[2*i+1]):
            if flag:
                print(" ", end="")
            print(arr[2*i] * arr[2*i+1], arr[2*i+1] - 1, end="")
            flag = 1
    if not flag:
        print("0 0")

if __name__ == "__main__":
    solution()
