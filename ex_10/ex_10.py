fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrive/create/update counter
        di[w] = di.get(w, 0) + 1

print(di)

x = sorted([(y, x) for x, y in di.items()], reverse=True)
print(x[:5])
