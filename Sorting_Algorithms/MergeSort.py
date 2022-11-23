def MergeSort(l:list,order:str='asc'):
    '''
    1st argument takes a list
    2nd kwargs defaults to 'asc' and takes either 'asc' for ascending and 'desc' for descending
    otherwise raises error
    '''
    #check order
    if order is None or order not in ['asc','desc']:
        raise ValueError('Order can only be \'asc\' or \'desc\'')
    #set up base case
    if len(l)<2:
        return l

    mid=len(l)//2
    left=l[:mid]
    right=l[mid:]

    leftSorted=MergeSort(left,order)
    rightSorted=MergeSort(right,order)
    if order=='asc':
        l=MergeAsc(leftSorted,rightSorted)
    elif order=='desc':
        l=MergeDesc(leftSorted,rightSorted)

    return l

def MergeAsc(a:list,b:list):
    i=j=0
    arr=[]
    while(i<len(a) and j<len(b)):
        if a[i]<b[j]:
            arr.append(a[i])
            i+=1
        else:
            arr.append(b[j])
            j+=1
            
    #adding leftover elements
    while(i<len(a)):
        arr.append(a[i])
        i+=1
    while(j<len(b)):
        arr.append(b[j])
        j+=1

    return arr
def MergeDesc(a:list,b:list):
    i=j=0
    arr=[]
    while(i<len(a) and j<len(b)):
        if a[i]>b[j]:
            arr.append(a[i])
            i+=1
        else:
            arr.append(b[j])
            j+=1

    #adding leftover elements
    while(i<len(a)): 
        arr.append(a[i])
        i+=1
    while(j<len(b)):
        arr.append(b[j])
        j+=1 
    return arr

if __name__=='__main__':
    exList=[3,5,9,2,1,4,7,6,8]
    print(f"Original Array:\n{exList}")
    exList=MergeSort(exList,'asc')
    print(f'In Ascending Order:\n{exList}')
    exList=MergeSort(exList,'desc')
    print(f'In Descending Order:\n{exList}')