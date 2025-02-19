def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A')+i), end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:   #연결이 돼있으면서 동시에 방문한 적이 없는.
            dfs(g, j, visited)  #다 끝나면 자기를 호출했던 함수로 돌아간다 #재귀
            # 쭉 가다가, 갈 곳이 아니면 return 한다는 말.

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

# visited = [0] * len(graph)
# dfs(graph, 0, visited)

visited = [0] * len(graph)
dfs(graph, 4, visited)

"""
visited
[0,0,0,0,0]
[0,0,0,0,1] E
[0,0,1,0,1] C
[1,0,1,0,1] A
[1,0,1,1,1] D: A와 C는 visited, 따라서 A(자기를 호출한 함수)로 return.
근데 A에서도 다 visited라, return. (C로)
(D -> A -> C)
[1,1,1,1,1] B: B 다 처리됐으니까 return.
(-> B -> C -> E: 완성~)
"""

print(visited)







