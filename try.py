from audioop import reverse
from collections import defaultdict
from inspect import stack
from math import ceil
from queue import LifoQueue
import re
from tabnanny import check
from numpy import sort




#         intervals = sorted(intervals)
        
#         if len(intervals)>1:
#             mergedlist = []
#             mergedlist.append(intervals[0])
#             for i in range(1,len(intervals)):
#                 if mergedlist[-1][1] < intervals[i][0]:
#                     mergedlist.append(intervals[i])
#                 else:      
#                     mergedlist[-1][1]=max(intervals[i][1],mergedlist[-1][1])
#                 print(mergedlist)
#             return mergedlist
#         else:
#             return intervals
# print(merge([[1,3],[2,6],[8,10],[15,18]]))

# for i in range(0,4,2):
#     print(i)



# maxi = []
# for i in l:
    
#     while i >= 10: 
#         i = i // 10
#     maxi.append(i)

#     print(i)
# for i in maxi:
    
# print(sort(maxi))

# def rearrangeArray(nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         for i in range(1,len(nums)-1):
#             if (nums[i-1] + nums[i+1]) / 2 == nums[i]:
#                 for j in nums[i:]:
    
#                     if (nums[i-1] + j) / 2 != nums[i]:
                        
#                         nums[i+1],nums[nums.index(j)] = nums[nums.index(j)],nums[i+1]
#                         break
#         return nums
    
    
# print(rearrangeArray([3,2,1]))    






# def findOriginalArray(changed):
#         """
#         :type changed: List[int]
#         :rtype: List[int]
#         """
#         original =[]
#         for i in changed:
#             original.append(i)
#         for i in sort(changed):
#             for j in sort(changed):
                
#                 if changed.index(i) != changed.index(j) and j == 2*i:
                    
                    
#                     original.pop(original.index(j))
#                     # print(original.index(j))
#                     break
#                 else:
#                     continue
#         print(changed)
#         print(original)
#         if len(original) == len(changed)/2:
            
#             return original
#         else:
#             return []

# print(findOriginalArray([0,3,2,4,6,0]))


def sorting(a):
    # Write your code here
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j+1] < a[j]:
                a[j+1],a[j] = a[j],a[j+1]
                
            else:
                continue
    return a


print(ceil(7.3))