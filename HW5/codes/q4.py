def calc_discount_example(stores):
    # Example discount calculation: sum of the lengths of store names
    return sum(len(store) for store in stores)

def max_discount_dp(stores, calc_discount):
    n = len(stores)
    dp = [0] * (1 << n)

    for mask in range(1, 1 << n):
        for j in range(n):
            if mask & (1 << j):
                prev_mask = mask ^ (1 << j)
                subset_stores = [stores[k] for k in range(n) if mask & (1 << k)]
                dp[mask] = max(dp[mask], dp[prev_mask] + calc_discount([stores[j]]))

    return dp[-1]

stores = ["StoreA", "StoreB", "StoreC"]
max_discount = max_discount_dp(stores, calc_discount_example)

stores2 = ["Shop1", "Shop2", "Shop3", "Shop4"]
max_discount2 = max_discount_dp(stores2, calc_discount_example)

stores3 = ["Alpha", "Beta", "Gamma"]
max_discount3 = max_discount_dp(stores3, calc_discount_example)

stores4 = ["Electronics", "Books", "Clothing"]
max_discount4 = max_discount_dp(stores4, calc_discount_example)

store_list = [stores, stores2, stores3, stores4]
max_discount_list = [max_discount, max_discount2, max_discount3, max_discount4]

for stores, max_discount in zip(store_list, max_discount_list):
    print("Test case:")
    print("----------")
    # Showing subsets and corresponding discounts
    for mask in range(1, 1 << len(stores)):
        subset_stores = [stores[j] for j in range(len(stores)) if mask & (1 << j)]
        discount = calc_discount_example(subset_stores)
        print(f"Stores visited: {subset_stores}, Discount: {discount}")

    print("Maximum achievable discount:", max_discount)

