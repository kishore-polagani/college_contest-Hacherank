Given an array on integers, search a given key in the array using linear search.
Note: Do not use any inbuilt functions/libraries for your main logic.

Input Format

First line of input contains two integers, N - size of the array and K - search key. Second line contains the elements of the array.

Constraints

1 <= N <= 102
0 <= ar[i] <= 109

Output Format

If key is found, print the index of the array, otherwise print -1.

Sample Input 0

5 15
-2 -19 8 15 4
Sample Output 0

3
...

x=list(map(int,input().split()))
y=x[0]
z=x[1]
l=[]
p=list(map(int,input().split()))
for i in range(y):
    if z==p[i]:
        l.append(i)
if len(l)==0:
    print("-1")
else:
    print(l[0])
