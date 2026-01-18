def sum_gp(a,r,n):
    if r==1:
        return a*n
    return a*(r**n-1)//(r-1)

print(sum_gp(2, 2, 5))  # 62