def solution(word):
    dictionary = {"0":"", "1":"A", "2":"E", "3":"I", "4":"O", "5":"U"}
    
    def conversion (nums):
        alpha = ""
        for num in nums : alpha += dictionary[num]
        return alpha 
    nums, order = "", 0
    while True:
        order += 1
        if len(nums) < 5 : nums += "1"
        else : 
            nums = list(str(int(nums) + 1))
            while "6" in nums:
                for i in range(5):
                    if nums[i] == "6":
                        nums[i] = "0"
                        nums[i-1] = str(int(nums[i-1]) + 1)
                        break
            nums = "".join(nums)
        if conversion(nums) == word:break
        nums = nums[:5 - nums.count("0")]
    return order