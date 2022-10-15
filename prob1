Find a duplicate element in the given array of integers. There will be only a single duplicate element in the array.
Note: Do not use any inbuilt functions/libraries for your main logic.

Input Format

First line of input contains size of the array - N and second line contains the elements of the array.

Constraints

2 <= N <= 100
0 <= ar[i] <= 109

Output Format

Print the duplicate element from the given array.

Sample Input 0

6
5 4 10 9 21 10
Sample Output 0

10
.......

n=int(input())
x=list(map(int,input().split()))
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if x[i]==x[j]:
            print(x[j],end=" ")
