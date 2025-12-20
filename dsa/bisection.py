def square_root_bisection(value, tolerance=0.01, max_iter=100):
    if value < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    if value == 0:
        print(f"The square root of {value} is {value}")
        return value
    elif value == 1:
        print(f"The square root of {value} is {value}")
        return value

    low = 0.0
    high = max(1.0, value)
    counter = 0
    midpoint = (high + low) / 2

    while (high - low) > tolerance and counter < max_iter:
        midpoint = (high + low) / 2
        if midpoint**2 > value:
            high = midpoint
        else:
            low = midpoint
        counter += 1

    midpoint = (high + low) / 2

    if (high - low) <= tolerance:
        root = midpoint
        print(f"The square root of {value} is approximately {root}")
        return root
    else:
        print(f"Failed to converge within {max_iter} iterations")
        return None
