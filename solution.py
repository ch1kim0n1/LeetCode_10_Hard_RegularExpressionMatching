# 6ms solution
class Solution:
    def isMatch(self, s, p):
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*':
                memo[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return memo[(i, j)]
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            memo[(i, j)] = False
            return False

        return dfs(0, 0)