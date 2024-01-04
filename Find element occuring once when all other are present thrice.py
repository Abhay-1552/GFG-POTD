"""
Given an array of integers arr[] of length N, every element appears thrice except for one which occurs once.
Find that element which occurs once.

Example 1:

Input:
N = 4
arr[] = {1, 10, 1, 1}
Output: 10
Explanation: 10 occurs once in the array while the other element 1 occurs thrice.

Example 2:

Input:
N = 10
arr[] = {3, 2, 1, 34, 34, 1, 2, 34, 2, 1}
Output: 3
Explanation: All elements except 3 occurs thrice in the array.

Your Task: You do not need to take any input or print anything. Your task is to complete the function singleElement()
which takes an array of integers arr and an integer N which finds and returns the element occuring once in the array.

Constraints:
1 ≤ N ≤ 10^5
-10^9 ≤ A[i] ≤ 10^9

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
"""


class Solution:
    def singleElement(self, arr, N):
        ary = {}
        for i in range(N):
            if arr[i] not in ary:
                ary[arr[i]] = 1
            else:
                ary[arr[i]] += 1

        key = list(ary.keys())
        val = list(ary.values())
        return key[val.index(1)]


if __name__ == '__main__':
    t = int(input("Times: "))
    for _ in range(t):
        N = int(input("Array Length: "))
        arr = list(map(int, input("Numbers: ").split()))

        ob = Solution()
        print(ob.singleElement(arr, N))
