def verify_card_number(card_number: str):
    numbers = []
    if "-" not in card_number and " " not in card_number:
        for c in card_number:
            numbers.append(int(c))
    else:
        cleaned = card_number.replace("-","").replace(" ","")
        for c in cleaned:
            c = int(c)
            numbers.append(c)

    check_digit = numbers[-1]
    numbers = numbers[:-1]
    numbers = numbers[::-1]
    total = 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            doubled = numbers[i] * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += numbers[i]
        
    total += check_digit
    if total % 10 == 0:
        return f"VALID!"
    else:
        return f"INVALID!"