def find_minimum_coins(coins, target_amount):
    # Function to recursively find the minimum coins
    def find_coins(coins, target, current_coins):
        if target == 0:
            return 0, current_coins
        if target < 0:
            return float('inf'), []

        min_coins = float('inf')
        best_combo = []

        for i, coin in enumerate(coins):
            remaining_coins = coins[:i] + coins[i+1:]
            num_coins, combo = find_coins(remaining_coins, target - coin, current_coins + [coin])

            if num_coins < min_coins:
                min_coins = num_coins
                best_combo = combo

        return min_coins + 1, best_combo

    # Initial call to the recursive function
    min_coins, best_combo = find_coins(coins, target_amount, [])
    return min_coins if min_coins != float('inf') else None, best_combo

# Test cases
coins = [1, 1, 5, 5, 10, 10, 25, 50]
test_amounts = [11, 23, 37, 1600, 56]

print(f"Coins: {coins}\n")

for amount in test_amounts:
    min_coins_needed, coins_used = find_minimum_coins(coins, amount)
    if (min_coins_needed is None):
        print(f"Cannot make {amount} with the given coins\n")
        continue
    print(f"Minimum coins needed to make {amount}: {min_coins_needed}")
    print(f"Coins used: {coins_used}\n")

