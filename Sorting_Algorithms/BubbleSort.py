def BubbleSort(l:list,order:str='asc'):
    '''
    1st argument takes a list
    2nd kwargs defaults to 'asc' and takes either 'asc' for ascending and 'desc' for descending
    otherwise raises error
    '''
    #check order
    if order is None or order not in ['asc','desc']:
        raise ValueError('Order can only be \'asc\' or \'desc\'')

    if order=='asc':
        for i in range(len(l)):
            for j in range(1,len(l)-i):
                if l[j-1]>l[j]:
                    SwapItem(l,j-1,j)
    elif order=='desc':
        for i in range(len(l)):
            for j in range(1,len(l)-i):
                if l[j-1]<l[j]:
                    SwapItem(l,j-1,j)

    return l

def SwapItem(lst:list,idx1,idx2):
    temp=lst[idx1]
    lst[idx1]=lst[idx2]
    lst[idx2]=temp
    return

if __name__=='__main__':
    exList=[3,5,9,2,1,4,7,6,8]
    BubbleSort(exList,'asc')
    print(f'In Ascending Order:\n{exList}')
    BubbleSort(exList,'desc')
    print(f'In Descending Order:\n{exList}')