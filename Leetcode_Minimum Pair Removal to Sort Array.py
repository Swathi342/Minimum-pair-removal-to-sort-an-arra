# Function 1: takes array and checks if it is already in ascending order if yes return output as 0
# and break the entire function and give answer as 0, else go to next function
# Function 2: sum of all adjecent numbers and take least sum, and replace that sum inplace of those
# 2 least numbers, continue this till the array is ascending order for that every time we have to
# check the array whether it is ascending or not
class Solution:
    def adj_pair(self, arr):
        adj_sums = [arr[i] + arr[i+1] for i in range(len(arr)-1)]
        min_val = min(adj_sums)
        min_ind = adj_sums.index(min_val)
        min_pair = [arr[min_ind], arr[min_ind+1]]
        return min_pair
    
    def check_arr(self, arr):
        if arr == sorted(arr):
            return 1
        else:
            return 0
    def minimumPairRemoval(self, arr):
        output = 0
        while True:
            if self.check_arr(arr):
                return output
            else:
                output += 1
                sum_adj = sum(self.adj_pair(arr))
                index = arr.index(self.adj_pair(arr)[0])
                arr = arr[:index] + [sum_adj] + arr[index+2:]

# Example usage for LeetCode:
solution = Solution()
result = solution.minimumPairRemoval([1,8,3,4])
print(result)
