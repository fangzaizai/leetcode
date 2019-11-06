# -*- coding: utf-8 -*-
# @Author: Anmeifang
# @Date:   2019-11-01 17:09:58
# @Last Modified by:   Anmeifang
# @Last Modified time: 2019-11-06 19:02:54

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        if (len(nums)>=3 and nums[0]<=0 and nums[-1]>=0):
            for i in range(len(nums)-2):
                if i > 0 and nums[i] == nums[i-1]: continue
                #起始数值和前一个值相同时，跳过此次循环
                former = i+1
                later = len(nums)-1
                if nums[i]<=0:
                    while former<later:
                        if nums[i]+nums[former]+nums[later]==0:
                            tmp_result = [nums[i],nums[former],nums[later]]
                            result.append(tmp_result)
                            #直接将结果append进数组，再对后面的元素进行去重
                            while (former<later and nums[former]==nums[former+1]):
                                former+=1
                            while (former<later and nums[later]==nums[later-1]):
                                later=later-1
                                #以上为去重
                            later=later-1
                            former+=1
                        elif nums[i]+nums[former]+nums[later]>0:
                            # if nums[former]+nums[i]>0:
                                # break
                            #这是个自作聪明的判断，加上之后运行时间变长了
                            else:
                                later=later-1
                        elif nums[i]+nums[former]+nums[later]<0:
                            # if nums[later]<0:
                                # break
                            else:
                                former+=1
        return result