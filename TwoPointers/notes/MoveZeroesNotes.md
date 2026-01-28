class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # STUDY THIS AND DO NOT DELETE
        write = 0
        # first pass
        # i = 0, write = 0
        
        # nums[i] = 0 do nothing i = 0
        # [0, 1, 0, 3, 12]
        # nums[1] != 0, swap 
        # [1, 0 ,0, 3, 12]
        # nums[2], 0, do nothing
        # nums[3], not 0, swap with write
        # [1, 3 ,0, 0, 12]
        # [1, 0, 1, 0, 1, 12]



                eg [0, 1, 0, 3, 12]

                eg [0, 0, 0, 1, 2]

                eg [0, 0, 1]

                eg [0, 0, 0]

                eg [1, 2, 3, 0]

                eg [1, 2, 0, 3]
