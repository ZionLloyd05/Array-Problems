
def linear(arr, x):

    if(arr[0] == x):
        print ("ceil => ",x)

    for i in range(len(arr)):
        if(i+1 < len(arr)):
            if(arr[i] < x and x < arr[i+1]):
                print ("ceil => ", arr[i+1])

            if(arr[i] < x and x <= arr[i+1]):
                print("floor => ", arr[i])
        else:
            if(arr[i] < x):
                print("floor => ", arr[i])
                

def binarySearch(arr, low, high, x):

    mid = int((low + high)/2)

    if(arr[0] == x):
        print ("ceil => ",x)

    if(arr[mid] < x and x < arr[mid+1]):
        print("floor => ", arr[mid])
        print("ceil => ", arr[mid+1])
    else:
        if(x < arr[mid]):
            binarySearch(arr, low, mid, x)
        else:
            binarySearch(arr, mid, high, x)

arr = [1,2,8,10,10,12,19]
linear(arr, 5)
binarySearch(arr, 0, len(arr), 5)
