if __name__ == '__main__':
    n = int(input())
    if  1<=n<=150:
        convertStr = ''
        for i in range(1,n+1):
            convertStr += str(i)
        print(convertStr)
    else:
        print('the input number is out of range')  
        