#20 random cards are placed in a row, all face down. A move consists of turning a face down card, face up and turning over the card 
#immediately to the right. Show that no matter what the choice of cards to turn, this sequence of moves must terminate.


def transform(b):
    for i in range(len(b)-1):
        if b[i] == '1':
            b[i] = '0'
            if b[i+1] == '0':
                b[i+1] = '1'
            else:
                b[i+1] = '1'

    return b
if __name__ == "__main__":
    a = list("01111110000")
    print(a)
    while a != transform(a.copy()):
        a = transform(a.copy())
    print(a)