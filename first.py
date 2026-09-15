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

# Check palindrome number

# Find largest of 3 numbers
# Find smallest of 3 numbers
# Count even and odd digits
# Find factorial
# Check prime number
# Print prime numbers 1–N
# Find factors of a number
# Count factors
# Find GCD
# Find LCM
# Check Armstrong number
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