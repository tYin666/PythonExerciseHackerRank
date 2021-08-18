def mutate_string(string, position, character):
    lis = list(string)
    lis[position] = character
    string_new = ''.join(lis)
    return string_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)