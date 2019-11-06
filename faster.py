counts = {}
nums=[4,7,56,1,3,6,7,8,8,2,2,33,-23]
for i in nums:
    counts[i] = counts.get(i, 0) + 1
print counts