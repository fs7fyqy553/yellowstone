import math

def calculate_yellowstone_permutation_integer(n):
    # n == 1 corresponds to first term in sequence
    if n <= 3:
        return n
    last_two = [2, 3]
    included = {1, 2, 3}
    for i in range(4, n+1):
        j = 1
        while True:
            if j not in included and math.gcd(last_two[0], j) != 1 and math.gcd(last_two[1], j) == 1:
                last_two[0] = last_two[1]
                last_two[1] = j
                included.add(j)
                break
            j += 1
    return last_two[1]