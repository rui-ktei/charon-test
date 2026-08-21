def bucket_of(timestamp, width):
    return timestamp // width


def spans(timestamps, width):
    ordered = sorted(timestamps)
    return [bucket_of(ordered[i + 1], width) - bucket_of(ordered[i], width)
            for i in range(len(ordered))]
