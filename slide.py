#Sliding window
def max_sum_subarray(arr, k):
   n = len(arr)
   if n<k:
      return 0
   current_sum = sum(arr[:k])
   max_so_far = current_sum
   for i in range(k, n):
      current_sum += arr[i] -arr[i-k]
      max_so_far = max(max_so_far, current_sum)
   return max_so_far
arr=[1,3,5,8,9]
k=3
result = max_sum_subarray(arr,k)
print(f"Maximum sum of subarray of size {k}: {result}")