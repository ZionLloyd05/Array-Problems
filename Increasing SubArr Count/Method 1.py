
arr = [1,2,3]

count = 0
n = len(arr)
j = 0

for i in range(len(arr)):
    x = i+1
    
    for j in range(len(arr)):

        if(x < len(arr)):
            if(arr[x] > arr[x-1]):
                count += 1
                x += 1
            else:
                break

print("No of Increasing sub array => ",count);
    
