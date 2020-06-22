from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Create hash-map to get all the same group together
        result = dict()
        for i, val in enumerate(groupSizes):
            if not result.get(val):
                result[val] = [i]
            else:
                result[val] = result[val] + [i]

        # Splitting the groups into the size they has to be in.
        _result = []
        for k in result:
            _result += (result[k][i:i+k] for i in range(0, len(result[k]), k))
        return _result


sol = Solution()
print(sol.groupThePeople([1, 2, 1, 2, 3, 3, 3]))
