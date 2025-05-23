def ft_statistics(*args, **kwargs) -> None:
    """
    Computes and prints statistical measures based on numerical inputs.

    Accepts any number of positional arguments (numbers) and performs
    statistical calculations depending on the values of any keyword arguments.

    Valid keyword values:
        "mean"               → prints the mean of the input numbers.
        "median"             → prints the median.
        "quartile"           → prints 1st and 3rd quartiles (25%, 75%).
        "standard_deviation" or "std" → prints the standard deviation.
        "variance" or "var"  → prints the variance.

    All other keyword values are ignored.

    Example:
        >>> ft_statistics(1, 2, 3, 4, 5, foo="mean", bar="median")
    """
    import math

    def Mean(values):
        return sum(values) / len(values)

    def Median(values):
        sorted_vals = sorted(values)
        n = len(sorted_vals)
        mid = n // 2
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2 if n % 2 == 0 else sorted_vals[mid]

    def Quartile(values):
        sorted_vals = sorted(values)
        n = len(sorted_vals)
        mid = n // 2
        lower = sorted_vals[:mid]
        upper = sorted_vals[mid:] if n % 2 == 0 else sorted_vals[mid + 1:]
        return Median(lower), Median(upper)

    def Standard_Deviation(values):
        m = Mean(values)
        return math.sqrt(sum((x - m) ** 2 for x in values) / len(values))

    def Variance(values):
        m = Mean(values)
        return sum((x - m) ** 2 for x in values) / len(values)

    if not args:
        print("ERROR: No values provided.")
        return

    # Validate all values are numeric
    try:
        args = [float(x) for x in args]
    except ValueError:
        print("ERROR: All arguments must be numbers.")
        return

    # Mapping accepted keyword values to functions
    operations = {
        "mean": lambda: print(f"mean: {Mean(args)}"),
        "median": lambda: print(f"median: {Median(args)}"),
        "quartile": lambda: print(f"quartile (25%, 75%): {Quartile(args)[0]}, {Quartile(args)[1]}"),
        "standard_deviation": lambda: print(f"standard deviation: {Standard_Deviation(args)}"),
        "std": lambda: print(f"standard deviation: {Standard_Deviation(args)}"),
        "variance": lambda: print(f"variance: {Variance(args)}"),
        "var": lambda: print(f"variance: {Variance(args)}"),
    }

    found = False
    for val in kwargs.values():
        func = operations.get(val)
        if func:
            func()
            found = True

    if not found:
        print("ERROR: No valid statistical operation requested.")
