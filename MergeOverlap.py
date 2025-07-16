# Merge overlapping intervals (e.g., [[1, 3], [2, 6], [8, 10]] → [[1, 6], [8, 10]])
def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: Sort intervals by the start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]  # Initialize with the first interval

    for current in intervals[1:]:
        last = merged[-1]
        # Step 2: Check for overlap
        if current[0] <= last[1]:
            # Merge overlapping intervals
            last[1] = max(last[1], current[1])
        else:
            # No overlap, add to result
            merged.append(current)
    
    return merged
intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]
print(merge_intervals(intervals))
