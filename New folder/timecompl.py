# O(n**2)
# n=int(input("Enter a number : "))
# i,count=1,0
# for i in range(n):
#     for j in range(n):
#         count=count+1
# print(count)

# O(logn)
# n=int(input("Enter a number : "))
# i,count=1,0
# while i<=n:
#         count=count+1
#         i=i*2
# print(count)

# n=int(input("Enter a number : "))
# i,count=1,0
# while n>=i:
#         count=count+1
#         n=n//2
# print(count)

n=int(input("Enter a number : "))
i,count=1,0
for i in range(n+1):
    while i<=n:
            count=count+1
            i=i*2
print(count)


