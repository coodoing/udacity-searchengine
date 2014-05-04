index = []

def add_to_index(index,keyword,url): 
    i=0    
    flag = 1
    keylist = ['',[]]
    n = len(index)
    while i<n:
        if keyword in index[i][0]:
            #print(index[i][1])
            index[i][1].append(url)
            flag = 0        
        i = i+1
    if flag==1:
        keylist[0]=keyword
        keylist[1].append(url)
        index.append(keylist)

def add_to_index2(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])        
    
    
add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print(index) 
# [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]


indexs = [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    i = 0
    while i<len(index):
        if keyword in index[i][0]:
            result = index[i][1]
            return result
        i = i+1
    return []

print(lookup(indexs,"udacity"))

str="this is a test"
print(str.split())
