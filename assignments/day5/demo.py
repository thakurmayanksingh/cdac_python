def apply_damage(player_health, damage):
    if damage < 0:
        # Prevent healing a player using a negative damage value
        raise ValueError("Damage cannot be a negative number.")
    new_health = player_health - damage
    return max(0, new_health)

try:
    apply_damage(10, 50)
except ValueError as e:
    print(f"Cheat detected: {e}")