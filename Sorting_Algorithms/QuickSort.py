def QuickSort(l:list,order:str='asc'):
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
    if l[0]<l[mid]:
        if l[mid]<l[-1]:
            pivot=mid
        elif l[-1]>l[0]:
            pivot=len(l)-1
        else: 
            pivot=0
    else:
        if l[0]<l[-1]:
            pivot=0
        elif l[-1]>l[mid]:
            pivot=len(l)-1
        else:
            pivot=mid

    if order=='asc':
        l=QuickAsc(l,pivot)
    elif order=='desc':
        l=QuickDesc(l,pivot)

    left=l[:pivot]
    right=l[pivot:]

    leftSorted=QuickSort(left,order)
    rightSorted=QuickSort(right,order)
    l=leftSorted+rightSorted
    return l

def QuickAsc(a:list,pivot:int):
    if pivot!=0:
        SwapItem(a,0,pivot)
        pivot=0
    j=0
    for i in range(1,len(a)):
        if a[i]<a[pivot]:
            j+=1
            SwapItem(a,i,j)
    SwapItem(a,pivot,j)
    return a


def QuickDesc(a:list,pivot:int):
    if pivot!=0:
        SwapItem(a,0,pivot)
        pivot=0
    j=0
    for i in range(1,len(a)):
        if a[i]>a[pivot]:
            j+=1
            SwapItem(a,i,j)
    SwapItem(a,pivot,j)
    return a

def SwapItem(lst:list,idx1,idx2):
    if idx1!=idx2:
        temp=lst[idx1]
        lst[idx1]=lst[idx2]
        lst[idx2]=temp
    return

if __name__=='__main__':
    exList=[3,5,9,2,1,4,7,6,8]
    print(exList)
    # print(f"Original Array:\n{exList}")
    exList=QuickSort(exList,'asc')
    print(f'In Ascending Order:\n{exList}')
    exList=QuickSort(exList,'desc')
    print(f'In Descending Order:\n{exList}')