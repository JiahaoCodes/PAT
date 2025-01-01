# 1011 A+B和C

def solution():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        if a + b > c:
            print("Case #%d: true" % (i + 1))
        else:
            print("Case #%d: false" % (i + 1))

if __name__ == "__main__":
    solution()
