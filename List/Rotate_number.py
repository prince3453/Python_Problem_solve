def rotate(arr,d):
    n = len(arr)
    lst = []
    lst = arry[d:]+arry[:d]
    return lst
    
arry = input("Enter the array to rotate : ").split(',')
d = int(input("Enter the position to rotate on left side : "))

print(rotate(arry,d))
