from itertools import combinations


def steiner(t, k, n):
    covered_t_sets = set()
    available_k_sets = set(combinations(range(n), k))
    available_t_sets = set(combinations(range(n), t))
    chosen_k_sets = set()

    def solve():
        if not available_t_sets:
            return chosen_k_sets

        for k_set in available_k_sets:

            candidates = set(combinations(k_set, t))
            if any(_ in covered_t_sets for _ in candidates):
                continue

            chosen_k_sets.add(k_set)
            available_k_sets.remove(k_set)
            covered_t_sets.update(candidates)
            available_t_sets.difference_update(candidates)

            solved = solve()
            if solved:
                return solved

            chosen_k_sets.remove(k_set)
            available_k_sets.add(k_set)
            covered_t_sets.difference_update(candidates)
            available_t_sets.update(candidates)

    return solve()


print(steiner(1, 2, 4))
print(steiner(2, 3, 7))
