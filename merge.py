def merge_intervals(intervals):
   intervals.sort(key=lambda x:x[0])
   merged =[]
   for inerval in intervals:
      if not merged or merged[-1][1] <inerval[0]:
         merged.append(inerval)
      else:
         merged[-1][1] = max(merged[-1][1], inerval[1])

   return merged
intervals=[[1,3],[2,6]]
print(merge_intervals(intervals))