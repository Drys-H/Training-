ls = [34, 5, 2, 35435, 2, -1, 34, 987, 43]
print(ls)

def add_1(l) : # increment EACH element of the list 
    for i in range(len(ls)):
        ls[i] = ls[i] + 1 
    return ls
    
def power2(l) : # square all the elements of the list     
    return [i**2 for i in ls] 

    #res = []
    #for i in range(len(ls)):  
        #res = pow(i,2)
    
    #return res

def pop(l) : # remove the head of the list   
    ls.pop(0)
    return ls 

def add_elt(l) : # add an element at the end of the list   
    ls.append(5)
    return ls

def lenghtSimple(l) :     
    elt = len(ls)
    return elt

def lenght(l, n) : # process the lenght of the list
    pass
    


def insertAtSimple(l) :   
    ls.insert(2,3)
    return ls

def insertAt(l, n, elt) : # add an element to the list at the n index 
    pass 





def removeTail(l) : # remove the last element of the list    
    res =[]
    i = 1
    res = ls[: len(ls) - i ]
    return res 
    
    #ls.remove(5)
    #return ls

func_list = [add_1, power2, pop, add_elt, lenghtSimple, lenght, insertAtSimple, insertAt, removeTail]

# ============== MAIN ========================

for func in func_list :
    print(func(ls))