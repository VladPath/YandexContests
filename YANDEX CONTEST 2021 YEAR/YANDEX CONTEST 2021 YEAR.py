# I. Сапер


# m,n,k = 3,2,1
# p,q = 1,1
# # [*,1]
# # [1,1]
# # [0,0]

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
  
# ////////////////////////////////////////////
    
# F. Симметричная последовательность

# n =  int(input())
# arr = list(map(int, input().split()))

# if arr == arr[::-1]:
#     print("0")
# else:
#     copy_arr = arr.copy()
#     count = 0
#     while copy_arr != copy_arr[::-1]:
#         count += 1
#         copy_arr = arr.copy() # Создаем копию исходной последовательности
#         for i in range(count):
#             copy_arr.append(copy_arr[count-i-1]) # Добавляем число симметрично относительно середины последовательности
#             r1 = f"{count}"
#             r2 = f"{copy_arr[-count:][::]}" # Выводим добавленные числа в обратном порядке

#     print(f"{r1}\n{' '.join(map(str, copy_arr[-count:][::]))}")
    

# ///////////////////////////
#  E. Чемпионат по метанию коровьих лепешек

# m = int(input())
# arr = list(map(int, input().split()))

# def throwing(arr, m):
#     winner = arr[0]
#     you = 0 
#     res = 0
#     for i in range(1, m-1):
#         if arr[i] > winner:
#             winner = arr[i]
#             you = 0
#         elif arr[i] <= winner and arr[i] > arr[i+1] and str(arr[i])[-1:] == '5' and arr[i] > you:
#             you = arr[i]
#     if arr[-1] > winner:
#         return 0

#     arr = sorted(arr, reverse=True)
#     for i in range(m-1):
#         if arr[i] == you and you != 0:

#             return i+1
#     return 0
    
    
    
# print(throwing(arr, m))