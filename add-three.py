# nums=[4,2,5,3,5,6,7,4,54,64,12,-34,-23,-6
nums=[14,-11,-2,-3,4,-3,-3,-8,-15,11,11,-6,-14,-13,5,-10,-13,0,-12,-8,14,-12,-10,2,-4,9,13,10,2,7,-2,-7,4,11,5,-7,-15,10,-7,-14,6,11,-5,7,6,8,5,8,-7,8,-15,14,11,13,1,-15,7,0,10,-14,14,-15,-14,3,4,6,4,4,-7,12,5,14,0,8,7,13,1,-11,-2,9,12,-1,8,0,-11,-5,0,11,2,-13,4,1,-12,5,-10,-1,-12,9,-12,-11,-2,9,-12,5,-6,2,4,10,6,-13,4,3,-7,-11,11,-3,-9,-4,-15,8,-9,-4,-13,-14,8,14]
nums = sorted(nums)
# if len(nums)<3:
#     return []
result = []
dic = {}
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        two_sum=nums[i]+nums[j]
        if two_sum in dic:
            dic[two_sum]+=[nums[i],nums[j]]
        else:
            dic[two_sum]=[nums[i],nums[j]]
print '1st'
print dic
for n in nums:
    print 'n is '+str(n)
    reverse = 0-n
    from collections import Counter
    count = Counter(nums)[n]
    if reverse in dic:
        print 'find in dic[reverse] is:'
        print dic[reverse]
        print "len is:" +str(len(dic[reverse]))
        if len(dic[reverse])==2:
            print "target <2"
            tmp_list = [dic[reverse][0],dic[reverse][1]]
            if n not in tmp_list or count !=1: 
                tmp_list.append(n)
                tmp_list = sorted(tmp_list)
                print "tmp_list is "+str(tmp_list)
                if tmp_list not in result:
                    result.append(tmp_list)
                print ' now result is'
                print result
        elif len(dic[reverse])>2:
            print "target >2"
            for m in range(0,len(dic[reverse]),2):
                print 'm is'
                print m
                print 'slice reverse'
                print dic[reverse][m]
                print dic[reverse][m+1]
                tmp_list = [dic[reverse][m],dic[reverse][m+1]]
                if n not in tmp_list or count !=1:
                    print type(tmp_list)
                    tmp_list.append(n)
                    print 'after appendppend'
                    print tmp_list
                    # a= tmp_list.append(int(n))
                    # print a
                    # tmp_result = sorted(tmp_list.append(n))
                    tmp_list = sorted(tmp_list)
                    if tmp_list in result:
                        pass
                    else:
                        result.append(tmp_list)
                    print "now result is"
                    print result
    else:
        print 'not find'
print result
zero = [0,0,0]
if zero in result:
    if Counter(nums)[0]<3:
        result.remove(zero)
        # return result
    else:
        print result
else:
    print result