correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]


def check_sudoku(li):
    i,j = 0,0
    result_row,result_column = 0,0
    column=[[]]
    row=[]
    n = len(li)
    
    while i<n:
        column = []
        while j<n:
            column.append(li[j][i])
            j = j+1    
        result_row = check_row(li[i])+result_row
        result_column = check_column(column)+result_column
        i = i+1        
    if result_row==n and result_column == n:
        return True;
    return False
        
        
def check_column(li):
    i = 0
    result = 0
    while i<len(li):
        if i+1 in li and li.count(i+1)==1:
            result = result+1
        i =i+1
    if result ==len(li):
        return 1
    return 0    

def check_row(li):
    i = 0
    result = 0
    while i<len(li):
        if i+1 in li and li.count(i+1)==1:
            result = result+1
        i =i+1
    if result ==len(li):
        return 1
    return 0    

print(check_sudoku(correct))
print(check_sudoku(incorrect))
