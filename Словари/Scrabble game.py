scrabble = {1: 'AEILNORSTU', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
print(sum(k for i in input() for k in scrabble if i in scrabble[k]))
