##Write a Python Program to compute the multiplication of two matrices and then print it.
A = [[1, 2, 4],
     [3, 6, 9],
     [5, 10,15]]

B = [[2,4,8],
     [4,6,16],
     [6,12,18]]

C = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for m in range(len(B)):

            C[i][j] += A[i][m] * B[m][j]
        for p in C:
            print(p)



###Write a Python program to find yesterday, today, and tomorrow's date.
import datetime
today = datetime.date.today()
yesterday = today- datetime.timedelta(days=1)

tomorrow = today + datetime.timedelta (days=1)

print('yesterday: ' ,yesterday)
print('today : ', today)
print('tomorrow :',tomorrow)





##Write a Python program to find Nth largest number in a list.
list_element = [50 , 500, 5000,1000,2000,3000]
n = 2
print("Largest num is :" ,)

list_element.sort()
print(list_element[-n:])



















