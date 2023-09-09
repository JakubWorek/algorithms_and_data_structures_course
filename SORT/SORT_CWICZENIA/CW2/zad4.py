def lider(T):
    ma = max(T)-1
    cnt = [0]*ma
    for i in range(len(T)):
        cnt[T[i]]+=1
    for i in range(len(cnt)):
        if cnt[i] > len(T)//2:
            return i
    return None

# lider lepiej

def lider_lepiej(T):
    kan=T[0]
    cnt=1

    for i in range(1,len(T)):
        if cnt == 0:
            kan=T[i]
            cnt=1
        if T[i]==kan:
            cnt+=1
        else:
            cnt-=1

    fcnt=0
    for i in range(len(T)):
        if T[i]==kan: fcnt+=1

    if fcnt >= len(T)//2+1: return kan

    return None