a = [1,2,55,1,3,2,34,55]
b=[]

def removeDuplicate(a):
    global b 
    for i in range(0,len(a)-1):
        if a[i] not in b:
            b = b + [a[i]]
            
    return b    

result = removeDuplicate(a)   
print(result)  