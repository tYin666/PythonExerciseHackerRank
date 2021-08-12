if __name__ == '__main__':
    
    L = []
    n = int(input())
    for i in range(n):
        for j in range(2):
            name = input()
            score = float(input())
            L.append([name, score])
        if i == n-1 and j == 1:
            break
    print(L)