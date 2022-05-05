A = int(input())
B = int(input())
C = int(input()) 

D = A

if B < D:
    D = B

if C < D:
    D = C
A=A-D
B=B-D
C=C-D
print(A, B, C)    
