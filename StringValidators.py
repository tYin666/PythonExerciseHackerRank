if __name__ == '__main__':
    s = input()
    
    s_hasAlnum = False
    s_hasAlpha = False
    s_hasDigit = False
    s_hasLower = False
    s_hasUpper = False 
    
    for i in range(len(s)):
        s_new = s[i];
        if s_new.isalnum():
            s_hasAlnum = True
        if s_new.isalpha():
            s_hasAlpha = True
        if s_new.isdigit():
            s_hasDigit = True
        if s_new.islower():
            s_hasLower = True
        if s_new.isupper():
            s_hasUpper = True
            
    print (s_hasAlnum)
    print (s_hasAlpha)
    print (s_hasDigit)
    print (s_hasLower)
    print (s_hasUpper)