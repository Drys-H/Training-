def add_1(l) : # increment EACH element of the list 
    for i in range(len(l)):
        l[i] = l[i] + 1 
    return l
    
def power2(l) : # square all the elements of the list     
    return [i**2 for i in l] # comprehensive list [op(i) for i in range(10)]


def pop(l) : # remove the head of the list   
   # l.pop(0)
    res = l[1:]
    return res 

def add_elt(l, n) : # add an element at the end of the list   
    l.append(n)
    return l

def lenghtSimple(l) :     
    return len(l)

def lenght(l) : # process the lenght of the list
    counter = 0
    for _ in l :  
       counter += 1
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
    res = []
    i = 1
    res = l[: len(l) - i ]
    return res 
    
    #ls.remove(5)
    #return ls


# ============== MAIN ========================
if __name__ == "__main__" : 
    ls = [34, 5, 2, 35435, 2, -1, 34, 987, 43]
    print(ls)


    print(f"add_1 : {add_1(ls)}")
    
    print(f"power2 : {power2(ls)}") # square all the elements of the list     


    print(f"pop : {pop(ls)}") # remove the head of the list   


    print(f"add_elt : {add_elt(ls, -1)}") # add an element at the end of the list   

    print(f"lenghtSimple : {lenghtSimple(ls)}")     


    print(f"lenght : {lenght(ls)}") # process the lenght of the list

        
   
    print(f"insertAtSimple : {insertAtSimple(ls)}")   


    print(f"insertAt : {insertAt(ls, 3, -1)}") # add an element to the list at the n index    


    print(f"removeTail : {removeTail(ls)}") # remove the last element of the list