def ft_statistics(*args, **kwargs) -> None:
    import math

    def is_valid_data(data):
        return data and all(isinstance(el, (int, float)) for el in data)

    def mean(data):
        return sum(data) / len(data)

    def median(data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def quartile(data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2

        lower = sorted_data[:mid]
        upper = sorted_data[mid:] if n % 2 == 0 else sorted_data[mid + 1:]

        def med(d):
            m = len(d)
            return (d[m // 2 - 1] + d[m // 2]) / 2 if m % 2 == 0 else d[m // 2]

        return [med(lower), med(upper)]

    def std(data):
        m = mean(data)
        return math.sqrt(sum((x - m) ** 2 for x in data) / len(data))

    def var(data):
        m = mean(data)
        return sum((x - m) ** 2 for x in data) / len(data)

    if not is_valid_data(args):
        for _ in kwargs:
            print("ERROR")
        return

    mapping = {
        "mean": lambda: print(f"mean : {mean(args)}"),
        "median": lambda: print(f"median : {median(args)}"),
        "quartile": lambda: print(f"quartile : {quartile(args)}"),
        "std": lambda: print(f"std : {std(args)}"),
        "var": lambda: print(f"var : {var(args)}"),
    }

    for key in kwargs.values():
        if key in mapping:
            mapping[key]()
        else:
            print("ERROR")
