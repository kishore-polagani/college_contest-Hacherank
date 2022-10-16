Given a matrix of size N x M, print row-wise sum, separated by a newline.
Note: Try to solve this without declaring/storing the matrix.

Input Format

First line of input contains N, M - the size of the matrix. Its followed by N lines each containing M integers - elements of the matrix.

Constraints

1 <= N, M <= 100
-106 <= ar[i] <= 106

Output Format

Print row-wise sum of the matrix, separated by a newline.

Sample Input 0

2 3
5 -1 3
19 8 -5
Sample Output 0

7
22
....

x=list(map(int,input().split()))
n=x[0]
m=x[1]
for i in range(n):
    l=list(map(int,input().split()))
    s=0
    for j in range(m):
        s=s+l[j]
    print(s)
