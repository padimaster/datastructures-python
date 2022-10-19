#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Example:
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]


def swap_move(array):
    z = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[i], array[z] = array[z], array[i]
            z += 1
    return array

array = [0,1,0,3,12]
print(swap_move(array))

# Hacks
# def one_liner_move(array):
#     array.sort(key=bool, reverse=True)
#     return array