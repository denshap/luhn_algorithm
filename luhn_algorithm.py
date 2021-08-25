def luhn(str):
    str=str.replace(' ','')
    result=False
    if(str.isdigit() and len(str)>1):
        sum=0
        odd=True
        for i in range(len(str),0,-1):
            if(odd):
                sum+=int(str[i-1])
            else:
                sum+=int(str[i-1])*2
                if(int(str[i-1])*2 > 9):
                    sum-=9
            odd=not odd   
        result= (sum%10==0)    
    return result 

print(luhn(input()))

