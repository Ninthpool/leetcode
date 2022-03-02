/*
Idea is to find the pivot point, so that we can do normal binary search in
one of the two sorted subarray (because we can only do binary search in sorted array).
*/
class Solution {
    public int search(int[] nums, int target) {

        if (nums == null || nums.length == 0) return -1;



        //Point is you need to find the pivot first, so that you'll know
        //which sequence you want to do binary search on.


        int pivot = 0; int end = nums.length - 1;

        //Find the pivot point. Idea is if it's in a correctly sorted array,
        //leftmost number would always be smaller than the rightmost number.
        //And notice that numbers at the left sequence will always be greater than those in
        //the the right sequence
        while (nums[pivot] > nums[end]) {
            int middle = pivot + (end - pivot) / 2;
            if (nums[middle] > nums[end]) {
                //if so, the pivot point must be to the right of the middle point.
                pivot = middle + 1;
            } else {
                // Pivot must be the middle point or to it's left.
                end = middle;
            }
        }


        // normal binary search
        int left = 0; int right = nums.length - 1;
        // If it's in the right sequence
        if (nums[pivot] <= target && target <= nums[right]) {
            left = pivot;
        } else {
            right = pivot;
        }

        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (nums[middle] > target) {
                right = middle - 1;
            } else if (nums[middle] < target) {
                left = middle + 1;
            } else {
                return middle;
            }
        }

        return -1;
    }
}
