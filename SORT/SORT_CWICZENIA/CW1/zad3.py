def fast_min_max(T):
    n=len(T)
    mini=T[-1]
    maxi=T[-1]

    for i in range(1,n,2):
        if T[i]<T[i-1]:
            mi,ma=T[i],T[i-1]
        else:
            mi,ma=T[i-1],T[i]
    
        if mi<mini: mini=mi
        if ma>maxi: maxi=ma

    return mini,maxi