## a naive O(n^2) stupid solution
def smallestDistancePair_naive(nums, k):
    l = []
    i= 0
    while i < len(nums):
         cur = nums[i]
         j = i+1 # assume nums have at least length of 2
         while j < len(nums):
             num = nums[j]
             dis = abs(num - cur)
             l.append(dis)
             j += 1
         i += 1

    l.sort()
    return l[k-1]

if __name__ == '__main__':
    print(smallestDistancePair_naive([1, 1,1], 2))
    print(smallestDistancePair_naive([1, 6,1], 3))
    print(smallestDistancePair_naive([2,2,0,1,1,0,0,1,2,0], 2))
    print(smallestDistancePair_naive([62, 100, 4], 3))
