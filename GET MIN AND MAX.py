# GET MIN AND MAX
print("Get MIX and MAX")
print("")#...space
print("")#...space
def get_min(arr,n):
    res = arr[0]
    for i in range(n):
        res = min(res, arr[i])
    return res

def get_max(arr,n):
    res = arr[0]
    for i in range(1,n):  #corrected the loop range
        res = max(res,arr[i])
    return res

# Driver program
arr = [12,1234,45,67]
n = len(arr)
print(">>> Minimum element in the array ")
print("---Minimum element of array:",get_min(arr,n))
print("")#.....space
print(">>> Mzximum element in the array")
print("---Maximum elemenet of array:",get_max(arr,n))
