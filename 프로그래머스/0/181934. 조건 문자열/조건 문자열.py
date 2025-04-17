def solution(ineq, eq, n, m):
    answer = 0
    if eq == "!":
        a = str(n) + ineq + str(m)
    else:
        a = str(n) + ineq + eq + str(m)
    if eval(a) == True:
        answer = 1
    return answer