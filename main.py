# задача 2
# num = 11
# num = str(num)
# res = []
# for i in num:
#     res.insert(0,i)
# print(''.join(res) == num)

# задача 3
# str = 'MCMXCIV'
# roman_duble_num = {
#             'IV':5,
#             'IX':9,
#             'XL':40,
#             'XC':90,
#             'CD':400,
#             'CM':900,
#         }
# roman_num = {
#             'I':1,
#             'V':5,
#             'X':10,
#             'L':50,
#             'C':100,
#             'D':500,
#             'M':1000,
#         }
# res = 0
# # for i in str:
# #     res += roman_num[i]
#
# for i in roman_duble_num:
#     if i in str:
#         res += roman_duble_num.get(i)
#         str = str.replace(i,'')
#
# for i in str:
#     res += roman_num[i]
#
# print(res)
#
#
# задача 4
# stroke = '!vlad and max!'
#
# rreplace(stroke, '!', '', 1)
# print(stroke)

# s = "abcd"
# print(s.title())

# not_dun = ['1','2','3','4']
# dun = []
# dun.append(not_dun.pop())
# print(dun)
# print(not_dun)


# 448 - findDisappearedNumbers
# list = [1, 1, 3, 3, 4, 5]
#
# disappeard_numbers = set(range(1, len(list)+1))
# for elem in list:
#     if elem in disappeard_numbers:
#         disappeard_numbers.remove(elem)
# print(disappeard_numbers)

# 26 removeDuplicates
# nums = [0,0,1,1,1,2,2,3,3,4,6,6,9,9,11,12,12]
# k = 1
# for i in range(1, len(nums)):
#     if nums[i] != nums[i-1]:
#         nums[k] = nums[i]
#         k += 1
# print(k)
# 27. Remove Element
# nums = [2,13,4,1,2,3]
# val = 2

# k = 0
# for i in range(len(nums)):
#     if nums[i] == val:
#         k += 1
#         nums[i] = nums[k]
#     else:
#         nums[i] = nums[k]
#         k += 1

# print(nums)

# def x(*strs):
#     res = []
#     for f in range(0, len(min(strs))):
#         print(f)
        
#     for f in range(len(min(strs))-1):
#         for s in strs:
#             a = []
#             if a == False:
#                 a.append(strs[s])
#             if strs[s] in a:
#                 a.append(strs[s])
#             else:
#                 pass
#         if len(a) == len(strs):
#             res.append(a[0])
                
#     if res:
#         return res
#     else:
#         return ''

# print(x(['hello', 'hell', 'hell']))
# def fizz(l): 
    # def devide_3_and_5(n):
    #     if n % 3 == 0 and n % 5 == 0:
    #         return True
    # def devide_3(n):
    #     if n % 3 == 0:
    #         return True
    # def devide_5(n):
    #     if n % 5 == 0:
    #         return True
    # res = []
    
    # for i in range(1, l+1):
    #     if devide_3_and_5(i):
    #         res.append('FizzBizz')
    #     elif devide_3(i):
    #         res.append('Fizz')
    #     elif devide_5(i):
    #         res.append('Bizz')
    #     else:
    #         res.append(i)
    # return res
# print(fizz(15))


# def step_to_sep(num):             

#     count = {0: num}
#     while count.keys != 0:
#         if count.keys % 2 == 0:
#             count.keys = count.keys / 2 
#             count.values += 1
#         else:
#             count.keys = count.keys - 1
#             count.values += 1
#     return count.values

# print(step_to_sep(3))

# a, b, c, d = map(int, input().split())
# if d > b:
#     res = a + (d-b) * c
#     print(res)
# else:
#     print(a)

# n = 10

# step = 1
# N = 0

# while n > step:
#     step = step * 2
#     N += 1

# print(N)

# nums = [2,2,1,1,1,2,2]
# s = sort()
# print(4/2)

# text = '  fly my  to the  moon  '

