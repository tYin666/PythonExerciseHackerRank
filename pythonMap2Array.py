if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    if 2<=n<=10: 
        arr_list = list(arr)
        arr_list.sort()
        max_value = arr_list[n-1]
        for i in range(1,n):
            if arr_list[n-i-1] != max_value:
                print(arr_list[n-i-1])
                break       
    else:
        print('the number is out of range')