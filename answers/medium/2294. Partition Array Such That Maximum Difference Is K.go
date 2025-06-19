import (
	"sort"
)

func partitionArray(nums []int, k int) int {
    sort.Ints(nums)
    sp := 1;
    prev := nums[0];
    for i := 1; i < len(nums); i++ {
        if nums[i] - prev > k {
            sp++;
            prev = nums[i];
        }
    }
    return sp;
}