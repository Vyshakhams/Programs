#sentence = "hello world and practice makes perfect and hello world again"
sentence = str(input("Enter sentence to sort"))


def sortingFun(sentence):
    sentence_list = []
    tmp=''
    for char in sentence:
        if char == ' ':
            sentence_list += [tmp]
            tmp=''
        else:
            tmp += char
    if tmp:
        sentence_list += [tmp]
    
    new = []
    for i in sentence_list:
        if i not in new:
            new += [i]
        
    for i in range(len(new)-1,0,-1):
        for  j in range(i):
            if new[j]>new[j+1]:
                temp = new[j]
                new[j] = new[j+1]
                new[j+1] = temp
                
    finalResult = ''
    last = len(new)-1
    for pos, elem in enumerate(new):
        finalResult += str(elem)
        if pos != last:
            finalResult+=" "            
    return finalResult


fin_res = sortingFun(sentence)
print(fin_res)                    




 