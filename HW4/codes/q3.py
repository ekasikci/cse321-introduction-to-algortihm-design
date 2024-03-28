def max_area_under_curve(f, n):
    max_so_far = float('-inf')
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(n):
        max_ending_here += f[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return max_so_far, start, end

f = [1, 2, 3, 4, 5]  # Simple increasing function
n = len(f)
print("Test Case 1:", max_area_under_curve(f, n))

f = [-2, -3, 4, -1, 2, 1, -5, 4, 7, -3]  # Combination of negative and positive values
n = len(f)
print("Test Case 2:", max_area_under_curve(f, n))


f = [-1, -2, -3, -4, -5]  # All negative values
n = len(f)
print("Test Case 3:", max_area_under_curve(f, n))


f = [3, -2, 5, -1, 4, -3]  # Alternating positive and negative values
n = len(f)
print("Test Case 4:", max_area_under_curve(f, n))


import random
f = [random.randint(-10, 10) for _ in range(10)]  # Random values
n = len(f)
print("Test Case 5:", max_area_under_curve(f, n))

