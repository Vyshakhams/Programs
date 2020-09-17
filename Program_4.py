list_a = ['python', 'pyhton3', 'user1', 'assignment', 'user', 'user1', 'python', 'User1']
dictionary = {}

def getWords(a_list):
    
    for i in a_list:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    
    return dictionary     
    
result = getWords(list_a)
print(result)  
