def nCr(n,r):
    start = 1
    for i in range(r):
        start = start*(n-i)/(r-i)
    return start
for i in range(14,21):
    value = nCr(2000,i)*0.5**nCr(i,2)
    print(f"{i}&{value:0.5E}\\\\")
