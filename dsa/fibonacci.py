def fibonacci(n):
    sequence = [0, 1]

    if n == 1:
        return 1
    if n == 2:
        return sequence[1]

    while len(sequence) < n + 1:
        sequence.append(sequence[-1] + sequence[-2])
    print(sequence)
    return sequence[n]

