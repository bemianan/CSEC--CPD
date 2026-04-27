class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter=[]
        nums1d=Counter(nums1)
        nums2d=Counter(nums2)
        for num in nums1d:
            if nums2d[num]:
                inter+=[num]*(min(nums1d[num],nums2d[num]))
        return inter
