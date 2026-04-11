class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        seq=strs[0]
        leng=len(seq)
        for wrd in strs:
            while seq != wrd[:leng]:
                leng-=1
                if leng==0:
                    return ""
                seq=seq[:leng]
        return seq
