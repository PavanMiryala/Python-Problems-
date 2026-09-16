# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         count={}
#         for x in s:
#             count[x]=count.get(x,0)+1
#         for x in t:
#             count[x]=count.get(x,0)-1
#         for x in count:
#             if count[x]!=0:
#                 return False 
#         return True

    
# s = "a10b2c2"
# result = ""
# i = 0
# while i < len(s):
#     ch = s[i]
#     i += 1
#     num = ""
#     while i < len(s) and s[i].isdigit():
#         num += s[i]
#         i += 1
#     result += ch * int(num)
# print(result)

# 🟢 Level 1 — Beginner: Numbers & Basics
# # Print numbers from 1 to N
# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     print(i)

# # Print even numbers
# n=int(input("enter the number:"))
# if n%2==0:
#     print("it is even")
# else:
#     print("it is odd")

# # Print odd numbers
# n=int(input("enter the number:"))
# if n%2!=0:
#     print("it is odd")
# else:
#     print("it is even ")

# Sum of first N numbers
# n=10
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# Count digits
# count=0
# for i in range(1,11):
#     count=count+1
# print(count)

# # Reverse a number
# n=145
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)

# # Sum of digits
# n = [12, 13, 14, 15]
# sum = 0
# for num in n:
#     sum=sum+num
# print(sum)

# # Product of digits
# n=[12,15,16]
# product=1
# for i in n:
#     product=product*i
# print(product)

# # Check palindrome number
# n=int(input("enter the number:"))
# temp=n
# rev=0
# while n>0:
#     digit=temp%10
#     rev=rev*10+digit 
#     n=n//10
# if temp==rev:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

# # Find largest of 3 numbers
# a=14
# b=16
# c=10
# if a>b and a>c:
#     print("largest is",a)
# elif b>a and b>c:
#     print("largest is ",b)
# else:
#     print("largest is",c)

# # Find smallest of 3 numbers
# a=14
# b=16
# c=10
# if a<b and a<c:
#     print("smallest is ",a)
# elif b<a and b<c:
#     print("smallest is ",b)
# else:
#     print("smallest is",c)

# # Count even and odd digits
# a=[1,2,3,4,5,6,7,8,9]
# even=0
# odd=0
# for i in a:
#     if i%2==0:
#         even=even+1
#     else:
#         odd=odd+1
# print("evne count is ",even)
# print("odd count is ",odd)

# # Find factorial
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# result=factorial(5)
# print(result)
    
# # Check prime number
# n = 7
# prime = True
# for i in range(2, n):
#     if n % i == 0:
#         prime = False
#         break
# if prime:
#     print("Prime")
# else:
#     print("Not Prime")

# # Print prime numbers 1–N
# def primenumber(n):
#     for num in range(2,n+1):
#         prime=True
#         for i in range(2,num):
#             if num%i==0:
#                 prime=False
#                 break
#         if prime:
#             print(num)
# result=primenumber(50)
# print(result)

# # Find factors of a number
# n=30
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# # Count factors
# n=30
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# print(count)

# # Find GCD
# def greatestcommondivisor(a,b):
#     gcd=1
#     for i in range(1,min(a,b)+1):
#         if a%i==0 and b%i==0:
#             gcd=i
#     return gcd
# res=greatestcommondivisor(12,18)
# print(res)

# # Find LCM
# def leastcomonfactor(a,b):
#     lcm=max(a,b)
#     while True:
#         if lcm%a==0 and lcm%b==0:
#             return lcm
#         lcm=lcm+1
# res=leastcomonfactor(12,18)
# print(res)

            
# # Check Armstrong number
# def armstrong(n):
#     temp=n
#     total=0
#     while temp>0:
#         digit=temp%10
#         total=total+digit**3
#         temp=temp//10
#     if total==n:
#         return True
#     else:
#         return False
# print(armstrong(153))
# print(armstrong(123))

# 🟡 Level 2 — Beginner+: Strings
# Reverse a string
# Count vowels
# Count consonants
# Count digits in a string
# Count spaces
# Check palindrome string
# Remove spaces
# Find character frequency
# Find duplicate characters
# Find first non-repeating character
# Check anagram
# Find longest word
# Capitalize each word
# Remove duplicate characters
# Reverse each word
# 🟠 Level 3 — Lists & Arrays
# Find largest element
# Find smallest element
# Find second largest
# Find second smallest
# Calculate list sum
# Count even/odd elements
# Remove duplicates
# Find duplicate elements
# Reverse a list
# Sort without sort()
# Find missing number
# Find common elements
# Merge two lists
# Move zeros to the end
# Find frequency of elements
# 🔵 Level 4 — Intermediate
# Two Sum
# Three Sum
# Maximum subarray sum
# Sliding window maximum sum
# Rotate array
# Merge sorted arrays
# Binary search
# Linear search
# Find majority element
# Find pairs with given sum
# Find longest consecutive sequence
# Remove duplicates from sorted list
# Kadane's algorithm
# Prefix sum problems
# Subarray with given sum
# 🟣 Level 5 — Advanced Python
# Recursion — factorial
# Recursion — Fibonacci
# Recursion — sum of digits
# Recursion — reverse string
# Backtracking basics
# Generate subsets
# Generate permutations
# Stack problems
# Queue problems
# Balanced parentheses
# Next greater element
# Linked list problems
# Binary tree traversal
# Graph traversal — BFS
# Graph traversal — DFS
# 🔴 Level 6 — Interview Level
# Dynamic Programming basics
# Fibonacci using DP
# Climbing stairs
# Coin change
# Longest Common Subsequence
# Longest Increasing Subsequence
# 0/1 Knapsack
# Dijkstra's algorithm
# Detect cycle in graph