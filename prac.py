from collections import Counter

def removeDuplicates(nums):  # [1, 2, 3]
    count = Counter(nums)     # { 1:1, 2:2, 3:1 }
    print(count)
    for key in count.keys():     # 3, 1
        num_ocur = nums[key]
        while num_ocur > 1:         
            nums.remove(key)
            num_ocur -= 1
    print(nums)


removeDuplicates([1, 2, 2, 3])