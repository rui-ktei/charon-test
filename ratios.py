def success_rate(succeeded, attempted):
    return succeeded / attempted * 100


def midpoint(values):
    ordered = sorted(values)
    if not ordered:
        raise ValueError("midpoint() requires a non-empty sequence of values")
    return ordered[len(ordered) // 2]
