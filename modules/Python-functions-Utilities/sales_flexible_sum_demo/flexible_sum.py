def flexible_sum(*args, **kwargs):
    total = 0

    # Sum positional arguments
    for value in args:
        if isinstance(value, (int, float)):
            total += value

    # Sum keyword arguments
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            total += value

    return total