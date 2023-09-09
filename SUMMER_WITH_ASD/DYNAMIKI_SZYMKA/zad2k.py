from zad2ktesty import runtests

# f(a,b) = najdłuzszy palindrom od a do b
# if a == b: -> True
# if a+1 == b: 
#   S[a] == S[b] -> True
#   S[a] =/= S[b] -> False
# T[a] =/= T[b] -> False
# else -> f(a+1, b-1)

def palindrom( s ):
    n = len(s)
    DP = [[False]*len(s) for _ in range(len(s)) ]

    # base case
    for i in range(len(s)):
        DP[i][i]=True

    ans=s[0]
    for j in range(len(s)):
        for i in range(j):
            if s[i]==s[j] and (DP[i+1][j-1] or j==i+1):
                DP[i][j]=True
                if j-i+1>len(ans):
                    ans=s[i:j+1]

    return ans

runtests ( palindrom )