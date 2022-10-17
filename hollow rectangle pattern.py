Print hollow rectangle pattern using '*'. See example for more details.

Input Format

Input contains two integers W - width of the rectangle and L - length of the rectangle.

Constraints

2 <= W <= 50
2 <= L <= 50

Output Format

For the given integers W and L, print the hollow rectangle pattern.

Sample Input 0

5 4
Sample Output 0

*****
*   *
*   *
*****
...

x,y=list(map(int,input().split()))
for i in range(1,y+1):
    for j in range(1,x+1):
        if (i==1 or i==y or j==1 or j==x):
            print("*",end="")
        else:
            print(" ",end="")
    print()
