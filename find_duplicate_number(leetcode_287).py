# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:55:54 2021

@author: shaws

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.
"""


# Solution 1
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            if counter[num]>=2:
                return num
            
            
# Solution 2
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited:
                return num
            visited.add(num)