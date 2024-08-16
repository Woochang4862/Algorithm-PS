'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}

1 2~n -> n-1
2 3~n -> n-2
3 4~n -> n-3
...
n-1 n~n -> 1

(n-1 + 1)/2*(n-1) = n*(n-1)/2
'''
N = int(input())
print(N*(N-1)//2)
print(2)