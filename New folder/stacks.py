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

# max_stack_len=5
# stack=[]
# te=int(input("Enter number of elements : "))
# i=1
# while i<=te:
#     if len(stack)==max_stack_len:
#         break
#     else:
#         element=int(input("Enter a number : "))
#         stack.append(element)
#     i=i+1

# By ME

# stack=[]
# max_len=5

# def push(e):
#     stack.append(e)
#     print(stack)
    
# def pop(e):
#     stack.pop()
#     print(stack)

# def top():
#     t=stack[-1]
#     print(t)

# def empty():
#     l=len(stack)
#     if l==0:
#         print("Stack is empty")

# def full():
#     te=int(input("Enter total no. of elements :" ))
#     i=0
#     while i<te:
#        if len(stack)<=max_len:
#            element=int(input("Enter a number : "))
#            stack.append(element)
#            i=i+1
#        else:
#            break
#     print(stack)
  
           
# full()          




# e=int(input("Enter a number : "))
# push(e)
# pop(e)
# top()
# empty()

# By Sir
# def stack():
#     stack=[]
#     return stack

# def push(stack,element):
#     if stack is not None:
#         stack.append(element)
#         return

# def pop(stack):
#     if len(stack)>0:
#         return stack.pop()
#     else:
#         raise Exception("Stack under flow")
    
# def top(stack):
#     if len(stack)>0:
#         return stack[-1]
#     else:
#         raise IndexError("Stack is underflow")
    
# def isEmpty(stack):
#     if len(stack)==0:
#         return True
#     else:
#         return False
    
# def isFull(stack,max_len):
#     if len(stack)==max_len:
#         return True
#     else:
#         return False
    
# stack=stack()
# element=int(input("Enter a number : "))
# push(stack,element)
# print(stack)
# pop(stack)
# print(stack)
# top=top(stack)
# print(top)
# res=isEmpty(stack)
# print(res)
# max_len=int(input("Enter no. of elements : "))
# res1=isFull(stack,max_len)
# print(res1)

# 4th May 2026
# class Stack():
#     def __init__(self):
#         self.stack=[]

# # obj=Stack()
# # print(obj.stack)

#     def push(self,element):
#         # print(self.stack)
#         if self.stack is not None: 
#             self.stack.append(element) 
#         else:
#             print("Stack is not initialized ")

# # obj=Stack()
# # print(obj.stack)
# # item=int(input("Enter a value : "))
# # obj.push(item)
# # print(obj.push(item))
        
#     def pop(self):  
#         if len(self.stack)>0:
#             return self.stack.pop()
#         else:
#             # raise IndexError("Stack is empty")
#             raise Exception("Stack is empty")
    
# # obj=Stack()
# # print(obj.stack)
# # print(obj.pop())

#     def top(self):
#         if len(self.stack)>0:
#             return self.stack[-1]
#         else:
#             print("Stack is empty")

#     def isEmpty(self):
#         if len(self.stack)==0:
#             print(True)
#         else:
#             print(False)
        
# obj=Stack()
# print(obj.stack)
# item=int(input("Enter a value : "))
# obj.push(item)
# print(obj.top())
# obj.isEmpty()
# print(obj.pop())
# obj.isEmpty()


# obj=Stack.__new__(Stack)
# print(id(obj))
# print(id(Stack))

class Stack():
    def __init__(self,cap):
        self.stack=[]
        self.c=cap

    def push(self,element):
        if self.stack is not None:
            if len(self.stack)<=self.c:
                self.stack.append(element)
            else:
                print("Stack is full")

    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            print("Stack is empty")
        
    def top(self):
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            print("Stack is empty")

    def isFull(self):
        if len(self.stack)==self.c:
            print(True)
        else:
            print(False)

capacity=int(input("Enter stack capacity : "))
obj=Stack(capacity)
print(obj.stack)
item=int(input("Enter a value : "))
obj.push(item)
print(obj.stack)
print(obj.pop())
obj.top()
obj.isFull()  