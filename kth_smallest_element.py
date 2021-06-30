# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 19:27:34 2021

@author: shaws
"""

class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        for j in range(len(arr)):
            mn = j
            for i in range(j+1, len(arr)):
                if arr[i] < arr[mn]:
                    mn = i
            arr[j], arr[mn] = arr[mn], arr[j]
            
            if j == k-1:
                return arr[j]
