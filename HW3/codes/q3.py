import random

# Function to generate the cost matrix
def generate_cost_matrix(num_parts):
    cost_matrix = {}
    for i in range(1, num_parts + 1):
        from_part = f'part_{i}'
        cost_matrix[from_part] = {}
        for j in range(1, num_parts + 1):
            to_part = f'part_{j}'
            # Randomly generate a cost
            cost_matrix[from_part][to_part] = random.randint(1, 10) if i != j else 0
    return cost_matrix

# Function to display the cost matrix
def display_cost_matrix(cost_matrix):
    parts = cost_matrix.keys()
    header_row = "\t" + "\t".join(parts)
    print(header_row)
    for from_part in parts:
        row = from_part + "\t" + "\t".join(str(cost_matrix[from_part][to_part]) for to_part in parts)
        print(row)

# Function to calculate the energy cost
def calculate_energy_cost(current_sequence, next_part, cost_matrix):
    if not current_sequence:
        return 0
    last_part = current_sequence[-1]
    return cost_matrix[last_part][next_part]

# Function to find the energy-efficient sequence
def find_min_energy_sequence(parts, cost_matrix):
    min_energy = float('inf')
    best_sequence = None

    def generate_permutations(current_sequence, remaining_parts, current_energy):
        nonlocal min_energy, best_sequence
        if not remaining_parts:
            if current_energy < min_energy:
                min_energy = current_energy
                best_sequence = current_sequence[:]
            return
        for i, part in enumerate(remaining_parts):
            next_energy = calculate_energy_cost(current_sequence, part, cost_matrix)
            generate_permutations(current_sequence + [part], remaining_parts[:i] + remaining_parts[i+1:], current_energy + next_energy)

    generate_permutations([], parts, 0)
    return best_sequence, min_energy  # Now also returns the total energy cost

# Number of parts
num_parts = 4
parts = [f'part_{i}' for i in range(1, num_parts + 1)]

# Generate and display the cost matrix
cost_matrix = generate_cost_matrix(num_parts)
display_cost_matrix(cost_matrix)

# Find and display the energy-efficient sequence
best_sequence = find_min_energy_sequence(parts, cost_matrix)
print("\nEnergy-efficient Sequence:", best_sequence)
