buyers = {}
a = {buyers.setdefault(buyer + ':', dict()).setdefault(product, []).append(int(count)) for i in range(int(input())) for
     buyer, product, count in [input().split()]}

for b in sorted(buyers):
    print(b)
    [print(f"{p}{' '}{sum(c)}") for p, c in sorted(buyers[b].items())]
