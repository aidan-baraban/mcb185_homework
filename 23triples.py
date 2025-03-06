## Pythagorean Triples

def find_pythagorean_triples():
    triples = []
    for a in range(1, 100):
        for b in range(a, 100):
            c = (a**2 + b**2) ** 0.5
            if c % 1 == 0:
                triples += [(a, b, int(c))]
    return triples
    
triples = find_pythagorean_triples()

for triple in triples:
    print(triple)