# def find_lenght_last_word(x):
#     word = []
#     res = 0
#     for i in x:
#         if not i:
#             res = len(word)
#             word = []
#         else:
#             word.append(i)
#     return res

# print(find_lenght_last_word(text))

# i = 'hello'
# for j in range(0, len(i)+1):
#     print(i[:j])

# text = ["flower","flow","flight"]


# def longet_prefix(x):
#     res = []

#     for i in range(0, len(min(x, key=len))):
#         eq = []
#         for j in x:
#             if not eq:
#                 eq.append(j[:i+1])
#             else:
#                 if eq[0] == j[:i]:
#                     pass
#                 else:
#                     print(eq)
                     
                    
# print(longet_prefix(text))
                
# print(longet_prefix(text))


# -----------------------------1768 - merge strings alternately



# a1 = 'HAha'
# a2 = '123222'

# def merge_strings(a, b):
    # m1 = list(a1)
    # m2 = list(a2)
    
    # ml1 = len(m1)
    # ml2 = len(m2)
    
    # c = []
    # i = 0
    # j = 0
    
    # while i != ml1 or j != ml2:
    #     if i < ml1: 
    #         c.append(m1[i])
    #         i += 1
    #     if j < ml2: 
    #         c.append(m2[j])
    #         j += 1
    
    # c = ''.join(c)

    # return c
    
# def merge_strings(a1, a2):
    #                       v1
    # c = ''
    # for i in range(max(len(a1), len(a2))):
    #     if i < len(a1):
    #         c += a1[i]
    #     if i < len(a2):
    #         c += a2[i]
    # return ''.join(c)    
    #                       v2
#     res = []
#     i, j = 0, 0
#     while i < len(a1) and j < len(a2):
#         res.append(a1[i])
#         res.append(a2[i])
#         i += 1
#         j += 1
#     res.append(a1[i:])
#     res.append(a2[j:])
#     return ''.join(res)
    
        
            

# print(merge_strings(a1, a2))

#  ----------------------------- problem - 1071

# import math


# str1 = 'hehe'
# str2 = 'hehe'

# if (str1+str2) == (str2+str1):
#     max_lenght_str = math.gcd(len(str1), len(str2))
#     print(str1[:max_lenght_str])
# else:
#     print('')


        
        
#  solution num 345 reverse vowels of string

# s = 'car drive'


# def reverse(s):
#     vowels = ['i', 'o', 'a', 'u', 'e', 'I', 'O', 'A', 'U', 'E']
#     s = list(s)
#     left = 0
#     right = len(s)-1
#     while left < right:
#         if s[left] in vowels and s[right] in vowels:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
#         if s[left] not in vowels:
#             left += 1
#         if s[right] not in vowels:
#             right -= 1

#     return ''.join(s)
# print(reverse(s))
            
            
    
    
        



# print(reverse(s))
            
# Субботник 
# p = -10
# v = 10
# q = 20
# m = 10
# q, m = list(map(int, input().split()))
# q, m = list(map(int, input().split()))



# def trees(p,v,q,m):
#     res = set()
#     if v != 0:
#         for i in range(p-v,p+v+1):
#             res.add(i)
#     if m != 0:
#         for i in range(q-m,q+m+1):
#             res.add(i)
#     print(res)
#     print(len(res))

# print(trees(p,v,q,m))



# p,v = int(input()),int(input())
# q,m = int(input()),int(input())

# def trees(p,v,q,m):
#     res = 0
#     res = ((p + v) + (q + m) + 2) - ()

# print(trees(p,v,q,m))


# p, v = list(map(int, input().split()))
# q, m = list(map(int, input().split()))
# p, v = list(map(int, input().split()))
# q, m = list(map(int, input().split()))

# p = -1
# v = 2
# q = 0
# m = 4

# # p = abs(p)
# # q = abs(q)
# res = 0

