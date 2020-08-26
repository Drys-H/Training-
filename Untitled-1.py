ls = [34, 5, 2, 35435, 2, -1, 34, 987, 43]
print(ls)

def add_1(l) : # increment EACH element of the list 
    for i in range(len(l)):
        l[i] = l[i] + 1 
    return l
    
def power2(l) : # square all the elements of the list     
    return [i**2 for i in l] # comprehensive list [op(i) for i in range(10)]

    res = []
    for i in range(len(ls)):  
        res.append(pow(ls[i],2))
    
    return res

def pop(l) : # remove the head of the list   
    l.pop(0)
    return l 

def add_elt(l) : # add an element at the end of the list   
    l.append(5)
    return l

def lenghtSimple(l) :     
    return len(l)

def lenght(l) : # process the lenght of the list
    counter=0
    for i in l:
       counter =+ 1
    return counter 
        
   
def insertAtSimple(l) :   
    l.insert(2,3)
    return l

def insertAt(l, n, elt) : # add an element to the list at the n index    
    res = []
    counter = 0
    for e in l:
        if counter == n: 
            res.append(elt)
        res.append(e)     
        counter =+ 1 
    return res

def removeTail(l) : # remove the last element of the list    
    res =[]
    i = 1
    res = l[: len(l) - i ]
    return res 
    
    #ls.remove(5)
    #return ls

func_list = [add_1, power2, pop, add_elt, lenghtSimple, lenght, insertAtSimple, insertAt, removeTail]

# ============== MAIN ========================

for func in func_list :
    print(func(ls))