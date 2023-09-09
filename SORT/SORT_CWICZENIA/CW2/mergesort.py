# czasowa: O(n log n), pamieciowa O(n)
def mergesort(nums, L=0, P=None):
    arr=[] #pomocnicza tablica do scalania
    for x in range(len(nums)): arr.append(0)

    if(P==None): 
        P=len(nums)-1
        
    s=(L+P)//2 #indeks srodka tablicy

    #dzielimy ciag na 2 czesci jezeli ma wiecej niz 1 element
    if(L<s): mergesort(nums,L,s)
    if(P>s+1): mergesort(nums,s+1,P)

    #scalanie
    i1=L
    i2=s+1

    for i in range(L,P+1): #scalamy do pomocniczej tablicy
        if( ((nums[i1]<nums[i2]) and (i1<=s)) or (i2>P) ):
            arr[i]=nums[i1] #bierzemy wartosc z lewego ciagu
            i1+=1
        else:
            arr[i]=nums[i2] #bierzemy wartosc z prawego ciagu
            i2+=1

    for j in range(L,P+1): nums[j]=arr[j]