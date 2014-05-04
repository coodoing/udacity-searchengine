seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))
print(10000+True)
print(seasons[-1])
print([2]+[0]*5)
d={}
d[1,0]=5
print(d)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")


#recursive



def edit_distance(s, t):
    if s == t:
        return 0
    if len(s) < len(t):
        return edit_distance(t, s)
    previous = range(len(t) + 1)
    for row, col in enumerate(s):
        temp = [row + 1]
        #print("temp list:")
        #print(temp)
        for row2, col2 in enumerate(t):
            insertions = previous[row2 + 1] + 1
            #print(previous[row2 + 1] )
            deletions = temp[row2] + 1
            replacing = previous[row2] + (col != col2)            
            temp.append(min(insertions, deletions, replacing))
        previous = temp 
    return previous.pop()

print("edit_distance:")
print (edit_distance('audacity', 'udacity'))
print (edit_distance('audacity', 'Udacity'))
print (edit_distance('peter', 'sarah'))
print(edit_distance('pete', 'peter'))




def edit_distance2(s, t):
    d = {}
    s=' '+s
    t=' ' +t
    S ,T= len(s), len(t)
    for i in range(S):
        d[i, 0] = i
    for j in range (T):
        d[0, j] = j
    for j in range(1,T):
        for i in range(1,S):
            d[i, j] = min(d[i-1, j] + 1, d[i, j-1] + 1, d[i-1, j-1] + (s[i] != t[j]))
    return d[S-1, T-1]
print("edit_distance2:")
print (edit_distance2('audacity', 'udacity'))
print (edit_distance2('audacity', 'Udacity'))
print (edit_distance2('peter', 'sarah'))
print(edit_distance2('pete', 'peter'))


    
def levenshtein(a,b):
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space.
        # Not really important to the algorithm anyway.
        a,b = b,a
        n,m = m,n
    current = range(n+1)    
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]+(a[j-1] != b[i-1])
            current[j] = min(add, delete, change)

    return current.pop()
print("levenshtein:")
print (levenshtein('audacity', 'udacity'))
print (levenshtein('audacity', 'Udacity'))
print (levenshtein('peter', 'sarah'))
print(levenshtein('pete', 'peter'))


