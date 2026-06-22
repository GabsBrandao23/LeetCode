nums = [2,7,11,15]
target = 9

def two_sum(nums, target):

    map = {}
    for index, value in enumerate(nums):
        key = target - value 
                
        if(key in map):
            return [map[key], index]
        else:
            map[value] = index

print(two_sum(nums, target))