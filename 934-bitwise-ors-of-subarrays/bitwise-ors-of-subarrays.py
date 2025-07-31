class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        prev= set()
        
        for n in arr:
            current= {n}
            for p in prev:
                current.add(n|p)

            res |= current
            prev = current

        return len(res)