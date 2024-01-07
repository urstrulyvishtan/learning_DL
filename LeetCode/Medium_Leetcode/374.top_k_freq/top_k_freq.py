class solution:
    def top_frequent_k (nums, k):
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for c, v in count.items():
            freq[v].append(c)
        
        res =[]
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
               res.append(n)
               if len(res) == k:
                   return res 