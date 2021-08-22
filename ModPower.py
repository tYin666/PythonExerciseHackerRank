if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())
    print(pow(a,b))
    if m >= 2:
        print(pow(a,b)%m)
    else: 
        print("m shall be a positiv value which greater than 2")