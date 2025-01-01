# 1005 继续(3n+1)猜想

def solution():
    count_arr = [0] * 101
    count_arr[0] = int(input())
    numbers = input().split()
    for i in range(count_arr[0]):
        number = int(numbers[i])
        if(count_arr[number] == 0):
            count_arr[number] = 1
        while(number != 1):
            if(number%2 == 0):
                number = number // 2
            else:
                number = (3*number + 1) // 2
            if(number < 100):
                count_arr[number] = 2
    format_flag = 0
    for i in range(100,0,-1):
        if(count_arr[i] == 1):
            if(format_flag == 0):
                print(i,end='')
                format_flag = 1
            else:
                print(' '+str(i),end='')
            

if __name__ == '__main__':
    solution()