from collections import Counter
import heapq

def top_k_frequent(nums, k):
    # Count frequency of each number
    freq_map = Counter(nums)

    # Use a heap to get the k most common elements
    return [item for item, count in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]
print(top_k_frequent([1,2,1,3, 3,1], 2))