# # print((4*2)-(3*2)-(0+0))
# # print((10*2) - (3*2)-(0+1))
# if p < 0 and q < 0:
#     p = abs(p) 
#     q = abs(q) 
# if (m*2) - (v*2) - (p+q) > 0 and p <0 and q < 0:
#     res += 1 + (m*2)
# elif (v*2) - (m*2) - (p+q) > 0 and p < 0 and q < 0:
#     res += 1 + (v*2)
# elif p != q:
#     if v != 0:
#         res += 1 + (v*2)

#     if m != 0:
#         res += 1 + (m*2)

#     if (p + q - 1) - (v+m) < 0 and v != 0 and m != 0:
#         res += (abs(p) + abs(q) - 1) - (v+m)
# elif p == q and v == m and v != 0:
#     res += 1 + (v*2)
# elif p == q and v != m:
#     if v > m:
#         res += 1 + (v*2)
#     else:
#         res += 1 + (m*2)
         

    

    
# print(res)
    
    
# print((11*2)-(11*2)-(0+1))
# print((11*2) - (10*2)-(0+1))


# print((4*2)-(2*2)-(0-(-1)))



# футбол
# a1, b1 = list(map(str, input().split(':')))
# a2, b2 = list(map(int, input().split(':')))
# w = int(input())

# a1,b1 = 1,1
# a2,b2 = 2,2
# w = 1

# if a1 == b1 and a2 == b2:
#     res = 1
# if a1 > b1 and a2 > b2:
#     res = 0

    
    


# print(a1,b2,a2,b2)
# print((a1-b1) - (a2+b2))

# олимпиадная задачка обнаружить
# заполненость острова после дождя 

# h = [3,1,4,3,5,1,1,3,1]

# def is_pool(h):
#     max_pos = 0
#     for i in range(len(h)):
#         if h[i] > max_pos:
#             max_pos = i
#     ans = 0
#     nowm = 0
#     for i in range(max_pos):
#         if h[i]>nowm:
#             nowm = h[i]
#         ans += nowm - h[i]
#     nowm = 0
#     for i in range(len(h)-1,max_pos, -1):
#         if h[i] > nowm:
#             nowm = h[i]
#         ans += nowm - h[i]
#     return ans
# print(is_pool(h))
        
# задача rle - из строки aaabbcad -> a3b2cad
# text = 'aaabbbcccdefj'

# def rle(x):
#     def pack(pos,count):
#         if count > 1:
#             return pos + str(count)
#         return pos
    
#     lastpos = 0
#     res = []
#     for i in range(len(x)):
#         if x[i] != x[lastpos]:
#             res.append(pack(x[lastpos], i - lastpos))
#             lastpos = i
#     res.append(pack(x[lastpos], len(x) - lastpos))
#     return ''.join(res)

# print(rle(text))
        
# 10 20
# freeze

# now, need = map(int, input().split())
# mode = input()

# now, need = 20, 20
# mode = 'fan'

# def conditioner(now, need, mode):
#     if mode == 'auto':
#         return need
#     elif mode == 'fan':
#         return now
#     elif mode == 'heat':
#         if now < need:
#             return need
#         else:
#             return now
#     elif mode == 'freeze':
#         if now > need:
#             return need
#         else:
#             return now


# print(conditioner(now, need, mode))



# a, b, c = map(int,input().split())
# # a, b, c = 3,4,5
# def trangle(a, b, c):
#     pass
#     if a != c or b != c or a != b:
#         return 'Yes'
#     else:
#         return 'No'

 
# print(trangle(a, b, c))
# a,b,c = 1, 2, 2

# def trang(a,b,c):
        
#     tr = [a,b,c]
    
#     for i in tr :
#         if i <= 0:
#             return 'NO'
        
#     if tr.count(a) > 2:
#         print('NO')
#     else:
#         print('YES')

# print(trang(a,b,c))
        
        



# def trang(a,b,c):
#     if a+b>c and a+c>b and b+c>a:
#         return 'YES'
#     else:
#         return 'NO'

