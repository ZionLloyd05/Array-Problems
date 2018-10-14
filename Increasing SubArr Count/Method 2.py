
count = 0
lenght = 1

arr = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(arr)):
    print("i => ", i)
    if(i < len(arr) and (i+1) < len(arr)):
        if(arr[i+1] > arr[i]):
            print("arr[i] => ", arr[i])
            print("arr[i+1] => ", arr[i+1])
            lenght += 1
            print("lenght => ", lenght)

        else:
            count += (((lenght - 1) * lenght) / 2)
            print("count in loop => ", count)
            lenght = 1
            print("lenght turned 1 => ")

if(lenght > 1):
    count += (((lenght - 1) * lenght) / 2)
    print("count outside loop => ", count)
print(count)
