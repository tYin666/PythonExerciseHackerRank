def solve(s):
    lis = s.split(' ')
    #print(lis)
    str0 = ''
    res_str = ""

    for i in range(len(lis)):
        temp_lis = list(lis[i])
        temp_str = ''
        print(temp_lis)
        index_firstC = 0
        for j in range(len(temp_lis)):
            temp_string = ''.join(temp_lis[j])
            print(temp_string)
            if temp_string.isalnum() == True:
                if temp_string.isalpha() == True:
                    index_firstC = j
                    str0 = temp_lis[j].upper()  
                    temp_lis.pop(index_firstC)
                    temp_lis.insert(index_firstC, str0)
            break                  
        print(temp_lis)
        temp_str = ''.join(temp_lis)  
        if i > 0:  
            res_str = res_str + ' ' + temp_str
        else:
            res_str = temp_str
    return res_str

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()
    s = "1 2 2 3 4 5 6 7 8  9"

    result = solve(s)

    print(result)
    #fptr.write(result + '\n')

    #fptr.close()