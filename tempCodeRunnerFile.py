

# def makeFiled(m,n,k,mines):
#     dx = (-1,-1,-1,0,0,1,1,1)
#     dy = (-1,0,1,-1,1,-1,0,1)
#     filed = []
    
#     for k in range(n+2):
#         filed.append([0]*(m+2))
    
#     for minei, minej in mines:
#         for k in range(len(dx)):
#             filed[minei + dx[k]][minej+dy[k]] += 1
            
#     for minei, minej in mines:
#         filed[minei][minej] = '*'
#     return filed

# n, m, k = map(int, input().split())

# mines = []
# for i in range(k):
#     mines.append(tuple(map(int, input().split())))

# filed = makeFiled(m,n,k,mines)

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(filed[i][j], end=' ')
#     print()
    
        