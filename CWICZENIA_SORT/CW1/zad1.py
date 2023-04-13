import random

def bubblesort(A):
    n=len(A)
    for i in range(n):
        for j in range(n-i):
            if A[j-1]>A[j]:
                A[j],A[j-1]=A[j-1],A[j]

def main():
    tab=[]

    for i in range(10):
        num=random.randint(1,100)
        tab.append(num)

    print(tab)
    bubblesort(tab)
    print(tab)

if __name__ == "__main__": main()
