def binario(decimal):
    if decimal == 0: 
        return 0
    else: 
        return decimal % 2 + binario(decimal // 2) * 10

print(binario(15000))