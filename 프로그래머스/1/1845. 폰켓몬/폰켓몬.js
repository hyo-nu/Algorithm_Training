function solution(nums) {
    let count = nums.length / 2
    const deletedNums = [...new Set(nums)]
    return count < deletedNums.length ? count : deletedNums.length
}