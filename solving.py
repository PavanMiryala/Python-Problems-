import numpy as np
import datetime
# arr=np.array([[10,20,30],
#               [20,30,50],
#               [40,50,60]])
# print(arr)

# arr=np.arange(1,10).reshape(3,3)
# print(arr)

# arr=np.zeros((3,4),dtype=int)
# print(arr)


# arr=np.ones((3,4),dtype=int)
# print(arr)

# arr=np.full((3,4),4)
# print(arr)

# arr=np.arange(1,20,2)
# mat=arr.reshape(2,5)
# print(arr)
# print(mat)

start=datetime.datetime.now()
#arr=np.linspace(0,50,6)
arr=np.identity(4)
arr = np.fliplr(arr)    #it gives reverse identity matrix that is used as fliplr 
end=datetime.datetime.now()-start
print(arr)
print(start)
print(end)