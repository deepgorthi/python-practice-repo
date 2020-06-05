nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
# target_array = [0,4,1,3,2]

def create_target_array(nums, index):
    target_array = []
    nums_length = len(nums)
    for i in range(nums_length):
        target_array[i] = index[i]
        print(i)
    return target_array

if __name__ == "__main__":
    print(create_target_array(nums, index))