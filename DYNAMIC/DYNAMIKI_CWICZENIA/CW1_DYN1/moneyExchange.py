def exchange(coins, amount):
    counts = [amount + 1] * (amount + 1)
    counts[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                counts[i] = min(counts[i], counts[i - coin] + 1)
                
    #print(counts)
                
    return counts[amount] if counts[amount] <= amount else -1

coins = [2, 5]
amount = 2
print(exchange(coins, amount))