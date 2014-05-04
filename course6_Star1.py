a={'1': 2,'3': 4}
print(a.get('3'))
b = [1, 2]
b.extend('hey')
b.extend([])
print(b)

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'], 
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'], 
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'], 
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'], 
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'], 
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'], 
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'], 
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] } 

def ancestors(genealogy, person):
    #if genealogy.get(person)==None:
        #return []
    #if genealogy.get(genealogy[person][0])==[] and genealogy.get(genealogy[person][1])==[]:
        #return genealogy[person]
    #else:
        #return genealogy[person].extend(ancestors(genealogy,genealogy[person][0])).extend(ancestors(genealogy,genealogy[person][1]))
    if person not in genealogy:
        return []
    else:
        #print(person)
        #print(genealogy[person])
        for entry in genealogy[person]:                    
            #genealogy[person].extend(ancestors(genealogy,entry))
            if entry in genealogy:
                for x in genealogy[entry]:
                    if x not in genealogy[person]:
                        genealogy[person].extend(ancestors(genealogy,entry))
    return genealogy[person]


print(ancestors(ada_family, 'Dave'))
print(ancestors(ada_family, 'Augusta Ada King'))
#>>> ['Anne Isabella Milbanke', 'George Gordon Byron', 
#    'Catherine Gordon','Captain John Byron']

print(ancestors(ada_family, 'Judith Blunt-Lytton'))
#>>> ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King', 
#    'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron', 
#    'Catherine Gordon', 'Captain John Byron']
