def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def calculate_strength(player_id):
    def find_next_player(current_player):
        digits_sum = sum(factorial(int(digit)) for digit in str(current_player))
        return digits_sum if digits_sum not in visited else None

    def recursive_group(current_player):
        visited.add(current_player)
        next_player = find_next_player(current_player)
        if next_player is not None:
            group.append(next_player)
            return recursive_group(next_player)

    max_id = player_id
    visited = set()
    group = [player_id]
    recursive_group(player_id)

    # Remove the initial player_id from the group
    group.remove(player_id)

    return max(group) * len(group)