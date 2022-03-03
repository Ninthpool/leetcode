## a naive O(n) time solution
def findClosestElements_naive(arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # assume arr is valid and sorted
        target_nums = sorted(arr, key = lambda n: abs(n-x))[:k]
        return sorted(target_nums)

# binary search

"""idea
1. Since we must return k number of elements, we are sure that the end of the
return string is located between arr[k] and arr[len(arr) -1]

2. What we need to do is to find this endpoint and after locating it, return k
numbers of elements before it
"""

def findClosestElements_naive(arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        ## assume arr is valid and sorted
        left, right = 0, len(arr) - k


if __name__ == '__main__':
    print(findClosestElements_naive(arr = [1,2,3,4,5], k = 4, x = 3))
    print(findClosestElements_naive(arr = [1,2,3,4,5], k = 3, x = 10))
