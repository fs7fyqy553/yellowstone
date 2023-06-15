import math

def calculate_yellowstone_permutation_integer(n, memoised_sequence=[1, 2, 3]):
    """n == 1 corresponds to first term in sequence and the function returns a tuple 
    containing the resulting term at index 0 and the resulting sequence at index 1, for 
    memoisation."""
    if n <= len(memoised_sequence):
        return memoised_sequence[n - 1], memoised_sequence
    
    last_two = memoised_sequence[-2:]
    included = set(memoised_sequence)

    for i in range(len(memoised_sequence) + 1, n + 1):
        j = 1
        while True:
            if j not in included and math.gcd(last_two[0], j) != 1 and math.gcd(last_two[1], j) == 1:
                last_two[0], last_two[1] = last_two[1], j
                memoised_sequence.append(j)
                included.add(j)
                break
            j += 1
    return last_two[1], memoised_sequence