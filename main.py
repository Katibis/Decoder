# Samy's code

def decoder(p):
    temp = ""
    for i in p:
        temp += str((int(i) + 7) % 10)
    return temp
print(decoder("45678888"))