package maxSubArray

func maxSubArray(nums []int) int {
	max := nums[0]
	temp_sum := 0

	for i := 0; i < len(nums); i++ {
		temp_sum += nums[i]

		if max < temp_sum {
			max = temp_sum
		}
		if temp_sum < 0 {
			temp_sum = 0
		}
	}
	return max
}
