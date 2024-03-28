def align_sequences(seq1, seq2, ins_del_cost=1, sub_cost=3):
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first row and column
    for i in range(1, m + 1):
        dp[i][0] = i * ins_del_cost
    for j in range(1, n + 1):
        dp[0][j] = j * ins_del_cost

    # Fill the dp matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + sub_cost,
                               dp[i][j - 1] + ins_del_cost,
                               dp[i - 1][j] + ins_del_cost)

    return dp[m][n]

# Test cases
test_cases = [
    ("AGCTA", "AGCTT", 1, 3),
    ("AAAA", "TTTT", 1, 3),
    ("GCGTATGC", "GCTATGCC", 1, 3),
    ("ACGT", "ACCT", 1, 3),
    ("GATTACA", "GCATGCU", 1, 3)]

for seq1, seq2, ins_del_cost, sub_cost in test_cases:
    print("Test case:")
    print("----------")
    print("Sequence 1:", seq1)
    print("Sequence 2:", seq2)
    print(align_sequences(seq1, seq2, ins_del_cost, sub_cost))
