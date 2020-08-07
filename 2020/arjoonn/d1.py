# https://leetcode.com/problems/brick-wall/


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        rowsums = {}
        most_gaps = 0
        for row in wall:
            total = 0
            for i in row[:-1]:  # Skip the last brick
                total += i
                if total not in rowsums:
                    rowsums[total] = 0
                rowsums[total] += 1
                most_gaps = max((rowsums[total]), most_gaps)
        return len(wall) - most_gaps
