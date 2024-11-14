
bin_list = [2**x - 1 for x in range(50)] # 10^15 ~= 2^50 이진수 50개는 필요함

def number_to_binary(x):
    x = bin(x)[2:]
    if len(x) in bin_list:
        return x
    for n in bin_list:
        if n > len(x):
            x = "0"*(n-len(x))+x
            break
    return x
     
def search(n):
    if '0' not in n or '1' not in n or len(n) == 1:
        return True
    
    mid = n[len(n)//2]
    if mid == '0':
        return False
    return search(n[:len(n)//2]) and search(n[len(n)//2+1:])
    
def solution(numbers):
    bin_numbers = list(map(number_to_binary, numbers))
    answer = []
    for n in bin_numbers:
        answer.append(1 if search(n) else 0)
    return answer