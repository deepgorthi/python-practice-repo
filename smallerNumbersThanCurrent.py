def smallerNumbersThanCurrent(nums):
    print(f"Original list - {nums}")
    print(f"Sorted list - {sorted(nums)}")
    return [sorted(nums).index(num) for num in nums] 
    # For descending Order
    # return [sorted(nums, reverse = True).index(num) for num in nums] 

print(smallerNumbersThanCurrent([8,1,2,2,3]))