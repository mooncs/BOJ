# 피보나치 수 5
def fibo(x):
    if x <= 1:
        return x
    return fibo(x-2) + fibo(x-1)
n = int(input())
print(fibo(n))

# # for문
# def fibo(x):
#     a, b = 0, 1
#     for _ in range(x):
#         a, b = b, a+b
#     return(a)
# n = int(input())
# print(fibo(n))
