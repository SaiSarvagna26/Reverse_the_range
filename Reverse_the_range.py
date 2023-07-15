def reverse_range(A, B, C):
    A[B:C+1] = reversed(A[B:C+1])
    return A


A = list(map(int,input().split()))
B = int(input())
C = int(input())
result = reverse_range(A, B, C)
print(result)  
