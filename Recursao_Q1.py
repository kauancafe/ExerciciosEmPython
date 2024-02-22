def div(m, n):
    if n > m:
        return 0
    else: 
        return 1 + div(m - n, n)

print(div(8, 2))