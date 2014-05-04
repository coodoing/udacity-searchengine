ar= [1,2,3]
ar.append(230)
#print(ar) #do not print ar.append(230) directly, otherwise it will return None
b=[]
b.append([1])
#print(b)

def triangle(n):    
    #valueN=[] #value of row N
    result = []
    #col = n
    if n==0:
        return []
    elif n ==1:
        return [[1]]
        #return [].append([1])
    else:
        for i in range(n):
            k=i+1  #be carefule about the value K
            valueN=[]
            #print(k,n)
            for j in range(k):
                if j==0 or j==k-1:
                    valueN.append(1)
                else:
                    #print('MM')
                    temp = triangle(k-1)
                    #print('NN')
                    #print(temp[k-2][j-1])
                    #print(temp[k-2][j])
                    valueN.append(temp[k-2][j-1]+temp[k-2][j])
                #print(valueN)# the current value of row K
            #print(valueN) # after the Kth loop, get all value of row K
            result.append(valueN) # get the final result
        #print(result)  #after all loop, get the final list 
        return result
    
print (triangle(0))
#>>> []

print (triangle(1))
#>>> [[1]]

print (triangle(2))
#>> [[1], [1, 1]]

print (triangle(3))
#>>> [[1], [1, 1], [1, 2, 1]]

print (triangle(6))
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]





