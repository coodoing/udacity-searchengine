import time

def time_excute(code):
    start = time.clock()
    result = eval(code)
    spend = time.clock()-start
    return result,spend

print(time_excute("1+45"))
print(12%3)
print(ord('a')%ord('a'))
print((ord('z')+3)%ord('z'))
print(ord(chr(3)))
print(chr(3))
print(ord('3'))
print(chr(ord('3')))




#Define a procedure,

#hashtable_lookup(htable,key)

#that takes two inputs, a hashtable
#and a key (string),
#and outputs the value associated
#with that key.

def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return
    bucket.append([key, value])

def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None





def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])    


def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table








    
def list_to_dic(htable):
    table={}
    for pair in htable:
        if pair !=[]:
            table[pair[0][0]]=pair[0][1]
    return table

            
def hashtable_update2(htable, key, value):
    htable[key]=value

def hashtable_lookup2(htable, key):
    #print htable
    return htable[key]





table = make_hashtable(10)
hashtable_update(table, 'Python', 'Monty')
hashtable_update(table, 'CLU', 'Barbara Liskov')
hashtable_update(table, 'JavaScript', 'Brendan Eich')
hashtable_update(table, 'Python', 'Guido van Rossum')
print(hashtable_lookup(table, 'Python'))
dic = list_to_dic(table)
print(hashtable_lookup2(dic, 'Python'))
#print hashtable_update2(htable, key, value)

