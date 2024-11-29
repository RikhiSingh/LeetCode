def hunddigit():
    numarr =[]
    
    for i in range(1,100):
        numarr.append(i)
    
    
    strarr = ''.join(map(str, numarr))
    
    return strarr[100]

print(hunddigit())