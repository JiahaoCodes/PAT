# 1008 数组循环右移问题

def revert_range(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def solution():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    m = m%n
    revert_range(arr, 0, n-1)
    revert_range(arr, 0, m-1)
    revert_range(arr, m, n-1)
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    solution()
