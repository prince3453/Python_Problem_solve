def rotate(arr,d):
    n = len(arr)
    lst = []
    lst = arry[d:]+arry[:d]
    return lst

def rotate_l(arr,d):
    n = len(arr)
    lst = []
    lst = arry[-d:]+arry[:-d]
    return lst
    
arry = input("Enter the array to rotate : ").split(',')
d = input("Enter the position to rotate on left or right side Please Enter (L/R) : ").upper()
c = int(input("Ente the rotational movement : "))
if d == 'L':
    print(rotate(arry,c))
elif d == 'R':
    print(rotate_l(arry,c))
else:
    print('Enter proper choice...')