# print(trang(a,b,c))

# if (a + b > c && a + c  > b  && b + c > a) {
#     cout << "YES";
# }
# else {
#     cout << "NO";
# }


# задание о номере телефона 
# import re

# a = '8(495)430-23-97'
# b = '+7-4-9-5-43-023-97'
# c = '4-3-0-2-3-9-7'
# new = '8-495-430'

# a = '+78047952807'
# b = '78047952807'
# c = '76147514928'
# new = '88047952807'

# a = list(input())
# b = list(input())
# c = list(input())
# new = list(input())


# def creat_reg_number(x:list):
#     new_list = []
#     for i in x:
#         if i not in ['-', '[', ']', '(', ')', '+']:
#             new_list.append(i)
#     return new_list

# def is_eq(new:list, old:list):
#     new[0] = '8'
#     old[0] = '8'
#     res = 0
#     for i in range(len(new)):
#         if new[i] == old[i]:
#             res += 1
#     if len(new) == res:
#         return 'YES'
#     return 'NO'
#     pass
    
    

# def get_new_number(new, a,b,c):
#     new_num = creat_reg_number(new)
#     a = creat_reg_number(a)
#     b = creat_reg_number(b)
#     c = creat_reg_number(c)
#     print(is_eq(new_num, a))
#     print(is_eq(new_num, b))
#     print(is_eq(new_num, c))
    

    

# get_new_number(new,a,b,c)

# def sort2(i,j):
#     if i>j:
#         return (i, j)
#     return (j,i)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# a,b = sort2(a,b)
# b,c = sort2(a,b)
# a,b = sort2(a,b)
# d,e = sort2(d,e)

# if e >= b and d >= a:
#     print('YES')
# else:
#     print('NO')
    
# n1, m1, n2, m2 = map(int, input().split())

# def sq1(n1, m1, n2, m2):
#     tm = max(n1, m1) + max(n2, m2)
#     tn = max(min(n1, m1), min(n2, m2))
#     return (tn, tm, tn*tm, 1)

# def sq2(n1, m1, n2, m2):
#     tm = min(n1, m1) + min(n2, m2)
#     tn = max(max(n1, m1), max(n2, m2))
#     return (tn, tm, tn*tm, 2)

# def sq3(n1, m1, n2, m2):
#     tm = max(n1, m1) + min(n2, m2)
#     tn = max(min(n1, m1), max(n2, m2))
#     return (tn, tm, tn*tm, 3)

# def sq4(n1, m1, n2, m2):
#     tm = min(n1, m1) + max(n2, m2)
#     tn = max(max(n1, m1), min(n2, m2))
#     return (tn, tm, tn*tm, 4)

# vars = []

# for i in (sq1, sq2, sq3, sq4):
#     x = i(n1, m1, n2, m2)
#     vars.append(x)

# vars = sorted(vars, key=lambda y: y[2])

# print(vars[0][0], vars[0][1])
    
    
# n, k, m = map(int, input().split())  


# while i < 1:
#     i += 1
#     # a = []

#     # a.insert(0, random.randint(20, 900))
#     # a.insert(1, random.randint(10, 19))
#     # a.insert(2, random.randint(1, 9))
        
#     # print(a)
#     # n, k, m = a
#     # print(n)
     
# n, k, m = 21,11, 21

# def materials(n,k,m):
#     if n==0 or k == 0 or m ==0 or m > k:
#         return 0
#     r = 0
#     while n >= k:
#         n = n-k
#         a = k
#         while a >= m:
#             a = a - m
#             r += 1
#         n += a
#     return r
    
# print(materials(n, k, m))

# # a = [0]*3
# # c,j,i = a
# # print(i)

# возрастающий ли массив?

# a = [1,7,9]
# a = list(map(int,input().split()))

# def increasing(a:list):
#     now = a[0]
    
#     for i in range(1,len(a)):

