## problem 3
## part a
def is_reflexive(A, R):
    for x in A:
        if not (R(x, x)):
            return False
    return True
    
## part b
def is_injective(domain, f):
    for x1 in domain:
        for x2 in domain:
            if x1 != x2:
                if f(x1) == f(x2):
                    return False
    return True
        
            

## part c
def is_transitive(A, R):
    for x in A:
        for y in A:
            for z in A:
                if not ((R(x,y) and R(y,z)) <= R(x,z)):
                    return False
    return True

## problem 4
## part a
def are_parts_nonoverlapping(p):
    for i in range(len(p)):
        for j in p[i]:
            for k in p[(i+1):]:
                if j in k:
                    return False
    return True
    

## part b
def do_parts_contain_element(x, p):
    for i in range(len(p)):
        if x in p[i]:
            return True
    return False

## part c
def do_parts_cover_set(s, p):
    for n in s:
        if not do_parts_contain_element(n, p):
            return False
    return True 
            
## part d
def do_parts_have_nothing_extra(s, p):
    for i in p:
        for j in i:
            if j not in s:
                return False
    return True

## part e
def is_partition(s, p):
    if do_parts_have_nothing_extra(s, p):
        count_of_p = 0
        for i in p:
            count_of_p += len(i)
        if count_of_p == len(s):
            return True
    return False
        
            
    

                       
        
    




    
