def split_and_join(line):
    # write your code here
    lis = line.split(" ")
    s_res = "-".join(str(e) for e in lis)
    return s_res

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)