def bucket_of(timestamp, width):
    return timestamp // width


def spans(timestamps, width):
    ordered = sorted(timestamps)
    return [
        bucket_of(ordered[index + 1], width) - bucket_of(ordered[index], width)
        for index in range(len(ordered) - 1)
    ]
