from argparse import ArgumentError
from signal import set_wakeup_fd


def SelectSort(l:list,order:str='asc'):
    '''
    1st argument takes a list
    2nd kwargs defaults to 'asc' and takes either 'asc' for ascending and 'desc' for descending
    otherwise raises error
    '''
    #check order

    if order is None or order not in ['asc','desc']:
        raise ArgumentError
    for i in range(len(l)):
        for j in range(i+1,len(l)): #iterate over rest of the list
            if order=='asc':
                if l[i]>l[j]:
                    SwapItem(l,i,j)
            elif order=='desc':
                if l[i]<l[j]:
                    SwapItem(l,i,j)
    return l

def SwapItem(lst:list,idx1,idx2):
    temp=lst[idx1]
    lst[idx1]=lst[idx2]
    lst[idx2]=temp
    return

if __name__=='__main__':
    exList=[3,5,9,2,1,4,7,6,8]
    SelectSort(exList,'asc')
    print(f'In Ascending Order:\n{exList}')
    SelectSort(exList,'desc')
    print(f'In Descending Order:\n{exList}')