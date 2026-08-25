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