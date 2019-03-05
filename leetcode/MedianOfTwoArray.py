a = [1,3]
b = [2]

arr = sorted(a+b)
print(arr)
arr_len = len(arr)
if arr_len%2 == 0:
    print(arr[int(arr_len/2-1)])
    median = (arr[int(arr_len/2)-1] + arr[int(arr_len/2)])/2
else:
    median = arr[int((arr_len + 1)/2)-1]

print(median)

