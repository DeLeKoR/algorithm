def topKFrequent(nums, k):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for num in count:
        freq = count[num]
        buckets[freq].append(num)
    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result