
def square(x: int | float) -> int | float:
    return x * x

def pow(x: int | float) -> int | float:
    return x ** x

def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal count
        result = function(x)
        for _ in range(count):
            result = function(result)
        count += 1
        return result

    return inner
