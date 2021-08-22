def count_substring(string, sub_string):
    count = 0
    res_string = string
    
    while (res_string.find(sub_string) != -1):
        i = res_string.find(sub_string)
        res_string = res_string[i+1: len(string)] 
        count = count+1 

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)