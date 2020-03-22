def subtractProductAndSum(n):
    num_list = [int(d) for d in str(n)]
    prod, summ = 1, 0
    for digit in num_list:
        prod = prod * digit
        summ = summ + digit
    return prod - summ    

print(subtractProductAndSum(234))