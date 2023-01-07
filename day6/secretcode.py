def encoder(x):
    return x[::-1]
def decoder(y):
    return y[::-1]

x  = input("enter a text to encrypt ")
print(encoder(x))

print(decoder(encoder(x)), "  here is decoded one ")