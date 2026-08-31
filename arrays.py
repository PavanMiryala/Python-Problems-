
# def armstrong(n):
#     temp=n
#     total=0
#     while temp>0:
#         digit=temp%10
#         total=total+digit**3
#         temp=temp//10
#     if total==n:
#         print("armstrong")
#     else:
#         print("not armstrong")
# armstrong(153)


#palindrome  if single elemnet means this logic 
# def palindrome(n):
#     temp=n
#     rev=0
#     while temp>0:
#         digit=temp%10
#         rev=rev*10+digit
#         temp=temp//10
#     if rev==n:
#         print("palindrome")
#     else:
#         print("not palindrome")
# palindrome(121)

# #find largest elememt 
# arr=[10,20,30,15,35,40,45]
# largest=arr[0]
# for i in arr:
#     if i>largest:
#         largest=i
# print(largest)

#find the smallest element 
# smallest=arr[0]
# for i in arr:
#     if i<smallest:
#         smallest=i
# print(smallest)

#find sum of the array
# total=0
# for i in arr:
#     total=total+i
# print(total)


#even or odd using array 

# arr=[10,20,30,15,35,40,45]
# even=0
# odd=0
# for i in arr:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("even",even)
# print("odd",odd)


# search an element in array
# arr=[10,20,30,15,35,40,45]
# target=35
# found=False
# for i in arr:
#     if i==target:
#         found=True
#         break
# if found:
#     print("element is found",target)
# else:
#     print("element is not found",target)

#search index value 

# arr=[10,20,30,15,35,40,45]
# target=35
# for i in range(len(arr)):
#     if arr[i]==target:
#         print("element is found at index",i)
#         break

#second highest 
# arr = [4, 9, 2, 15, 6, 8]
# highest=arr[0]
# second_highest=None
# for i in range(1,len(arr)):
#     if arr[i]>highest:
#         second_highest=highest
#         highest=arr[i]
#     elif arr[i]!=highest and (second_highest is None or arr[i]>second_highest):
#         second_highest=arr[i]
# print("second highest is ",second_highest)

#by using function 

# def secondhighest(arr):
#     highest=arr[0]
#     second_highest=None
#     for i in range(1,len(arr)):
#         if arr[i]>highest:
#             second_highest=highest
#             highest=arr[i]
#         elif arr[i]!=highest and (second_highest is None or arr[i]>second_highest):
#             second_highest=arr[i]
#     return second_highest
# arr=[10,20,40,30]
# result=secondhighest(arr)
# print("secondgighest is ",result)

#reverse an array 
# arr=[10,20,40,30]
# left=0
# right=len(arr)-1
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print(arr)


#find the average
# arr=[10,20,30,42,32]
# total=0
# for i in arr:
#     total=total+i
# print("the sum of array is :",total)
# average=total/len(arr)
# print("the average of array is :",average)

#by using function
# def average1(arr):
#     total=0
#     for i in arr:
#         total=total+i
#     return total/len(arr)
# arr=[10,20,30,43,45,30]
# result=average1(arr)
# print(result)

#count negative,positive and zero
# arr=[10,20,-11,-2,0,-12,14,0,-18,0]
# positive=0
# negative=0
# zero=0
# for i in arr:
#     if i>0:
#         positive+=1
#     elif i<0:
#         negative+=1
#     else:
#         zero=+1

# print("positive numbers are :",positive)
# print("negative numbers are :",negative)
# print("zeros are :",zero)

#remove duplicates 
# arr=[10,20,30,10,20,30]
# result=[]
# for i in arr:
#     if i not in result:
#         result.append(i)
# print(result)


#DAY 2 
#reverse
# arr = [5, 10, 15, 20, 25]
# left=0
# right=len(arr)-1
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     right-=1
#     left+=1
# print(arr)


#palindrome 
# arr = [1, 2, 3, 2, 1]
# left=0
# right=len(arr)-1
# while left < right:
#     if arr[left]!=arr[right]:
#         print("it is not a palindrome")
#         break
#     left+=1
#     right-=1
# else:
#     print("it is a palindrome")

#two sum
# arr = [1, 2, 3, 4, 6, 8, 11]
# target = 14
# left=0
# right=len(arr)-1
# while left < right:
#     total=arr[left]+arr[right]
#     if total==target:
#         print(arr[left],arr[right])
#         break
#     elif total<target:
#         left+=1
#     else:
#         right-=1


#three sum
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# target = 15
# fixed=1
# left=0
# right=len(arr)-1
# while left < right:
#     total=arr[fixed]+arr[left]+arr[right]
#     if total==target:
#         print(arr[fixed]+arr[left]+arr[right])
#         break
#     elif total<target:
#         left+=1
#     else:
#         right-=1

#move zeros 
# arr = [0, 1, 0, 3, 12]
# j=0
# for i in range(len(arr)):
#     if arr[i]!=0:
#         arr[i],arr[j]=arr[j],arr[i]
#         j+=1
# print(arr)

#remove duplicates 
arr = [1, 1, 2, 2, 3, 4, 4]
i=0
for j in range(1,len(arr)):
    if arr[i]!=arr[j]:
        i+=1
        arr[i]=arr[j]
print(arr[:i+1])