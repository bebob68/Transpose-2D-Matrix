
# Python script to get transpose elements of two dimension list or a matrix
# the script will return a list containing transposed elements
def transpose(lst): 
    lst2 = []
    # iterate over list lst to the length of an item  
    for i in range(len(lst[0])): 
        # print(i) 
        row =[] 
        for item in lst: 
            # appending to new list with values and index positions 
            # i contains index position and item contains values 
            row.append(item[i]) 
        lst2.append(row) 
    return lst2 
  
# Run this code  
mtx = [[7,2,1,0,], [5, 1, 8, 2], [9, 0, 5, 7]] 
print(transpose(mtx) 
