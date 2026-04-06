class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		res = [] 
		m = {} 

		for i, num in enumerate(nums):
			m[num] = i 

		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				target = -(nums[i] + nums[j])
				if target in m and m[target] not in (i, j):
					triplet = [nums[i], nums[j], target]
					triplet.sort()
					found = False 

					for trip in res:
						if trip[0] == triplet[0] and trip[1] == triplet[1] and trip[2] == triplet[2]:
							found = True
							break 

					if not found:
						res.append(triplet)

		return res
					




        