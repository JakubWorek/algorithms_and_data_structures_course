import random

def twosum(T,X):
    i=0
    j=len(T)-1

    while i<len(T)-1 and j<len(T):
        if T[j]+T[i]==X:
            return True
        if T[j]+T[i]>X:
            j-=1
        if T[j]+T[i]<X:
            i+=1
    
    return False

def main():
    tab=[]

    for i in range(10):
        num=random.randint(1,100)
        tab.append(num)

    tab.sort()
    print(tab)
    x=int(input("X: "))
    print(twosum(tab,x))

if __name__ == "__main__": main()