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

3. Upon listing out all the possible case, found that there's no pattern between
value of left and right. Decided to inspect the window [mid-k, mid], and this
makes more sense -- so use this as the selecting condition.

consider [1 2 3 4 5] k=3
1) x  mid-k  mid
here need to move window to left and
mid can't be the target since at least left should be

2) mid-k x      mid
same thing, here need to move window to left and
mid can't be the target (there are k+1 elements between mid-k
and mid, so at least mid-1 could be the target)

3) mid-k          x mid
here need to move winodw to right and mid could be the target

4) mid-k   mid   x
here need to move window to right and mid could be the target

4. when binary search end (left = right), we find the end point of the k substring
"""

def findClosestElements_bry(arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        import math
        ## assume arr is valid and sorted
        left, right = k - 1, len(arr) - 1
        while left < right:
            ## notice that we need to do ceil div to account for index out of bound
            ## otherwise mid-k might not exist
            mid = math.ceil((left + right) / 2)
            if x - arr[mid - k] <= arr[mid] -x:
                # first two cases
                right = mid - 1
            else:
                left = mid
        return arr[right-k+1:right+1]


## same thign, but finding start
def findClosestElements(arr, k: int, x: int):
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) //2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]

if __name__ == '__main__':
    print(findClosestElements_naive(arr = [1,2,3,4,5], k = 4, x = 3))
    print(findClosestElements_naive(arr = [1,2,3,4,5], k = 3, x = 10))

    print(findClosestElements_bry(arr = [1,2,3,4,5], k = 4, x = 3))
    print(findClosestElements_bry(arr = [1,2,3,4,5], k = 3, x = 10))
    print(findClosestElements_bry(arr = [0,0,1,2,3,3,4,7,7,8], k = 3, x = 5))

    print(findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))
    print(findClosestElements(arr = [1,2,3,4,5], k = 3, x = 10))
    print(findClosestElements(arr = [0,0,1,2,3,3,4,7,7,8], k = 3, x = 5))
