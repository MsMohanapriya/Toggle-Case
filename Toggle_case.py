def ToggleCase(string):
    # new_str=[]
    # for i in range(len(string)):
    #     if ord(string[i])>=65 and ord(string[i])<=90:
    #        new_str.append( chr(ord(string[i])+32))
        
    #     if ord(string[i])>=97 and ord(string[i])<=122:
    #        new_str.append( chr(ord(string[i])-32))
    #     else:
    #         new_str.append(string[i])
    
    # return ''.join(new_str)
    
    string=list(string)
    for i in range(len(string)):
        string[i]=chr(ord(string[i])^(1<<5))
        
    return ''.join(string)
    
    
string=input("enter string: ")
print(ToggleCase(string))
