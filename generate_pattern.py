def generate_pattern(n):

    result = []
    def dfs(open, close, current):
        if open == n and close == n:
            result.append(current)
            return
        if open < n:
            dfs(open + 1, close, current + '(')
        if close < open:
            dfs(open, close + 1, current + ')')

    dfs(0, 0, '')
    return result


print(generate_pattern(3))