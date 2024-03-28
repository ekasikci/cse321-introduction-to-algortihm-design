def calculate_discount(stores):
    # This function calculates the discount for a given set of stores and returns the total
    return sum(stores)

def generate_subsets(stores, index=0, current_subset=[]):
    if index == len(stores):
        discount = calculate_discount(current_subset)
        print(f"Selected Stores: {current_subset} \tDiscount: {discount}")
        return

    # Include the current store in the subset
    generate_subsets(stores, index + 1, current_subset + [stores[index]])

    # Exclude the current store from the subset
    generate_subsets(stores, index + 1, current_subset)

def find_max_discount(stores):
    # Perform an exhaustive search over all combinations of stores
    generate_subsets(stores)

# Example test
store_values = [5, 10, 15, 20, 25]
find_max_discount(store_values)
