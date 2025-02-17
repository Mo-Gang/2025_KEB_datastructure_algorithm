# 1부터 입력 받은 수의 합을 구하는 코드를 작성해봐라

# # mine
# n = int(input("Input n : "))
# code = n*(n+1)/2
# print(code)


# # professor's

# f(n) = 3 + n
# O(n)
n = int(input("Input n : "))
r = 0
for i in range(n+1):
    r = r + i
print(r)


# 0(1)
n = int(input("Input n : "))
print(n * (n+1) // 2)
