def create_character(name, strength, intelligence, charisma):
    # Name Validation
    if not isinstance(name, str):
        return "The character name should be a string"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    
    stats = (strength, intelligence, charisma)

    # Stats Validation
    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"
    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1"
    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4"
    if sum(stats) != 7:
        return "The character should start with 7 points"

    full_dot = "●"
    empty_dot = "○"

    line1 = name
    line2 = "STR " + full_dot * strength     + empty_dot * (10 - strength)
    line3 = "INT " + full_dot * intelligence + empty_dot * (10 - intelligence)
    line4 = "CHA " + full_dot * charisma     + empty_dot * (10 - charisma)

    return "\n".join([line1, line2, line3, line4])
print(repr(create_character("ren", 4, 2, 1)))
