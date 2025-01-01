#1004 成绩排名

def solution():
    cnt = int(input())
    max_score = 0
    max_name = ""
    max_id = ""
    min_score = 101
    min_name = ""
    min_id = ""
    for i in range(cnt):
        input_str = input().split(" ")
        score = int(input_str[2])
        if score > max_score:
            max_score = score
            max_name = input_str[0]
            max_id = input_str[1]
        if score < min_score:
            min_score = score
            min_name = input_str[0]
            min_id = input_str[1]

    print(f"{max_name} {max_id}")
    print(f"{min_name} {min_id}")

if __name__ == "__main__":
    solution()