#         if a[i] <= now :
#             return 'NO' 
#         now = a[i]
#     return 'YES'

# print(increasing(a))

# задание тип массива 

# a = 0
# x=[]
# while a != -2000000000:
#      a = int(input())
#      x.append(a)
# x.pop()
     
# def type_arr(x):
#     # constant
#     c = 0
#     a = 0
#     wa = 0
#     d = 0
#     wd = 0
    
#     f = x[0]
#     for i in range(1, len(x)):
#         if f == x[i]:
#             c += 1
#             wa += 1
#             wd += 1
#         elif f > x[i]:
#             d += 1
#             wd += 1
#         elif f < x[i]:
#             a += 1
#             wa += 1
#         f = x[i]
#     if a and d:
#         return 'RANDOM'
#     if d == 0 and a == 0 and c == len(x)-1:
#         return 'CONSTANT'
#     if a == wa and a > 0:
#         return 'ASCENDING'
#     if wa > a and  not d:
#         return 'WEAKLY ASCENDING'
#     if d == wd:
#         return 'DESCENDING'
#     if wd > d and a == 0:
#         return 'WEAKLY DESCENDING'
    
    
# print(type_arr(x))

# Ближайший массив 

# arr = [1111,1000]
# x = 1
# def nearest_digit(arr, x):
#     j = 1000
#     r = 0
#     for i in range(0, len(arr)):
#         if abs(arr[i] - x) < j:
#             r = arr[i]
#             j = abs(arr[i] - x )
            
#     return r
# print(nearest_digit(arr, x))

# # n = int(input())
# arr = list(map(int,input().split()))
# x = int(input())
          

# arr = list(map(int, input().split()))
# arr = [1,2,1]

# def bigger_neighbors(arr:list):
#   r = 0
#   for i in range(1, len(arr)-1):
#     if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
#       r += 1
#   return r
    
# print(bigger_neighbors(arr))


# arr = [11, 121,21,16,15, 11, 123, 1, 123, 22, 15, 25, 55, 25, 55, 25, 65,75,15, 8090, 15,15, 111,23,65,2, 25,2]

# m = len(arr)

# def throwing(arr, m):
#     winner = arr[0]
#     you = 0 
#     for i in range(1, m-1):
#         if arr[i] > winner:
#             winner = arr[i]
#             you = 0
#         elif arr[i] <= winner and arr[i] > arr[i+1] and str(arr[i])[-1:] == '5' and arr[i] > you:
#             you = arr[i]
#     if arr[-1] > winner:
#         return 0
#     arr = sorted(arr, reverse=True)
#     print(arr)
#     for i in range(m-1):
#         if arr[i] == you and you != 0:
#             print(you)

#             return i+1
#     return 0
    
    
    
# print(throwing(arr, m))
    
# Симметричкная последовательность
# arr = [1,2,3,4,5,4,3]
# n = len(arr)

# def is_simm(arr,n):
#     i = 0
#     j = n-1
#     while i != n//2:
#         if arr[i] == arr[j]:
#             i+= 1
#             j-= 1
#         else:
#             return False
#     return True

# def simmetric_arr(arr, n):
#     if n == 1:
#         return f'{n}\n{arr[0]}'
#     elif is_simm(arr,n):
#         return 0
#     # if arr[0]!=arr[-1]:
#     #     for i in range(len(arr)):
#     #         if arr[i] != arr[-1]:
#     #             pass
                
        
            
            
#     if arr[-1] == arr[-2]:
#         res = []
#         print('четная')
#         for i in range(n-3, -1, -1):
#             res.append(arr[i])
#             # вывожу f строку с колличеством изменений и последовательностью добавлений
#         return f"{len(res)}\n{' '.join(map(str,res))}" 
#     elif arr[-1] != arr[-2]:
#         res = []
#         print('нечетная')
#         for i in range(n-2, -1, -1):
#             res.append(arr[i])
#             # вывожу f строку с колличеством изменений и последовательностью добавлений
#         return f"{len(res)}\n{' '.join(map(str,res))}" 
            
