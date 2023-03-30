"""zip function."""

def zip(x: list[str], y: list[int]) -> dict[str,int]:
    """Returns a dictionary with keys corresponding to values"""
    if len(x) != len(y) or len(x) == 0:
        return {}
    result = {}
    for elem in range(len(x)):
        result[x[elem]] = y[elem]
    return result