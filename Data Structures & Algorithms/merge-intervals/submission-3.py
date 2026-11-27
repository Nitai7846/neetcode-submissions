class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        ans = []
        ans.append([intervals[0][0], intervals[0][1]])

        for i in range(1, len(intervals)):

            new_start = intervals[i][0]
            new_end = intervals[i][1]
            last_start = ans[-1][0]
            last_end = ans[-1][1]

            if new_start <= last_end:
                ans[-1][1] = max(new_end, last_end)
            else:
                ans.append([intervals[i][0], intervals[i][1]])

        return ans 





        