# n = int(input("Кол-во чисел: "))
# arr = []
# n = 5
# arr = [1,2,3,4,5,4]
# # for i in range(n):
# #     arr.append(int(input("Число: ")))

# # Проверяем, является ли последовательность уже симметричной
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

# # print(simmetric_arr(arr, n))


# Произведение чисел 
text = '12288 -10075 29710 15686 -18900 -17715 15992 24431 6220 28403 -23148 18480 -22905 5411 -7602 15560 -26674 11109 -4323 6146 -1523 4312 10666 -15343 -17679 7284 20709 -7103 24305 14334 -12281 17314 26061 25616 17453 16618 -24230 -19788 21172 11339 2202 -22442 -20997 1879 -8773 -8736 5310 -23372 12621 -25596 -28609 -13309 -13 10336 15812 -21193 21576 -1897 -12311 -6988 -25143 -3501 23231 26610 12618 25834 -29140 21011 23427 1494 15215 23013 -15739 8325 5359 -12932 18111 -72 -12509 20116 24390 1920 17487 25536 24934 -6784 -16417 -2222 -16569 -25594 4491 14249 -28927 27281 3297 5998 6259 4577 12415 3779 -8856 3994 19941 11047 2866 -24443 -17299 -9556 12244 6376 -13694 -14647 -22225 21872 7543 -6935 17736 -2464 9390 1133 18202 -9733 -26011 13474 29793 -26628 -26124 27776 970 14277 -23213 775 -9318 29014 -5645 -27027 -21822 -17450 -5 -655 22807 -20981 16310 27605 -18393 914 7323 599 -12503 -28684 5835 -5627 25891 -11801 21243 -21506 22542 -5097 8115 178 10427 25808 10836 -11213 18488 21293 14652 12260 42 21034 8396 -27956 13670 -296 -757 18076 -15597 4135 -25222 -19603 8007 6012 2704 28935 16188 -20848 13502 -11950 -24466 5440 26348 27378 7990 -11523 -26393 '
n = [4, 3, 5, 2, 5]
# n = [-4, 3, -5, 2, 5]
# n = list(map(int,text.split()))
# print(n)


# def the_product_of_numbers(x):
#     n.sort()
#     print(n)
#     res = []
#     if abs(n[-1]+n[-2]) > abs(n[0]+n[1]):
#         print(n[-2],n[-1])
        
#     else:
#         print(n[0],n[1])
        
# print(the_product_of_numbers(n))
        
# n = list(map(int,input().split()))




# # n = list(map(int,input().split()))
# n = [-100, -21, -32, 1, 210, 320]
# n = [3, 5, 1, 7, 9, 0, 9, -3, 10]
# # n = [-5, -30000, -12]
# # n = []


# def the_product_of_numbers(x):
#     x.sort()
#     a = abs(x[-1]*x[-2]*x[-3])
#     b = abs(abs(x[0])*abs(x[1])*abs(x[2]))
#     c = abs(abs(x[0])*abs(x[1])*x[-1])
#     d = x[-1]*x[-2]*abs(x[0])
#     li = {'a':a, 'b':b, 'c':c, 'd':d}
#     r = max(li, key=li.get)
#     print(li[r])
    
#     if r == 'a':
#         return f'{x[-1]} {x[-2]} {x[-3]}'
#     elif r == 'b':
#         return f'{x[0]} {x[1]} {x[2]}'
#     elif r == 'c':
#         return f'{x[0]} {x[1]} {x[-1]}'
#     elif r == 'd':
#         return f'{x[-1]} {x[-2]} {x[0]}'
        
# print(the_product_of_numbers(n))


# сапер 

m,n,k = 3,2,1
p,q = 1,1
# [*,1]
# [1,1]
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
    
        
        
    


