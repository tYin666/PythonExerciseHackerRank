def swap_case(s):
    list = []
    for i in range(len(s)):
        s_char = s[i]
        if s_char.islower():
            list.append(s_char.upper())
        elif s_char.isupper():
            list.append(s_char.lower())
        else:
            list.append(s_char)
    
    s_rec = ''.join(str(e) for e in list)
    return s_rec

if __name__ == '__main__':
   # s = input()
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)