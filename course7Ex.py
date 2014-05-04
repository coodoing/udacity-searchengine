a=[1,2,3]
a.append(230)

print(a)
def explode_list(p,n):
    result=[]
    if n==0:
        return []
    else:
        if p!=[]:
            for entry in p:
                k = n # after each loop, just restore the k to n
                while k>0:
                    result.append(entry)
                    k-=1
            return result
print (explode_list([1, 2, 3], 2))
print (explode_list([1, 0, 1], 0))
print (explode_list(["super"], 5))



def reverse_index(dict):
    result = {}
    for entry in dict:
        if dict[entry] not in result:
            result[dict[entry]] = [entry]
        else:        
            #print(result[dict[entry]])
            result[dict[entry]].append(entry)
    return result

winners_by_year = {
    1930: 'Uruguay', 1934: 'Italy', 1938: 'Italy', 1950: 'Uruguay',
    1954: 'West Germany', 1958: 'Brazil', 1962: 'Brazil', 1966: 'England',
    1970: 'Brazil', 1974: 'West Germany', 1978: 'Argentina',
    1982: 'Italy', 1986: 'Argentina', 1990: 'West Germany', 1994: 'Brazil',
    1998: 'France', 2002: 'Brazil', 2006: 'Italy', 2010: 'Spain' }
wins_by_country = reverse_index(winners_by_year)
print (wins_by_country['Brazil'])
print (wins_by_country['England']) 




def is_list(p):
    return isinstance(p, list)

def same_structure(a,b):
    if is_list(a)==False and is_list(b)==False:
        return True
    elif is_list(a)==True and is_list(b)==False:
        return False
    elif is_list(a)==False and is_list(b)==True:
        return False
    else:
        if len(a)!=len(b):
            return False
        else:
            i=0
            while i<len(a):
                if same_structure(a[i],b[i])==False:
                    return False
                i+=1
            return True   
        


print (same_structure(3, 7))
#>>> True
print (same_structure([1, 0, 1], [2, 1, 2]))
#>>> True
print (same_structure([1, [0], 1], [2, 5, 3]))
#>>> False
print (same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['d', 'e']]]]))
#>>> True
print (same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['de']]]]))
#>>> False
