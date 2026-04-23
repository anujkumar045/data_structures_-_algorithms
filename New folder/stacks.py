# stack=[]
# element=int(input("Enter a number :"))
# stack.append(element)
# print(stack)
# stack.pop(0)
# print(stack)

# stack=[]
# n=int(input("Enter number of elements : "))
# for i in range(n):
#     element=int(input("Enter a number : "))
#     stack.append(element)
# print(stack)

# x=stack.pop()
# print(x,stack)

# t=stack[-1]
# print(t)

# if len(stack)==0:
#     print("Stack is empty")

max_stack_len=5
stack=[]
te=int(input("Enter number of elements : "))
i=1
while i<=te:
    if len(stack)==max_stack_len:
        break
    else:
        element=int(input("Enter a number : "))
        stack.append(element)
    i=i+1