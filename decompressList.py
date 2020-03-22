def decompressList(nums):    
    decompressed_list = []
    
    for i in range(len(nums)//2):
        for _ in range(nums[2*i]):
            decompressed_list.append(nums[2*i + 1])
    return decompressed_list

print(decompressList([1, 2, 3, 4]))