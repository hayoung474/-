
def dfs(current_node, computers, visited):

    if visited[current_node] == True:
        return False

    
    visited[current_node] = True

    for j in range(len(computers[current_node])):
        if computers[current_node][j] == 1:
            dfs(j, computers, visited)

    return True


def solution(n, computers):

    answer = 0

    visited = [False for i in range(n)]

    for i in range(n):
        if visited[i] == False:
            if dfs(i, computers, visited) == True:
                answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
