import random

def generate_random_cost_matrix(size):
    return [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

def find_optimal_schedule(users, processes, processors, user_cost_matrices):
    min_cost = float('inf')
    best_assignment = None

    # Function to perform the search
    def search(user_index, assigned_processes, assigned_processors, current_cost, current_assignment):
        nonlocal min_cost, best_assignment

        # Check if all users have been assigned
        if user_index == len(users):
            if current_cost < min_cost:
                min_cost = current_cost
                best_assignment = current_assignment.copy()
            return

        user = users[user_index]
        cost_matrix = user_cost_matrices[user_index]

        # Iterate through each process and processor
        for process in processes:
            if process in assigned_processes:
                continue  # Skip if process is already assigned
            for processor in processors:
                if processor in assigned_processors:
                    continue  # Skip if processor is already assigned

                next_cost = current_cost + cost_matrix[process - 1][processor - 1]
                new_assignment = current_assignment + [(user, process, processor)]

                # Mark the process and processor as assigned and recurse
                assigned_processes.add(process)
                assigned_processors.add(processor)
                search(user_index + 1, assigned_processes, assigned_processors, next_cost, new_assignment)

                # Backtrack
                assigned_processes.remove(process)
                assigned_processors.remove(processor)

    # Start the search with the first user
    search(0, set(), set(), 0, [])

    return min_cost, best_assignment

# Example usage
num_users = 5
num_processes = 5
num_processors = 5
users = list(range(1, num_users + 1))
processes = list(range(1, num_processes + 1))
processors = list(range(1, num_processors + 1))
user_cost_matrices = [generate_random_cost_matrix(num_processes) for _ in range(num_users)]

# Display the cost matrices for each user
for i, matrix in enumerate(user_cost_matrices):
    print(f"Cost Matrix for User {i + 1}:")
    for row in matrix:
        print(row)
    print()

# Find and display the optimal schedule
min_cost, best_assignment = find_optimal_schedule(users, processes, processors, user_cost_matrices)
print("Minimum Cost:", min_cost)
print("Best Assignment:")
for user, process, processor in best_assignment:
    user_index = user - 1  # Adjusting for zero-based index
    process_index = process - 1
    processor_index = processor - 1
    cost = user_cost_matrices[user_index][process_index][processor_index]
    print(f"User {user} uses Process {process} and Processor {processor} -> Cost = {cost}")