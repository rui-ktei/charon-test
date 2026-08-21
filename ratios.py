def success_rate(succeeded, attempted):
    return succeeded / attempted * 100


def midpoint(values):
    ordered = sorted(values)
    return ordered[len(ordered) / 2]
