def find_max_min_resources(tasks, left, right):
    # Base case: Only one task
    if left == right:
        return (tasks[left], tasks[left])

    # Base case: Two tasks, directly compare
    if right - left == 1:
        return (max(tasks[left], tasks[right]), min(tasks[left], tasks[right]))

    # Divide the tasks into two halves
    mid = (left + right) // 2
    left_max, left_min = find_max_min_resources(tasks, left, mid)
    right_max, right_min = find_max_min_resources(tasks, mid + 1, right)

    # Conquer: Compare and combine results from two halves
    return (max(left_max, right_max), min(left_min, right_min))

# Test case 1
tasks_1 = [10, 20, 5, 40, 15, 25, 30]
max_resources_1, min_resources_1 = find_max_min_resources(tasks_1, 0, len(tasks_1) - 1)
print(f"Test Case 1 - Max Resources: {max_resources_1}, Min Resources: {min_resources_1}")

# Test case 2
tasks_2 = [45, 55, 35, 65, 25, 75, 15]
max_resources_2, min_resources_2 = find_max_min_resources(tasks_2, 0, len(tasks_2) - 1)
print(f"Test Case 2 - Max Resources: {max_resources_2}, Min Resources: {min_resources_2}")

# Test case 3
tasks_3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
max_resources_3, min_resources_3 = find_max_min_resources(tasks_3, 0, len(tasks_3) - 1)
print(f"Test Case 3 - Max Resources: {max_resources_3}, Min Resources: {min_resources_3}")

# Test case 4
tasks_4 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
max_resources_4, min_resources_4 = find_max_min_resources(tasks_4, 0, len(tasks_4) - 1)
print(f"Test Case 4 - Max Resources: {max_resources_4}, Min Resources: {min_resources_4}")

# Test case 5
tasks_5 = [12, 5, 20, 8, 15, 3, 10, 25, 18, 7]
max_resources_5, min_resources_5 = find_max_min_resources(tasks_5, 0, len(tasks_5) - 1)
print(f"Test Case 5 - Max Resources: {max_resources_5}, Min Resources: {min_resources_5}")
