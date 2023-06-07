import math

def yellowstone_permutation_calculator(k):
    # NOTE: k = 0 corresponds to the first integer in the sequence
    assert type(k) == int and k >= 0
    sequence = [1, 2, 3]
    lookup_set = set(sequence)
    if k <= 2:
        return sequence[k]
    while len(sequence) - 1 < k:
        penultimate = sequence[len(sequence) - 2]
        last = sequence[len(sequence) - 1]
        print("Penultimate", penultimate, "Last", last)
        next_term = float("infinity")
        for potential_factor in range(2, penultimate + 1):
            # print(potential_factor)
            if penultimate % potential_factor != 0:
                continue
            if last % potential_factor == 0:
                continue
            print("Potential factor", potential_factor)
            multiplier = 1
            while multiplier * potential_factor in lookup_set or math.gcd(last, multiplier * potential_factor) != 1:
                multiplier += 1
            potential_next_term = multiplier * potential_factor
            print("Potential next term", potential_next_term)
            next_term = min(potential_next_term, next_term)
        sequence.append(next_term)
        lookup_set.add(next_term)
    return sequence[k]

print("nth term", yellowstone_permutation_calculator(69))