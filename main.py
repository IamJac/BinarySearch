from array import *
def binary_search(data_array,left,right,target):
    if left>right:
        print("The value ",target," is not within the array")
    else:
        mid=(left+right)//2
        if target==data_array[mid]:
            print("The value ",target," has been found at index ",mid)
        elif target>data_array[mid]:
            left=mid+1
            binary_search(data_array, left, right, target)
        else:
            right=mid-1
            binary_search(data_array, left, right, target)

data=array('i',[])
size=int(input("Input size of the array"))
print("Input integral values into the array")
for i in range(0,size,1):
    inputs=int(input())
    data.append(inputs)
print() #For a new line
print("User input")
for j in data:
    print(j,end=" ")
print()
data1=sorted(data)
print("Sorted array elements")
for t in data1:
    print(t,end=" ")
print()
num=int(input("Input a value to be searched in the array"))
binary_search(data1,0,size-1,num)
